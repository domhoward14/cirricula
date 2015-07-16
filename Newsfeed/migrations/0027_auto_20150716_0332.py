# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0026_auto_20150716_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slugName',
            field=models.SlugField(default=uuid.uuid1),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='slugName',
            field=models.SlugField(default=uuid.uuid1),
        ),
        migrations.AlterField(
            model_name='people',
            name='peopleSlugName',
            field=models.SlugField(default=uuid.uuid1),
        ),
    ]
