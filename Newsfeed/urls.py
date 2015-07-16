from django.conf.urls import patterns, url
from Newsfeed import views

urlpatterns = patterns\
    ('',
        url(r'^$', views.index, name = 'index'),
        url(r'^userRegistration.html/', views.addNewUser, name='addUser'),
        url(r'^studentPage.html/', views.student, name = 'studentPage'),
        url(r'^professorsPage.html/', views.professor, name = 'professor'),
        url(r'^adminPage.html/', views.admin, name = 'admin'),
        url(r'^recommendCourse.html/', views.makeRecomendations, name ='recommendations'),
        url(r'^viewAllClasses.html', views.allClasses, name ='viewAllClasses'),
        url(r'^viewMembers.html', views.allMembers, name = 'veiwAllMembers'),
        url(r'^success.html', views.success, name = 'success'),
        url(r'^homePage.html', views.homePage, name = 'Homepage'),
        url(r'^recommendLesson.html', views.recLesson, name = 'receccomendLessons'),
    )

