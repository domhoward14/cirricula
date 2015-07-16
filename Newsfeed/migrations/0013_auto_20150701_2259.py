# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0012_auto_20150701_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lessonPre',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
