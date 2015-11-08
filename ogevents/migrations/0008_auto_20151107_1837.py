# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ogevents', '0007_auto_20151107_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('author_name', models.CharField(max_length=20, default='schememanager')),
                ('event_date', models.DateField(max_length=10, verbose_name='Event date in the format yyyy-mm-dd, e.g for the 24th of August 2015, enter 2015-08-24')),
                ('event_detail', models.TextField(verbose_name='Event details')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_live', models.BooleanField(default=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='manager',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='schememanager',
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='schememanager',
            field=models.ForeignKey(blank=True, related_name='scheme_manager', null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.AddField(
            model_name='event',
            name='author',
            field=models.ForeignKey(to='ogevents.Userdetail'),
        ),
        migrations.AddField(
            model_name='event',
            name='schememanager',
            field=models.ForeignKey(blank=True, related_name='post_scheme_manager', null=True, to='ogevents.Userdetail'),
        ),
    ]
