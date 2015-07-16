# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0018_auto_20150702_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='professor',
            field=models.CharField(default=b'null', max_length=40, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='lesson',
            name='courseString',
            field=models.CharField(default=b'null', max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='lesson',
            name='course',
            field=models.ForeignKey(to='Newsfeed.course', null=True),
        ),
    ]
