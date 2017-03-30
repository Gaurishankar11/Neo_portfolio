# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_auto_20170330_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='db_type',
            field=models.CharField(default=b'Other', max_length=20, choices=[(b'NoSql', b'NoSql'), (b'RDBMS', b'RDBMS'), (b'Other', b'Other')]),
        ),
        migrations.AlterField(
            model_name='database',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
