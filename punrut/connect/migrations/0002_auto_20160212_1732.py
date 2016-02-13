# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_skills',
            name='skill_name',
            field=models.CharField(max_length=b'128'),
        ),
    ]
