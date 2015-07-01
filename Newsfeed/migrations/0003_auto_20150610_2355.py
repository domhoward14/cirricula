# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0002_auto_20150609_0603'),
    ]

    operations = [
        migrations.DeleteModel(
            name='admin_login',
        ),
        migrations.AddField(
            model_name='comment',
            name='hideBit',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='hideBit',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='people',
            name='hideBit',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='people',
            name='isActive',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_id',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='email',
            field=models.EmailField(unique=True, max_length=75),
        ),
    ]
