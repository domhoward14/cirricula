# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0034_auto_20150716_0446'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='course',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='lesson',
            name='course',
        ),
        migrations.DeleteModel(
            name='lesson',
        ),
        migrations.RemoveField(
            model_name='peoplecourse',
            name='course',
        ),
        migrations.DeleteModel(
            name='PeopleCourse',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='comment',
        ),
        migrations.DeleteModel(
            name='comment',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='people',
        ),
        migrations.DeleteModel(
            name='ratings',
        ),
        migrations.RemoveField(
            model_name='recommendedlist',
            name='recommendedClass',
        ),
        migrations.RemoveField(
            model_name='recommendedlist',
            name='student',
        ),
        migrations.DeleteModel(
            name='recommendedList',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='student',
        ),
        migrations.DeleteModel(
            name='People',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='wishListClass',
        ),
        migrations.DeleteModel(
            name='course',
        ),
        migrations.DeleteModel(
            name='wishList',
        ),
    ]
