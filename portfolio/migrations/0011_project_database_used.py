# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20170330_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='database_used',
            field=models.ManyToManyField(to='portfolio.Database'),
        ),
    ]
