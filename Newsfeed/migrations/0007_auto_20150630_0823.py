# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0006_auto_20150630_0814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tempreccommendedlist',
            name='recommendedClass',
            field=models.CharField(max_length=20),
        ),
    ]
