# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0007_remove_student_certifications_student_certification_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_certifications',
            name='student_certification_date',
            field=models.CharField(default=0, max_length=b'128'),
            preserve_default=False,
        ),
    ]
