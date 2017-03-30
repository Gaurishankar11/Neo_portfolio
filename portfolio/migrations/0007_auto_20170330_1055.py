# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20170329_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('status', models.BooleanField(default=False, max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order_sequence']},
        ),
        migrations.RemoveField(
            model_name='project',
            name='oreder_sequence',
        ),
        migrations.AddField(
            model_name='project',
            name='logo',
            field=models.ImageField(upload_to=b'media', blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='order_sequence',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='category',
            field=models.ForeignKey(blank=True, to='portfolio.Category', null=True),
        ),
    ]
