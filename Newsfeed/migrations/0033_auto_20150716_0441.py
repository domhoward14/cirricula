# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0032_auto_20150716_0424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='courseId',
            new_name='courseNum',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parentId',
        ),
        migrations.RemoveField(
            model_name='peoplecourse',
            name='peopleId',
        ),
    ]
