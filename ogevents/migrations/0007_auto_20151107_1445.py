# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogevents', '0006_post_schememanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='user',
            field=models.OneToOneField(to='ogevents.Userdetail'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to='ogevents.Userdetail'),
        ),
        migrations.AlterField(
            model_name='post',
            name='schememanager',
            field=models.ForeignKey(to='ogevents.Userdetail', related_name='post_scheme_manager', null=True, blank=True),
        ),
    ]
