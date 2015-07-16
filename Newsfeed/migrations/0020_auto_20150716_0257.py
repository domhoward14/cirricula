# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0019_auto_20150702_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slugName',
            field=models.SlugField(default=b'null', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='slugName',
            field=models.SlugField(default=b'null', unique=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='people',
            name='slugName',
            field=models.SlugField(default=b'null', unique=True),
            preserve_default=True,
        ),
    ]
