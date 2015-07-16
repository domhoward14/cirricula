# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0030_auto_20150716_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_name',
            field=models.CharField(max_length=45),
        ),
    ]
