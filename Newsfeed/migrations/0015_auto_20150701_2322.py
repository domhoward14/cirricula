# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0014_remove_lesson_lessonpre'),
    ]

    operations = [
        migrations.CreateModel(
            name='recommendedList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('recommendedClass', models.ForeignKey(to='Newsfeed.course')),
                ('student', models.ForeignKey(to='Newsfeed.People')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='tempReccommendedList',
        ),
    ]
