from django import forms
from connect.models import Student_skills
from connect.models import Student_profile_update
from connect.models import Student_certifications
from connect.models import Student_achievements
from django.contrib.auth.models import User


# Create your forms here.
class Student_profile_update_Form(forms.ModelForm):
	#uid=forms.CharField(label="Message: ",widget=forms.Textarea)
	student_profile_pic=forms.FileField()
	student_name=forms.CharField()
	student_email_address=forms.CharField()
	student_password=forms.CharField()
	student_phone=forms.CharField()
	# student_date_of_birth=forms.CharField()
	class Meta:
		model = Student_profile_update
		fields = ('student_name','student_email_address','student_password','student_phone','student_profile_pic',)

class Student_skills_Form(forms.ModelForm):
	#uid=forms.CharField(label="Message: ",widget=forms.Textarea)
	skill_name=forms.CharField()
	class Meta:
		model=Student_skills
		fields=('skill_name',)


class Student_certifications_Form(forms.ModelForm):
	#uid=forms.CharField(label="Message: ",widget=forms.Textarea)
	student_certification_name=forms.CharField()
	student_certification_authority=forms.CharField()
	student_certification_license_number=forms.CharField()
	student_certification_URL= forms.CharField()
	# student_certification_date=forms.CharField()
	class Meta:
		model = Student_certifications
		fields = ('student_certification_name','student_certification_authority','student_certification_license_number','student_certification_URL',)


class Student_achievements_Form(forms.ModelForm):
	#uid=forms.CharField(label="Message: ",widget=forms.Textarea)
	student_achievement_title=forms.CharField()
	student_achievement_description=forms.CharField()
	student_achievement_link= forms.CharField()
	student_achievement_file=forms.FileField()
	class Meta:
		model=Student_achievements
		fields=('student_achievement_title','student_achievement_description','student_achievement_link','student_achievement_file',)

