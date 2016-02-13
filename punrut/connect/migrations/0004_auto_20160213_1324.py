# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0003_auto_20160213_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_profile_update',
            name='student_profile_pic',
            field=models.FileField(upload_to=b''),
        ),
    ]
