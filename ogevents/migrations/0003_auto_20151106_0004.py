# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ogevents', '0002_userdetail_is_schememanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='details',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='schememanager',
            field=models.ForeignKey(related_name='scheme_manager', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
