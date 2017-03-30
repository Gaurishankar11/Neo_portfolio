# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_project_database_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='production_link',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='third_party_library',
            field=models.ManyToManyField(to='portfolio.Library', null=True, blank=True),
        ),
    ]
