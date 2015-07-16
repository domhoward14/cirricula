# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0022_remove_people_slugname'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='slugName',
            field=models.SlugField(default=b'null'),
            preserve_default=True,
        ),
    ]
