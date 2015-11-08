# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ogevents', '0003_auto_20151106_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('is_schememanager', models.BooleanField(default=False)),
                ('details', models.TextField(null=True, blank=True)),
                ('schememanager', models.ForeignKey(null=True, blank=True, related_name='scheme_manager', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='author_name',
            field=models.CharField(default='schememanager', max_length=20),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Event details'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.DateField(max_length=10, verbose_name='Event date in the format yyyy-mm-dd, e.g for the 24th of August 2015, enter 2015-08-24'),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='schememanager',
            field=models.ForeignKey(null=True, blank=True, related_name='scheme_manager', to='ogevents.Manager'),
        ),
    ]
