# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0010_auto_20150701_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reccommendedlist',
            name='student',
            field=models.ForeignKey(to='Newsfeed.People', null=True),
        ),
    ]
