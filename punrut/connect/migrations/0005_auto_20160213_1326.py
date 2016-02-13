# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0004_auto_20160213_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_profile_update',
            name='student_phone',
            field=models.CharField(max_length=b'128'),
        ),
    ]
