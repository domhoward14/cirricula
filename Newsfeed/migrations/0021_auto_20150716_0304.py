# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0020_auto_20150716_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(unique=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='course',
            name='slugName',
            field=models.SlugField(default=b'null'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='lesson_name',
            field=models.CharField(unique=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slugName',
            field=models.SlugField(default=b'null'),
        ),
        migrations.AlterField(
            model_name='people',
            name='slugName',
            field=models.SlugField(default=b'null'),
        ),
    ]
