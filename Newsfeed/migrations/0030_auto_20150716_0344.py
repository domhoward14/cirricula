# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0029_auto_20150716_0338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='slugName',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='lessonSlugName',
        ),
        migrations.RemoveField(
            model_name='people',
            name='peopleSlugName',
        ),
    ]
