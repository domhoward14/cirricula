# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0009_auto_20150701_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reccommendedlist',
            name='recommendedClass',
            field=models.ForeignKey(to='Newsfeed.course', null=True),
        ),
    ]
