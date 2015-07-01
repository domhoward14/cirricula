# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0007_auto_20150630_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='people',
            name='hideBit',
        ),
        migrations.AddField(
            model_name='course',
            name='dislikes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='dislikes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='people',
            name='dislikes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='people',
            name='likes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
