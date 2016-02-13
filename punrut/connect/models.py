from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.text import slugify
# from faculty.models import *


class Activities(models.Model):
	activity_id=models.IntegerField()
	# task_name=models.ForeignKey(Assign_task)
	date=models.TextField()
	# assign_task_id=models.ForeignKey(Assign_task)

class Students(models.Model):
	student_id = models.IntegerField()
	student_name = models.TextField()


class Student_profile_update(models.Model):
	student_profile_pic=models.FileField(upload_to='')
	student_name=models.CharField(max_length='128')
	student_email_address=models.CharField(max_length='128')
	student_password=models.CharField(max_length='128')
	student_phone=models.CharField(max_length='128')
	student_date_of_birth=models.CharField(max_length='128')

class Student_skills(models.Model):
	skill_name=models.CharField(max_length='128')

class Student_certifications(models.Model):
	student_certification_name=models.CharField(max_length='128')
	student_certification_authority=models.CharField(max_length='128')
	student_certification_license_number=models.CharField(max_length='128')
	student_certification_URL= models.CharField(max_length='128')
	# student_certification_date=models.CharField(max_length='128')
	# student_certification_does_not_expire=

class Student_achievements(models.Model):
	student_achievement_title=models.CharField(max_length='128')
	student_achievement_description=models.CharField(max_length='128')
	student_achievement_link= models.CharField(max_length='128')
	student_achievement_file=models.FileField(upload_to='')

class Student_projects(models.Model):	
	student_project_name=models.CharField(max_length='255')
	student_project_start_year_date=models.CharField(max_length='255')
	student_project_end_year_date=models.CharField(max_length='255')
	student_project_URL=models.CharField(max_length='255')
	student_project_description=models.CharField(max_length='255')
	# student_project_team_members=

# class Student_academics(models.Models):
# 	student_academics_school=models.TextField()	

class News_feed(models.Model):
	news_feed_id=models.IntegerField()
	feed=models.CharField(max_length='255')
	# time=models.TextField()

class Work_publish(models.Model):
	work_id=models.IntegerField()
	work_name=models.CharField(max_length='255')
	work_desc=models.CharField(max_length='255')
	work_sub=models.CharField(max_length='255')
	# work_file=models.FileField(upload_to='')

# class Student_post(models.Model):
# 	news=models.ForeignKey

# class Submit_task(models.Model):
	# student_id=models.ForeignKey(Students)
	# assign_task_id=models.ForeignKey(Assign_task)

class Materials(models.Model):
	m_id=models.IntegerField()
	subject=models.CharField(max_length='255')
	m_type_id=models.IntegerField()
	m_title=models.CharField(max_length='255')
	m_download_link=models.CharField(max_length='255')
	submitted_by=models.IntegerField()

class Material_type(models.Model):
	# m_type_id=models.ForeignKey(Materials)
	m_type_name=models.CharField(max_length='255')

class Connections(models.Model):
	# student1_id=models.ForeignKey(Students)
	# student2_id=models.ForeignKey(Students)
	# status_id=models.ForeignKey(Status)
	Requested_by_id=models.IntegerField(Students)

class Status(models.Model):
	status_id=models.IntegerField()
	status=models.CharField(max_length='255')

class Posts(models.Model):
	post_id=models.IntegerField()
	timestamp=models.CharField(max_length='255')
	post=models.CharField(max_length='255')
	# upload_img=models.FileField(upload_to='')
	# upload_video=models.FileField(upload_to='')
	posted_by_id=models.IntegerField()

class Comments(models.Model):
	comment_id=models.IntegerField()
	commented_by=models.IntegerField()
	comment=models.CharField(max_length='255')
	# post_id=models.ForeignKey(Posts)	

# class Stud_ment_connections(models.Model):
	# student1_id=models.ForeignKey(Students)
	# faculty_id=models.ForeignKey(Faculty)
	# status_id=models.ForeignKey(Status)