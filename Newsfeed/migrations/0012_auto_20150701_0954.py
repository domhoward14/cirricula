# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0011_auto_20150701_0935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reccommendedlist',
            name='recommendedClass',
        ),
        migrations.RemoveField(
            model_name='reccommendedlist',
            name='student',
        ),
        migrations.DeleteModel(
            name='reccommendedList',
        ),
    ]
