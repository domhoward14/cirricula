# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0004_course_hidebit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseFee',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='hideBit',
            field=models.IntegerField(default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='people',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
