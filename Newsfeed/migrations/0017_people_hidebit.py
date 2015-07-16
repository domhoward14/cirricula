# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0016_auto_20150702_0749'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='hideBit',
            field=models.IntegerField(default=0, null=True),
            preserve_default=True,
        ),
    ]
