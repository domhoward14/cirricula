# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0017_people_hidebit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='dislikes',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
