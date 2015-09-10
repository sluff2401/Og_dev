# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogevents', '0002_auto_20150801_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(help_text='Enter the details of the event'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.DateField(help_text='Enter event date in the format yyyy-mm-dd, e.g for the 24th of August 2015, enter 2015-08-24'),
        ),
    ]
