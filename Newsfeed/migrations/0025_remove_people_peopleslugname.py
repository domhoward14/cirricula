# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0024_auto_20150716_0317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='peopleSlugName',
        ),
    ]
