# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0028_auto_20150716_0335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='slugName',
            new_name='lessonSlugName',
        ),
    ]
