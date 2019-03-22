# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='f_change_data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lefteyex', models.CharField(max_length=100)),
                ('lefteyey', models.CharField(max_length=100)),
                ('rihgteyex', models.CharField(max_length=100)),
                ('rihgteyey', models.CharField(max_length=100)),
                ('rotation', models.CharField(max_length=100)),
                ('distance', models.CharField(max_length=100)),
                ('ratio', models.CharField(max_length=100)),
            ],
        ),
    ]
