# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0005_auto_20150630_0601'),
    ]

    operations = [
        migrations.CreateModel(
            name='tempReccommendedList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student', models.CharField(max_length=20)),
                ('recommendedBy', models.CharField(default=b'admin', max_length=20, null=True)),
                ('recommendedClass', models.ForeignKey(to='Newsfeed.course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='reccommendedlist',
            name='recommendedBy',
            field=models.CharField(default=b'admin', max_length=20, null=True),
            preserve_default=True,
        ),
    ]
