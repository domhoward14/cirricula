# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0033_auto_20150716_0441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='id',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='id',
        ),
        migrations.RemoveField(
            model_name='people',
            name='id',
        ),
        migrations.RemoveField(
            model_name='peoplecourse',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='id',
        ),
        migrations.RemoveField(
            model_name='recommendedlist',
            name='id',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='id',
        ),
        migrations.AddField(
            model_name='comment',
            name='courseNum',
            field=models.IntegerField(default=b'null', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='courseNum',
            field=models.IntegerField(default=b'null', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='people',
            name='courseNum',
            field=models.IntegerField(default=b'null', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='peoplecourse',
            name='courseNum',
            field=models.IntegerField(default=b'null', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ratings',
            name='courseNum',
            field=models.IntegerField(default=b'null', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recommendedlist',
            name='courseNum',
            field=models.IntegerField(default=b'null', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='wishlist',
            name='courseNum',
            field=models.IntegerField(default=b'null', serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='courseNum',
            field=models.IntegerField(default=b'null', serialize=False, primary_key=True),
        ),
    ]
