# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0009_auto_20160213_1552'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_achievements',
            old_name='student_achievements_file',
            new_name='student_achievement_file',
        ),
    ]
