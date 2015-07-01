__author__ = 'domhoward14'
from Newsfeed.models import People, course, lesson, comment, PeopleCourse, ratings

def newUser(role, firstName, lastName, email, number):
    user = People.objects.get_or_create(role=role, first_name=firstName, last_name=lastName, phone_number=number, email=email)
    return user
    user.save()

def delUser(email):
    student = People.objects.get(email=email)
    student.hideBit = 1
    return student
    student.save()

def approvePeople(email):
    student = People.objects.get(email=email)
    student.isActive = 1
    return student
    student.save()

def addCourse(courseName, courseDesc, courseFee, courseId):
    Course = course.objects.get_or_create(course_name=courseName, courseDesc=courseDesc, courseFee=courseFee, course_id=courseId)[0]
    Course.hideBit = 0
    Course.save()

def delCourse(courseId):
    Course = course.objects.get_or_create(courseId=courseId)
    Course.hideBit = 1
    Course.save()


def addSuggestedCourse(courseName, courseDesc, courseFee, createdTS, courseId ):
    Course = course.objects.get_or_create(couresName=courseName, courseDesc=courseDesc, courseFee=courseFee, createdTS=createdTS, courseId=courseId, hideBit = 1)
    Course.save()





