from account.models               import EmailAddress
from django.conf                  import settings
from django.contrib.auth.models   import User
from django.core.mail             import send_mail
from django.core.urlresolvers     import reverse
from django.http                  import HttpResponseRedirect
from social_core.exceptions       import InvalidEmail
from social_core.pipeline.partial import partial

@partial
def mail_validation(backend, details, is_new=False, *args, **kwargs):
    social              = kwargs.get('social')
    new_association     = kwargs.get('new_association')
    requires_validation = new_association and \
                          social is None and \
                          details['email'] and \
                          (backend.REQUIRES_EMAIL_VALIDATION or backend.setting('FORCE_EMAIL_VALIDATION', False))

    if no_user_with_email(details['email']):
        return HttpResponseRedirect(settings.LOGIN_URL + "?alert=account_not_found")

    if requires_validation:
        data = backend.strategy.request_data()
        if 'verification_code' in data:
            backend.strategy.session_pop('email_validation_address')
            if not backend.strategy.validate_email(details['email'],
                                                   data['verification_code']):
                return HttpResponseRedirect(settings.LOGIN_URL + "?alert=invalid_verification_code")
        else:
            current_partial = kwargs.get('current_partial')
            backend.strategy.send_email_validation(backend,
                                                   details['email'],
                                                   current_partial.token)
            backend.strategy.session_set('email_validation_address',
                                         details['email'])
            return backend.strategy.redirect(
                backend.strategy.setting('EMAIL_VALIDATION_URL')
            )

def send_verification_email(strategy, backend, code, partial_token):
    verify_url = strategy.build_absolute_uri(reverse('social:complete', args=(backend.name,))) + '?verification_code=' + code.code
    email      = code.email
    subject    = "Verify your account"
    message    = """Before you can login via Fairlogin you need to verify your email address by visiting the following link:

{verify_url}
""".format(verify_url=verify_url)

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

def no_user_with_email(email):
    return User.objects.filter(email__iexact=email).first() is None

