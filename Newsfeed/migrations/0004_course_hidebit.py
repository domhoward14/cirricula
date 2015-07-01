# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0003_auto_20150610_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='hideBit',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=True,
        ),
    ]
