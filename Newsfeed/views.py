from django.shortcuts import render
from Newsfeed.forms import *
from Newsfeed.models import *
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'Login.html')

def homePage(request):
    return render(request, 'homePage.html')

def addNewUser(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return render(request, 'success.html/')

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
            return render(request, 'success.html/')

        else:
            print form.errors
    else:
        form = recommendedClasses()

    return render(request, 'recommendCourse.html', {'form':form})

def recLesson(request):

    if request.method == 'POST':
        form = recommendedLessons(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return render(request, 'success.html')

        else:
            print form.errors
    else:
        form = recommendedLessons()
        return render(request, 'recommendLesson.html', {'form': form})






def student(request):
    courses = course.objects.order_by('-likes')
    courses = courses.filter(hideBit=0)
    courses = courses[:5]
    people = People.objects.filter(role="Professor")
    people = people[:5]
    lessons = lesson.objects.order_by('-likes')
    lessons = lessons[:5]
    context_dict = {'courses':courses, 'people':people, 'lessons':lessons}
    return render(request, 'studentPage.html', context_dict)

def professor(request):
    #Courses = PeopleCourse.objects.filter(peopleId.first_name="Bill")
    #context_dict = {'Courses':Courses}
    return render(request, 'professorsPage.html')

def admin(request):
    courses = course.objects.filter(hideBit = 1)
    lessons = lesson.objects.filter(hideBit = 1)
    context_dict = {'courses':courses, 'lessons':lessons}
    return render(request, 'adminPage.html', context_dict)

def allClasses(request):
    courses = course.objects.filter(hideBit = 0)
    context_dict = {'courses':courses}
    return render(request, 'viewAllClasses.html', context_dict)

def allMembers(request):
    students = People.objects.filter(role='Student')
    professors = People.objects.filter(role='Professor')
    context_dict = {'students':students, 'professors':professors}
    return render(request, 'viewMembers.html', context_dict)

def success(request):
    return render(request, 'success.html')




