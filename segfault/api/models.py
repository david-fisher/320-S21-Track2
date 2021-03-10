from django.db import models
import django
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

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

class Course(models.Model):
    name = models.CharField(max_length=50, null=False)
    fullName = models.CharField(max_length=50)
    semester = models.CharField(max_length=10, null=False)

    class Meta:
        db_table = 'COURSES'
        ordering = ['semester', 'name']
        unique_together = ['semester', 'name']


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



