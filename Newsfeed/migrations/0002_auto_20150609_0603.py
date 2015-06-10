# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Newsfeed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('course_name', models.CharField(max_length=45)),
                ('courseDesc', models.CharField(max_length=100)),
                ('courseFee', models.IntegerField()),
                ('createdTS', models.DateTimeField(auto_now_add=True)),
                ('course_id', models.IntegerField(serialize=False, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='lesson',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lesson_name', models.CharField(max_length=45)),
                ('lessonDesc', models.CharField(max_length=100)),
                ('lessonPre', models.CharField(max_length=100)),
                ('createdTS', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(to='Newsfeed.course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=75)),
                ('phone_number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PeopleCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(to='Newsfeed.course')),
                ('peopleId', models.ForeignKey(to='Newsfeed.People')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ratings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like', models.CharField(max_length=10)),
                ('rate', models.IntegerField()),
                ('comment', models.ForeignKey(to='Newsfeed.comment')),
                ('people', models.ForeignKey(to='Newsfeed.People')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='reccommendedList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student', models.ForeignKey(to='Newsfeed.People')),
                ('wishListClass', models.ForeignKey(to='Newsfeed.course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent_id',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='status',
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
        migrations.AddField(
            model_name='comment',
            name='parentId',
            field=models.ForeignKey(to='Newsfeed.comment', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.CharField(default=b'default', max_length=100),
        ),
    ]
