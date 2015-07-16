# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0015_auto_20150701_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='role',
            field=models.CharField(default=b'Student', max_length=20),
        ),
    ]
