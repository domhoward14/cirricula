__author__ = 'domhoward14'
from Newsfeed.models import People, course, lesson, comment, PeopleCourse, ratings

def newUser(role, firstName, lastName, email, number):
    People.objects.get_or_create(role=role, first_name=firstName, last_name=lastName, phone_number=number, email=email)

def delUser(email):
    student = People.objects.get(email=email)
    student.hideBit = 1

def approvePeople(email):
    student = People.objects.get(email=email)
    student.isActive = 1

def addCourse(courseName, courseDesc, courseFee, createdTS, courseId):
    course.objects.get_or_create(couresName=courseName, courseDesc=courseDesc, courseFee=courseFee, createdTS=createdTS, courseId=courseId)

def delCourse(courseId):
    Course = course.objects.get_or_create(courseId=courseId)
    Course.hideBit = 1

def addSuggestedCourse():
    course.objects.get_or_create(couresName=courseName, courseDesc=courseDesc, courseFee=courseFee, createdTS=createdTS, courseId=courseId, hideBit = 1)






