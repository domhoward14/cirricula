# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0023_people_slugname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='slugName',
            new_name='peopleSlugName',
        ),
    ]
