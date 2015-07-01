# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0008_auto_20150701_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='hideBit',
            field=models.IntegerField(default=1, max_length=1),
        ),
    ]
