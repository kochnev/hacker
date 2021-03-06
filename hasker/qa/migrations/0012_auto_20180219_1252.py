# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-19 12:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qa', '0011_auto_20180219_0841'),
    ]

    operations = [
        migrations.CreateModel(
            name='Votes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_type', models.IntegerField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='answervote',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='answervote',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='answervote',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='questionvote',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='questionvote',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questionvote',
            name='user',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='voters',
        ),
        migrations.RemoveField(
            model_name='question',
            name='voters',
        ),
        migrations.DeleteModel(
            name='AnswerVote',
        ),
        migrations.DeleteModel(
            name='QuestionVote',
        ),
    ]
