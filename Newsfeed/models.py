from django.db import models

class admin_login (models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)
    def __unicode__(self):
        return self.username

#This is a relational table for lesson and course
class comment (models.Model):
    #make relation to course id
    models.ForeignKey(course)
    #make relation to lesson id
    models.ForeignKey(lesson)
    #make relation to people id
    models.ForeignKey(People)
#parent_id identifies what comment it came from.
    parent_id = models.IntegerField()
    comment_text = models.CharField(max_length = 100)
    status = models.CharField(max_length = 10)
    def __unicode__(self):
        return self.id

class newsfeed (models.Model):
    #relation to commentid
    #relation to peopleid
    like = models.CharField(max_length=10)
    rate = models.IntegerField()
    def __unicode__(self):
        return self.id

#this is a relationship table
class PeopleCourse(models.Model):
    #foreign key to people_id
    peopleId = models.ForeignKey(People)
    #foreign key to course_id
    foreignKey = models.ForeignKey(course)
    recommended = models.CharField(max_length=10)
    my_Wish_list = models.CharField(max_length=10)
    def __unicode__(self):
        self.id

#This may need to be created in the authentication page
class People (models.Model):
    role = models.CharField(max_length=20)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=25)
    #password cannot be stored in plain text
    phone_number = models.IntegerField()
    peopleCourse = models.ManyToManyField(course, through=PeopleCourse)
    def __unicode__(self):
        self.first_name

class course (models.Model):
    course_name = models.CharField(max_length=45)
    courseDesc = models.CharField(max_length=100)
    courseFee = models.IntegerField()
    createdTS = models.DateTimeField(auto_now_add= True)
    course_id = models.IntegerField()
    def __unicode__(self):
        self.course_name

class lesson (models.Model):
    #relation to course id
    lesson_name = models.CharField(max_length=45)
    lessonDesc = models.CharField(max_length=100)
    lessonPre = models.CharField(max_length=100)
    createdTS = models.DateTimeField(auto_now_add=True)
    course_id = models.IntegerField()
    def __unicode__(self):
        self.lesson_name



