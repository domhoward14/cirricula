# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0021_auto_20150716_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='slugName',
        ),
    ]
