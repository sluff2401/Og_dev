# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogevents', '0004_auto_20151107_0943'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='is_schememanager',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='schememanager',
        ),
    ]
