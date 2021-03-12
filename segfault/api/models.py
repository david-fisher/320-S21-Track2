import django
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


# All attributes are pending to be changed after SQL team giving their construction
# dont use default = none to prevent empty names


class Scenario(models.Model):
    name = models.CharField(max_length=50, null=False)
    status = models.TextChoices('status', 'Draft Published Closed')
    public = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=300)
    additional_data = models.CharField(max_length=300)


    class Meta:
        db_table = 'SCENARIOS'
        ordering = ['date_created','name']


# Name "Webuser" to distinguish from auth.User, we might use that later
class Webuser(User):
    """ 
    takingClass = ArrayField(models.ForeignKey(Course, related_name='students',on_delete=models.CASCADE,))
    teachingClass  = ArrayField(models.ForeignKey(Course, related_name='instructors',on_delete=models.CASCADE,))
    """  
    
    class Meta:
        db_table = 'users'
    

""" 
class Student(webuser):

    class Meta:
        db_table = 'users'

class Stakeholder(webuser):
    class Meta:
        db_table = 'users'

class Professor(webuser):
    class Meta:
        db_table = 'users'
 """



class Course(models.Model):
    name = models.CharField(max_length=50, null=False)
    fullName = models.CharField(max_length=50, default = '', null=True, blank = True)
    semester = models.CharField(max_length=10, null=False)
    #TODO: This is bullshit just for demo 
    students = models.ForeignKey(Webuser, on_delete = models.CASCADE, blank=True,null=True)
    scenarios = models.ManyToManyField("scenario",related_name="course",through="PartOf")
    class Meta:
        db_table = 'COURSES'
        ordering = ['semester', 'name']
        unique_together = ['semester', 'name']


#demo
class PartOf(models.Model):
    scenario = models.ForeignKey(Scenario, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    class Meta:
        unique_together = ('scenario', 'course')
        db_table = 'PARTOF'



#TODO:implement other choices
class Demographic(models.Model):
    #TODO: use Webuser for now
    student = models.OneToOneField(Webuser,primary_key=True, on_delete = models.CASCADE, related_name = "demographics")
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

#TODO: may be redundant 
class Response(models.Model):
    scenario = models.ForeignKey('scenario', on_delete = models.CASCADE)
    #TODO: verify pages is in scenario

    # commented because of pages are not implemented
 #   page = models.ForeignKey('pages', on_delete = models.CASCADE)

    date_taken = models.DateField(auto_now_add=True)
    choice = models.CharField(max_length = 300)
    class Meta:
        db_table = 'RESPONSES'
        ordering = ['scenario']

#TODO: may be redundant 
class Issue(models.Model):
    scenario = models.ForeignKey('scenario', on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    importance_score = models.FloatField(validators = [MinValueValidator(0.0)])
    class Meta:
       db_table = 'ISSUES'
       ordering = ['scenario']


#TODO: may be redundant 
class Conversation(models.Model):
    #TODO: use Webuser for now
    stakeholder = models.ForeignKey(Webuser, on_delete = models.CASCADE)
    question = models.CharField(max_length = 100)
    response = models.TextField(max_length = 100)
    class Meta:
        db_table = 'CONVERSATIONS'

