from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from connect.models import Student_skills
from connect.models import Student_profile_update
from connect.models import Student_certifications
from connect.models import Student_achievements
from connect.forms import Student_profile_update_Form
from connect.forms import Student_skills_Form
from connect.forms import Student_certifications_Form
from connect.forms import Student_achievements_Form

from django.contrib.auth.models import User

import sys

# Create your views here.

#  Student views
def dashboard(request):    
    return render(request, 'student/sp/dashboard.html', {})
def report(request):    
    return render(request, 'student/sp/report.html', {})
def publishwork(request):    
    return render(request, 'student/sp/publishwork.html', {})
def submittask(request):    
    return render(request, 'student/sp/submittask.html', {})
def notesinfo(request):    
    return render(request, 'student/sp/notesinfo.html', {})
def infopediainfo(request):    
    return render(request, 'student/sp/infopediainfo.html', {})
def professorinfo(request):    
    return render(request, 'student/sp/professorinfo.html', {})
def collegeinfo(request):    
    return render(request, 'student/sp/collegeinfo.html', {})
def thread(request):    
    return render(request, 'student/sp/thread.html', {})
def update(request):
    context = RequestContext(request)
    if request.method == "POST":
        student_profile = Student_profile_update_Form(request.POST,request.FILES)
        if student_profile.is_valid():
            student_profile.save()
            return HttpResponse("file saved")
        else:
            print  student_profile 
    else:
         student_profile = Student_profile_update_Form()
    return render_to_response('student/sp/update.html',{},context)            

def achievements(request):    
    context = RequestContext(request)
    if request.method == "POST":
        achievement = Student_achievements_Form(request.POST,request.FILES)
        if achievement.is_valid():
            achievement = achievement.save()
            # return HttpResponse("file saved")
        else:
            print achievement
    else:
        achievement = Student_achievements_Form()
    return render_to_response('student/sp/achievements.html',{},context)      


def academics(request):    
    return render(request, 'student/sp/academics.html', {})

def certificate(request):
    context = RequestContext(request)
    if request.method == "POST":
        certification = Student_certifications_Form(data = request.POST)
        if certification.is_valid():
            certification = certification.save()
            # return HttpResponse("file saved")
        else:
            print certification
    else:
        certification = Student_certifications_Form()
    return render_to_response('student/sp/certificate.html',{},context)       



def skills(request):
    context = RequestContext(request)
    if request.method == "POST":
        skill_name = Student_skills_Form(data = request.POST)
        if skill_name.is_valid():
            skill_name = skill_name.save()
            # return HttpResponse("file saved")
        else:
            print skill_name
    else:
        skill_name = Student_skills_Form()
    return render_to_response('student/sp/skills.html',{},context)        
    
def projects(request):    
    return render(request, 'student/sp/projects.html', {})

#   Mentor views
def mdashboard(request):    
    return render(request, 'mentor/mp/mdashboard.html', {})
def mpublishnotes(request):    
    return render(request, 'mentor/mp/mpublishnotes.html', {})
def mmentorstudents(request):    
    return render(request, 'mentor/mp/mmentorstudents.html', {})
def mreport(request):    
    return render(request, 'mentor/mp/mreport.html', {})
def massignments(request):    
    return render(request, 'mentor/mp/massignments.html', {})
def mprofile(request):    
    return render(request, 'mentor/mp/mprofile.html', {})
def mexperience(request):    
    return render(request, 'mentor/mp/mexperience.html', {})
def machievements(request):    
    return render(request, 'mentor/mp/machievements.html', {})
def mcertification(request):    
    return render(request, 'mentor/mp/mcertification.html', {})