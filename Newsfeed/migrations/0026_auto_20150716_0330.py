# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0025_remove_people_peopleslugname'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='peopleSlugName',
            field=models.SlugField(default=uuid.uuid1, unique=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='slugName',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slugName',
            field=models.SlugField(default=uuid.uuid1, unique=True),
        ),
    ]
