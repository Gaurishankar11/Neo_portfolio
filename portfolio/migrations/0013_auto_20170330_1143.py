# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_auto_20170330_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='dev_link',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
    ]
