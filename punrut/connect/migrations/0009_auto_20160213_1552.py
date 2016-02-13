# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0008_student_certifications_student_certification_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_achievements',
            name='student_achievements_file',
            field=models.FileField(default=0, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student_achievements',
            name='student_achievement_description',
            field=models.CharField(max_length=b'128'),
        ),
        migrations.AlterField(
            model_name='student_achievements',
            name='student_achievement_link',
            field=models.CharField(max_length=b'128'),
        ),
    ]
