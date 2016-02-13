from django.conf.urls import url,patterns,include
from connect.views import *
from connect import views

urlpatterns = (
    url(r'^$', views.dashboard, name='dashboard'),

    # Student profile url's
    url(r'^sp/profile/$', views.update, name='update'),
    url(r'^sp/dashboard/$', views.dashboard, name='dashboard'),
    url(r'^sp/report/$', views.report, name='report'),
    url(r'^sp/publishwork/$', views.publishwork, name='publishwork'),
    url(r'^sp/submittask/$', views.submittask, name='submittask'),
    url(r'^sp/notesinfo/$', views.notesinfo, name='notesinfo'),
    url(r'^sp/infopediainfo/$', views.infopediainfo, name='infopediainfo'),
    url(r'^sp/professorinfo/$', views.professorinfo, name='professorinfo'),
    url(r'^sp/collegeinfo/$', views.collegeinfo, name='collegeinfo'),
    url(r'^sp/thread/$', views.thread, name='thread'),
    url(r'^sp/update/$', views.update, name='update'),
    url(r'^sp/achievements/$', views.achievements, name='achievements'),
    url(r'^sp/academics/$', views.academics, name='academics'),
    url(r'^sp/certificate/$', views.certificate, name='certificate'),
    url(r'^sp/skills/$', views.skills, name='skills'),
    url(r'^sp/projects/$', views.projects, name='projects'),

    # Mentor View
    url(r'^mp/mdashboard/$', views.mdashboard, name='mdashboard'),
    url(r'^mp/mpublishnotes/$', views.mpublishnotes, name='mpublishnotes'),
    url(r'^mp/mmentorstudents/$', views.mmentorstudents, name='mmentorstudents'),
    url(r'^mp/mreport/$', views.mreport, name='mreport'),
    url(r'^mp/massignments/$', views.massignments, name='massignments'),
    url(r'^mp/mprofile/$', views.mprofile, name='mprofile'),
    url(r'^mp/mexperience/$', views.mexperience, name='mexperience'),
    url(r'^mp/machievements/$', views.machievements, name='machievements'),
    url(r'^mp/mcertification/$', views.mcertification, name='mcertification'),
)