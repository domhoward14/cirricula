# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0013_auto_20150701_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='lessonPre',
        ),
    ]
