# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import __builtin__


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0027_auto_20150716_0332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slugName',
            field=models.SlugField(default=__builtin__.id),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slugName',
            field=models.SlugField(default=__builtin__.id),
        ),
        migrations.AlterField(
            model_name='people',
            name='peopleSlugName',
            field=models.SlugField(default=__builtin__.id),
        ),
    ]
