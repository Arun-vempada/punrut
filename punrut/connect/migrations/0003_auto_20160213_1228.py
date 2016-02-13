# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0002_auto_20160212_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_profile_update',
            name='student_date_of_birth',
        ),
        migrations.AddField(
            model_name='student_profile_update',
            name='student_profile_pic',
            field=models.FileField(default=0, upload_to=b'C/Bitnami/djangostack-1.8.8-0/xtraFiles'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student_profile_update',
            name='student_email_address',
            field=models.CharField(max_length=b'128'),
        ),
        migrations.AlterField(
            model_name='student_profile_update',
            name='student_name',
            field=models.CharField(max_length=b'128'),
        ),
        migrations.AlterField(
            model_name='student_profile_update',
            name='student_password',
            field=models.CharField(max_length=b'128'),
        ),
    ]
