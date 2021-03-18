import django
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# All attributes are pending to be changed after SQL team giving their construction
# dont use default = none to prevent empty names

""" 
# Name "Webuser" to distinguish from auth.User, we might use that later
    class Webuser(User):
    takingClass = ArrayField(models.ForeignKey(Course, related_name='students',on_delete=models.CASCADE,))
    teachingClass  = ArrayField(models.ForeignKey(Course, related_name='instructors',on_delete=models.CASCADE,))
    class Meta:
        db_table = 'users'
 """

class Student(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'STUDENTS'

class Professor(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'PROFESSORS'


class Course(models.Model):
    name = models.CharField(max_length=50, null=False)
    students = models.ForeignKey(Student, on_delete = models.CASCADE, blank=True,null=True)

    class Meta:
        db_table = 'COURSES'
        ordering = ['name']
        #unique_together = ['name']


class Demographic(models.Model):
    student_id = models.OneToOneField(Student,primary_key=True, on_delete = models.CASCADE, related_name = "demographics")
    age = models.IntegerField()
    grade = models.CharField(max_length = 30) 
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('OT', 'OTHER'),
    )
    gender = models.CharField(max_length = 2, choices = GENDER_CHOICES)
    race = models.CharField(max_length = 30) 
    major = models.CharField(max_length = 30) 
    class Meta:
        db_table = 'DEMOGRAPHICS'




class Scenario(models.Model):
    
    SCENARIO = models.AutoField(primary_key = True, editable=False)
    VERSION = models.IntegerField(default=1, editable=False)
    name = models.CharField(max_length=50, null=False)
    public = models.BooleanField(default=False)    
    NUM_CONVERSATION = models.IntegerField(default = 0)
    IS_FINISHED = models.BooleanField(default = False)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'SCENARIOS'
        ordering = ['date_created','name']

class Scenarios_for(models.Model):
    #not sure about unique together
   
    SCENARIO = models.ForeignKey('Scenario', on_delete = models.CASCADE, related_name='scenarios_for1')
    COURSE = models.ForeignKey('courses', on_delete = models.CASCADE, related_name='scenarios_for2')
    VERSION = models.IntegerField(default=1, editable=False)

    class Meta:
        #not sure about this
        unique_together = (('SCENARIO'), ('COURSE'))
        db_table = 'SCENARIO_FOR'

class Response(models.Model):
    scenario = models.ForeignKey('Scenario', on_delete = models.CASCADE)
    #TODO: verify pages is in scenario

    # commented because of pages are not implemented
 #   page = models.ForeignKey('pages', on_delete = models.CASCADE)

    date_taken = models.DateField(auto_now_add=True)
    choice = models.CharField(max_length = 300)
    class Meta:
        db_table = 'RESPONSES'
        ordering = ['Scenarios']

class Issues(models.Model):
    ISSUE = models.AutoField(default = None, primary_key = True, editable = False)
    scenario = models.ForeignKey('Scenario', on_delete = models.CASCADE)
    VERSION = models.IntegerField(default=1, editable=False)
    name = models.CharField(max_length = 100)
    importance_score = models.FloatField(validators = [MinValueValidator(0.0)])
    class Meta:
       db_table = 'ISSUES'
       ordering = ['Scenario']

class Conversations(models.Model):
    CONVERSATION = models.AutoField(primary_key = True, editable = False)
    STAKEHOLDER = models.ForeignKey('Stakeholders', on_delete = models.CASCADE, related_name="conversations_had6")
    question = models.CharField(max_length = 100)
    response = models.TextField(max_length = 100)
    class Meta:
        db_table = 'CONVERSATIONS'


class Stakeholders(models.Model):
    STAKEHOLDER = models.AutoField(primary_key = True, editable = False)
    SCENARIO = models.ForeignKey('Scenario', to_field = 'SCENARIO', on_delete = models.CASCADE, related_name="stakeholders2", default = 1)
    VERSION = models.IntegerField(default=1, editable=False)
    NAME = models.CharField(max_length = 1000, default = "default")
    DESCRIPTION = models.TextField(default = "default")
    JOB = models.TextField(default = "default")
    INTRODUCTION = models.TextField(default = 'default')

    class Meta:
        db_table = 'STAKEHOLDERS'


class Coverage(models.Model):

    
    STAKEHOLDER = models.ForeignKey('Stakeholders', on_delete = models.CASCADE, related_name = "coverage2", default = None)
    ISSUE = models.ForeignKey('Issues', on_delete = models.CASCADE, related_name = "coverage1", default = None)
    COVERAGE_SCORE = models.FloatField(validators = [MinValueValidator(0.0)])

    class Meta:
        unique_together = (('STAKEHOLDER'),('ISSUE'))
        db_table = 'CONVERSATIONS'  
