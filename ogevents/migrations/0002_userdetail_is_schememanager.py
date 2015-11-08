# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogevents', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='is_schememanager',
            field=models.BooleanField(default=False),
        ),
    ]
