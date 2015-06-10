from django.db import models

class ratings (models.Model):
    people = models.ForeignKey('People')
    comment = models.ForeignKey('comment')
    like = models.CharField(max_length=10)
    rate = models.IntegerField()
    def __unicode__(self):
        return self.id

class course (models.Model):
    course_name = models.CharField(max_length=45)
    courseDesc = models.CharField(max_length=100)
    courseFee = models.IntegerField()
    createdTS = models.DateTimeField(auto_now_add= True)
    course_id = models.IntegerField(primary_key=True, unique=True)
    hideBit = models.IntegerField(max_length=1, default=0)
    def __unicode__(self):
        return self.course_name

class lesson (models.Model):
    lesson_name = models.CharField(max_length=45)
    lessonDesc = models.CharField(max_length=100)
    lessonPre = models.CharField(max_length=100)
    createdTS = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(course)
    hideBit = models.IntegerField(max_length=1, default=0)
    def __unicode__(self):
        return self.lesson_name

class People (models.Model):
    role = models.CharField(max_length=20)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=75, unique=True)
    phone_number = models.IntegerField()
    hideBit = models.IntegerField(max_length=1, default=0)
    isActive = models.IntegerField(max_length=1, default=0)
    def __unicode__(self):
        return self.first_name

class PeopleCourse(models.Model):
    peopleId = models.ForeignKey(People)
    course = models.ForeignKey(course)
    def __unicode__(self):
        return self.id

class reccommendedList(models.Model):
    student = models.ForeignKey(People)
    recommendedClass = models.ForeignKey(course)
    def __unicode__(self):
        return self.recommendedClass

class wishList(models.Model):
    student = models.ForeignKey(People)
    wishListClass = models.ForeignKey(course)
    def __unicode__(self):
        return self.recommendedClass

class comment (models.Model):
    parentId = models.ForeignKey('self', null=True)
    course = models.ForeignKey(course, null=True)
    lesson = models.ForeignKey(lesson, null=True)
    comment_text = models.CharField(max_length = 100, default='default')
    hideBit = models.IntegerField(max_length=1, default=0)
    def __unicode__(self):
        return self.id



