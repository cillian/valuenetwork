# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0005_auto_20170319_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_type',
        ),
        migrations.RemoveField(
            model_name='company',
            name='human',
        ),
        migrations.RemoveField(
            model_name='human',
            name='addresses',
        ),
        migrations.RemoveField(
            model_name='human',
            name='companies',
        ),
        migrations.RemoveField(
            model_name='human',
            name='jobs',
        ),
        migrations.RemoveField(
            model_name='human',
            name='materials',
        ),
        migrations.RemoveField(
            model_name='human',
            name='nonmaterials',
        ),
        migrations.RemoveField(
            model_name='human',
            name='persons',
        ),
        migrations.RemoveField(
            model_name='human',
            name='projects',
        ),
        migrations.RemoveField(
            model_name='human',
            name='records',
        ),
        migrations.RemoveField(
            model_name='human',
            name='regions',
        ),
        migrations.RemoveField(
            model_name='image',
            name='nonmaterial',
        ),
        migrations.RemoveField(
            model_name='material',
            name='addresses',
        ),
        migrations.RemoveField(
            model_name='material',
            name='jobs',
        ),
        migrations.RemoveField(
            model_name='material',
            name='material_type',
        ),
        migrations.RemoveField(
            model_name='material',
            name='materials',
        ),
        migrations.RemoveField(
            model_name='material',
            name='nonmaterials',
        ),
        migrations.RemoveField(
            model_name='material',
            name='records',
        ),
        migrations.RemoveField(
            model_name='nonmaterial',
            name='addresses',
        ),
        migrations.RemoveField(
            model_name='nonmaterial',
            name='jobs',
        ),
        migrations.RemoveField(
            model_name='nonmaterial',
            name='nonmaterial_type',
        ),
        migrations.RemoveField(
            model_name='nonmaterial',
            name='nonmaterials',
        ),
        migrations.RemoveField(
            model_name='nonmaterial',
            name='records',
        ),
        migrations.RemoveField(
            model_name='person',
            name='human',
        ),
        migrations.RemoveField(
            model_name='project',
            name='human',
        ),
        migrations.RemoveField(
            model_name='project',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='project',
            name='project_type',
        ),
        migrations.RemoveField(
            model_name='rel_human_addresses',
            name='address',
        ),
        migrations.RemoveField(
            model_name='rel_human_addresses',
            name='human',
        ),
        migrations.RemoveField(
            model_name='rel_human_addresses',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_human_companies',
            name='company',
        ),
        migrations.RemoveField(
            model_name='rel_human_companies',
            name='human',
        ),
        migrations.RemoveField(
            model_name='rel_human_companies',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_human_jobs',
            name='human',
        ),
        migrations.RemoveField(
            model_name='rel_human_jobs',
            name='job',
        ),
        migrations.RemoveField(
            model_name='rel_human_jobs',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_human_materials',
            name='human',
        ),
        migrations.RemoveField(
            model_name='rel_human_materials',
            name='material',
        ),
        migrations.RemoveField(
            model_name='rel_human_materials',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_human_nonmaterials',
            name='human',
        ),
        migrations.RemoveField(
            model_name='rel_human_nonmaterials',
            name='nonmaterial',
        ),
        migrations.RemoveField(
            model_name='rel_human_nonmaterials',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_human_persons',
            name='human',
        ),
        migrations.RemoveField(
            model_name='rel_human_persons',
            name='person',
        ),
        migrations.RemoveField(
            model_name='rel_human_persons',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_human_projects',
            name='human',
        ),
        migrations.RemoveField(
            model_name='rel_human_projects',
            name='project',
        ),
        migrations.RemoveField(
            model_name='rel_human_projects',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_human_records',
            name='human',
        ),
        migrations.RemoveField(
            model_name='rel_human_records',
            name='record',
        ),
        migrations.RemoveField(
            model_name='rel_human_records',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_human_regions',
            name='human',
        ),
        migrations.RemoveField(
            model_name='rel_human_regions',
            name='region',
        ),
        migrations.RemoveField(
            model_name='rel_human_regions',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_material_addresses',
            name='address',
        ),
        migrations.RemoveField(
            model_name='rel_material_addresses',
            name='material',
        ),
        migrations.RemoveField(
            model_name='rel_material_addresses',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_material_jobs',
            name='job',
        ),
        migrations.RemoveField(
            model_name='rel_material_jobs',
            name='material',
        ),
        migrations.RemoveField(
            model_name='rel_material_jobs',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_material_materials',
            name='material',
        ),
        migrations.RemoveField(
            model_name='rel_material_materials',
            name='material2',
        ),
        migrations.RemoveField(
            model_name='rel_material_materials',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_material_nonmaterials',
            name='material',
        ),
        migrations.RemoveField(
            model_name='rel_material_nonmaterials',
            name='nonmaterial',
        ),
        migrations.RemoveField(
            model_name='rel_material_nonmaterials',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_material_records',
            name='material',
        ),
        migrations.RemoveField(
            model_name='rel_material_records',
            name='record',
        ),
        migrations.RemoveField(
            model_name='rel_material_records',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_nonmaterial_addresses',
            name='address',
        ),
        migrations.RemoveField(
            model_name='rel_nonmaterial_addresses',
            name='nonmaterial',
        ),
        migrations.RemoveField(
            model_name='rel_nonmaterial_addresses',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_nonmaterial_jobs',
            name='job',
        ),
        migrations.RemoveField(
            model_name='rel_nonmaterial_jobs',
            name='nonmaterial',
        ),
        migrations.RemoveField(
            model_name='rel_nonmaterial_jobs',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_nonmaterial_nonmaterials',
            name='nonmaterial',
        ),
        migrations.RemoveField(
            model_name='rel_nonmaterial_nonmaterials',
            name='nonmaterial2',
        ),
        migrations.RemoveField(
            model_name='rel_nonmaterial_nonmaterials',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='rel_nonmaterial_records',
            name='nonmaterial',
        ),
        migrations.RemoveField(
            model_name='rel_nonmaterial_records',
            name='record',
        ),
        migrations.RemoveField(
            model_name='rel_nonmaterial_records',
            name='relation',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='human',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Human',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
        migrations.DeleteModel(
            name='Nonmaterial',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='rel_Human_Addresses',
        ),
        migrations.DeleteModel(
            name='rel_Human_Companies',
        ),
        migrations.DeleteModel(
            name='rel_Human_Jobs',
        ),
        migrations.DeleteModel(
            name='rel_Human_Materials',
        ),
        migrations.DeleteModel(
            name='rel_Human_Nonmaterials',
        ),
        migrations.DeleteModel(
            name='rel_Human_Persons',
        ),
        migrations.DeleteModel(
            name='rel_Human_Projects',
        ),
        migrations.DeleteModel(
            name='rel_Human_Records',
        ),
        migrations.DeleteModel(
            name='rel_Human_Regions',
        ),
        migrations.DeleteModel(
            name='rel_Material_Addresses',
        ),
        migrations.DeleteModel(
            name='rel_Material_Jobs',
        ),
        migrations.DeleteModel(
            name='rel_Material_Materials',
        ),
        migrations.DeleteModel(
            name='rel_Material_Nonmaterials',
        ),
        migrations.DeleteModel(
            name='rel_Material_Records',
        ),
        migrations.DeleteModel(
            name='rel_Nonmaterial_Addresses',
        ),
        migrations.DeleteModel(
            name='rel_Nonmaterial_Jobs',
        ),
        migrations.DeleteModel(
            name='rel_Nonmaterial_Nonmaterials',
        ),
        migrations.DeleteModel(
            name='rel_Nonmaterial_Records',
        ),
    ]
