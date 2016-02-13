# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import connect.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activities',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activity_id', models.IntegerField()),
                ('date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment_id', models.IntegerField()),
                ('commented_by', models.IntegerField()),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Connections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Requested_by_id', models.IntegerField(verbose_name=connect.models.Students)),
            ],
        ),
        migrations.CreateModel(
            name='Material_type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('m_type_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Materials',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('m_id', models.IntegerField()),
                ('subject', models.TextField()),
                ('m_type_id', models.IntegerField()),
                ('m_title', models.TextField()),
                ('m_download_link', models.TextField()),
                ('submitted_by', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='News_feed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_feed_id', models.IntegerField()),
                ('feed', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post_id', models.IntegerField()),
                ('timestamp', models.TextField()),
                ('post', models.TextField()),
                ('posted_by_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_id', models.IntegerField()),
                ('status', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_achievements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_achievement_title', models.TextField()),
                ('student_achievement_description', models.TextField()),
                ('student_achievement_link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_certifications',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_certification_name', models.TextField()),
                ('student_certification_authority', models.TextField()),
                ('student_certification_license_number', models.TextField()),
                ('student_certification_URL', models.TextField()),
                ('student_certification_date', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_profile_update',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_name', models.TextField()),
                ('student_email_address', models.TextField()),
                ('student_password', models.TextField()),
                ('student_phone', models.IntegerField()),
                ('student_date_of_birth', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_projects',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_project_name', models.TextField()),
                ('student_project_start_year_date', models.TextField()),
                ('student_project_end_year_date', models.TextField()),
                ('student_project_URL', models.TextField()),
                ('student_project_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student_skills',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('skill_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_id', models.IntegerField()),
                ('student_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Work_publish',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_id', models.IntegerField()),
                ('work_name', models.TextField()),
                ('work_desc', models.TextField()),
                ('work_sub', models.TextField()),
            ],
        ),
    ]
