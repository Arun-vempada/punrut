# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0006_auto_20160213_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_certifications',
            name='student_certification_date',
        ),
    ]
