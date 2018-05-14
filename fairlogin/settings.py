import os
from django.conf                   import settings
from social_core.backends.open_id  import OpenIdAuth
from social_core.exceptions        import AuthMissingParameter
from fairlogin.social_core_backend import KeycloakOAuth2

SOCIAL_AUTH_KEYCLOAK_KEY = os.environ['SOCIAL_AUTH_KEYCLOAK_KEY']
SOCIAL_AUTH_KEYCLOAK_SECRET = os.environ['SOCIAL_AUTH_KEYCLOAK_SECRET']
SOCIAL_AUTH_KEYCLOAK_AUTHORIZATION_URL = os.environ['SOCIAL_AUTH_KEYCLOAK_AUTHORIZATION_URL']
SOCIAL_AUTH_KEYCLOAK_ACCESS_TOKEN_URL = os.environ['SOCIAL_AUTH_KEYCLOAK_ACCESS_TOKEN_URL']
SOCIAL_AUTH_KEYCLOAK_PUBLIC_KEY = os.environ['SOCIAL_AUTH_KEYCLOAK_PUBLIC_KEY']
SOCIAL_AUTH_KEYCLOAK_ID_KEY = 'email'
SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'fairlogin.social_core_pipeline.send_verification_email'
SOCIAL_AUTH_EMAIL_VALIDATION_URL = settings.LOGIN_URL + "?info=verify_email"
SOCIAL_AUTH_FORCE_EMAIL_VALIDATION = True

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'fairlogin.social_core_pipeline.mail_validation',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

AUTHENTICATION_BACKENDS = (
    'fairlogin.social_core_backend.KeycloakOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)
