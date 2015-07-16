# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0031_auto_20150716_0420'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_id',
            new_name='courseId',
        ),
    ]
