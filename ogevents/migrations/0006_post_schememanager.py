# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogevents', '0005_auto_20151107_1012'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='schememanager',
            field=models.ForeignKey(blank=True, null=True, related_name='post_scheme_manager', to='ogevents.Manager'),
        ),
    ]
