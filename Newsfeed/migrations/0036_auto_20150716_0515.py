# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0035_auto_20150716_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('comment_text', models.CharField(default=b'default', max_length=100)),
                ('hideBit', models.IntegerField(default=0, max_length=1)),
                ('courseNum', models.IntegerField(default=b'null', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_name', models.CharField(max_length=45)),
                ('courseDesc', models.CharField(max_length=100)),
                ('courseFee', models.IntegerField(null=True)),
                ('createdTS', models.DateTimeField(auto_now_add=True)),
                ('hideBit', models.IntegerField(default=1, max_length=1)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('professor', models.CharField(default=b'null', max_length=40, null=True)),
                ('courseNum', models.IntegerField(default=b'null', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('lesson_name', models.CharField(max_length=45)),
                ('lessonDesc', models.CharField(max_length=100)),
                ('createdTS', models.DateTimeField(auto_now_add=True)),
                ('hideBit', models.IntegerField(default=1, max_length=1)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('courseString', models.CharField(default=b'null', max_length=20, null=True)),
                ('courseNum', models.IntegerField(default=b'null', serialize=False, primary_key=True)),
                ('course', models.ForeignKey(to='Newsfeed.course', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('role', models.CharField(default=b'Student', max_length=20)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.EmailField(unique=True, max_length=75)),
                ('phone_number', models.CharField(max_length=20)),
                ('isActive', models.IntegerField(default=0, max_length=1)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0, null=True)),
                ('hideBit', models.IntegerField(default=0, null=True)),
                ('courseNum', models.IntegerField(default=b'null', serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PeopleCourse',
            fields=[
                ('courseNum', models.IntegerField(default=b'null', serialize=False, primary_key=True)),
                ('course', models.ForeignKey(to='Newsfeed.course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('like', models.CharField(max_length=10)),
                ('courseNum', models.IntegerField(default=b'null', serialize=False, primary_key=True)),
                ('rate', models.IntegerField()),
                ('comment', models.ForeignKey(to='Newsfeed.comment')),
                ('people', models.ForeignKey(to='Newsfeed.People')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='recommendedList',
            fields=[
                ('courseNum', models.IntegerField(default=b'null', serialize=False, primary_key=True)),
                ('recommendedClass', models.ForeignKey(to='Newsfeed.course')),
                ('student', models.ForeignKey(to='Newsfeed.People')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='wishList',
            fields=[
                ('courseNum', models.IntegerField(default=b'null', serialize=False, primary_key=True)),
                ('student', models.ForeignKey(to='Newsfeed.People')),
                ('wishListClass', models.ForeignKey(to='Newsfeed.course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='comment',
            name='course',
            field=models.ForeignKey(to='Newsfeed.course', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='lesson',
            field=models.ForeignKey(to='Newsfeed.lesson', null=True),
            preserve_default=True,
        ),
    ]
