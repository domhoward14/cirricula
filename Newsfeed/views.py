from django.shortcuts import render
from django.http import HttpResponse
from Newsfeed.forms import *
from Newsfeed.models import *

def index(request):
    return render(request, 'Login.html')

def homePage(request):
    return render(request, 'homePage.html')

def addNewUser(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return homePage(request)

        else:
            print form.errors
    else:
        form = NewUserForm()

    return render(request, 'userRegistration.html', {'form': form})

def makeRecomendations(request):
    if request.method == 'POST':
        form = recommendedClasses(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return homePage(request)

        else:
            print form.errors
    else:
        form = recommendedClasses()

    return render(request, 'recommendCourse.html', {'form':form})

def student(request):
    courses = course.objects.all()
    people = People.objects.filter(role="Professor")
    context_dict = {'courses':courses, 'people':people}
    return render(request, 'studentPage.html', context_dict)

def professor(request):
    #Courses = PeopleCourse.objects.filter(peopleId.first_name="Bill")
    #context_dict = {'Courses':Courses}
    return render(request, 'professorsPage.html')

def admin(request):
    return render(request, 'adminPage.html')
