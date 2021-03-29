import django
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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
 
class Scenario(models.Model):

    scenario_id = models.AutoField(primary_key=True, editable=False)
    scenario = models.IntegerField(default=1, editable=True)
    version = models.IntegerField(default=1, editable=True)
    name = models.CharField(max_length=50, null=False)
    public = models.BooleanField(default=False)
    NUM_CONVERSATION = models.IntegerField(default=0)
    IS_FINISHED = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'SCENARIOS'
        ordering = ['date_created', 'name']
        unique_together = ('scenario','version')


class Student(models.Model):
    student = models.AutoField(
        primary_key=True, editable=False, db_column='student')
    first_name = models.CharField(max_length=50, null=False, db_column='fname')
    last_name = models.CharField(max_length=50, null=False, db_column='lname')

    class Meta:
        db_table = 'STUDENTS'


class Professor(models.Model):
    professor = models.AutoField(
        primary_key=True, editable=False, db_column='professor')
    first_name = models.CharField(max_length=50, null=False, db_column='fname')
    last_name = models.CharField(max_length=50, null=False, db_column='lname')
    scenarios = models.ManyToManyField(
        Scenario, related_name='professor',  through='Professors_to_scenario')

    class Meta:
        db_table = 'PROFESSORS'

class Professors_to_scenario(models.Model):
    professor = models.ForeignKey(
        Professor, on_delete = models.CASCADE)
    scenario = models.ForeignKey(
        Scenario, on_delete=models.CASCADE,)
    permission = models.IntegerField(default = 1)


class Course(models.Model):
    course = models.AutoField(
        primary_key=True, editable=False, db_column='course')
    name = models.CharField(max_length=50, null=False)
    students = models.ManyToManyField(
        Student, related_name='courses', through='Student_to_Course')
    professors = models.ManyToManyField(
        Professor, related_name='courses', through='Professor_to_Course')
    scenarios = models.ManyToManyField(
        Scenario, related_name='courses',  through='Scenario_to_Course')

    class Meta:
        db_table = 'COURSES'


class Student_to_Course(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, db_column='student')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('student', 'course')
        db_table = 'STUDENT_TO_COURSE'


class Professor_to_Course(models.Model):
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, db_column='professor')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('professor', 'course')
        db_table = 'PROFESSORS_TO_COURSES'


class Demographic(models.Model):
    student = models.OneToOneField(
        Student, primary_key=True, on_delete=models.CASCADE, related_name="demographics", null=False, db_column='student')
    # TODO: May Use Birthday
    age = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(0)], db_column='age')
    grade_choices = (('0', 'Other'),
                     ('1', 'Freshmen'),
                     ('2', 'Sophomore'),
                     ('3', 'Junior'),
                     ('4', 'Senior'))
    grade = models.CharField(
        max_length=1, choices=grade_choices, db_column='grade')
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('OT', 'Other'),
    )
    gender = models.CharField(
        max_length=2, choices=gender_choices, db_column='gender')
    race = models.CharField(max_length=30, db_column='race')
    major = models.CharField(max_length=30, db_column='major')

    class Meta:
        db_table = 'DEMOGRAPHICS'



class Scenario_to_Course(models.Model):

    scenario = models.ForeignKey(
        Scenario, on_delete=models.CASCADE,)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('scenario', 'course')
        db_table = 'SCENARIO_FOR'

        
class Pages(models.Model):
    PAGE = models.AutoField(primary_key=True, editable=False)
    PAGE_CHOICES = (
        ('I', 'INTRO'),
        ('G', 'GENERIC'),
        ('R', 'REFLECTION'),
        ('S', 'STAKEHOLDER'),
        ('A', 'ACTION'),
    )
    PAGE_TYPE = models.CharField(max_length=2, choices=PAGE_CHOICES)
    PAGE_TITLE = models.CharField(max_length=1000)
    SCENARIO = models.ForeignKey(
        Scenario, on_delete=models.CASCADE)
    BODY = models.TextField()
    NEXT_PAGE = models.IntegerField(null=True)
    X_COORDINATE = models.IntegerField()
    Y_COORDINATE = models.IntegerField()

    class Meta:
        db_table = 'pages'

class Response(models.Model):
    response_id = models.AutoField(primary_key=True, editable=False)
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)
    scenario = models.ForeignKey(
        Scenario, on_delete=models.CASCADE)
    page = models.ForeignKey(
        Pages, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)
    date_taken = models.DateField(auto_now_add=True)
    choice = models.CharField(max_length=300)

    # TODO: Verify page in scenario

    class Meta:
        db_table = 'RESPONSES'
        ordering = ['scenario', 'page', 'student']
        unique_together = ('scenario','page','student','course')


class Issue(models.Model):
    issue = models.AutoField(default=None, primary_key=True, editable=False)
    scenario = models.ForeignKey(
        Scenario, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    importance_score = models.FloatField(validators=[MinValueValidator(0.0)])

    class Meta:
        db_table = 'ISSUES'

        
class Stakeholders(models.Model):
    stakeholder = models.AutoField(primary_key=True, editable=False)
    scenario = models.ForeignKey(
        Scenario, on_delete=models.CASCADE, null=False)
    version = models.IntegerField(default=1, editable=False)
    name = models.CharField(max_length=1000,  null=False)
    description = models.TextField(default="")
    job = models.TextField(default="default")
    introduction = models.TextField(default='default')

    class Meta:
        db_table = 'STAKEHOLDERS'
        

class Conversations(models.Model):
    conversation = models.AutoField(primary_key=True, editable=False)
    stakeholder = models.ForeignKey(
        Stakeholders, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    response = models.TextField(max_length=100)

    class Meta:
        db_table = 'CONVERSATIONS'


class Reflection_questions(models.Model):
    PAGE = models.ForeignKey(
        Pages, on_delete=models.CASCADE)
    REFLECTION_QUESTION = models.TextField()
    class Meta:
        unique_together = ['PAGE', 'REFLECTION_QUESTION']
        db_table = 'reflection_questions'


class Generic_page(models.Model):
    
    PAGE = models.ForeignKey(
        Pages, on_delete=models.CASCADE)
    BODY = models.TextField()
    
    class Meta:
        unique_together = ['PAGE', 'BODY']
        db_table = 'generic_page'


class Stakeholder_to_page(models.Model):
    class Meta:
        unique_together = ['PAGE', 'STAKEHOLDER']
        db_table = 'stakeholder_to_page'
    PAGE = models.ForeignKey(
        Pages, on_delete=models.CASCADE)
    STAKEHOLDER = models.ForeignKey(
        Stakeholders, on_delete=models.CASCADE)


class Action_page(models.Model):
    class Meta:
        unique_together = ['PAGE', 'CHOICE']
        db_table = 'action_page'
    PAGE = models.ForeignKey(
        Pages, on_delete=models.CASCADE)
    CHOICE = models.TextField()
    RESULT_PAGE = models.IntegerField(null=True)

class Reflections_taken(models.Model):
    REFLECTIONS = models.TextField(max_length=100)
    RESPONSE_ID = models.ForeignKey(
        Response, on_delete = models.CASCADE)

    class Meta:
        db_table = 'reflections_taken'


class Response_to_action_page(models.Model):
    RESPONSE = models.ForeignKey(
        Response, on_delete=models.CASCADE)
    ACTION_PAGE = models.ForeignKey(
        Action_page, on_delete=models.CASCADE)

    class Meta:
        db_table = 'response_to_action_page'
        unique_together = ['RESPONSE', 'ACTION_PAGE']


class Responses_to_conversations(models.Model):
    RESPONSE = models.ForeignKey(
        Response, on_delete = models.CASCADE)
    STAKEHOLDER = models.ForeignKey(
        Stakeholders, on_delete=models.CASCADE)
    SCORE = models.DecimalField(max_digits=5, decimal_places=2)
    CONVERSATION = models.ForeignKey(
        Conversations, on_delete=models.CASCADE)

    class Meta:
        db_table = 'responses_to_conversations'


class Student_times(models.Model):
    STUDENT = models.ForeignKey(
        Student, on_delete=models.CASCADE)
    COURSE = models.ForeignKey(
        Course, on_delete=models.CASCADE)
    SCENARIO = models.ForeignKey(
        Scenario, on_delete=models.CASCADE)
    DATE_TAKEN = models.DateField(auto_now_add=True)
    PAGE = models.ForeignKey(
        Pages, on_delete=models.CASCADE)
    START_TIME = models.DateField(auto_now_add = True)
    END_TIME = models.DateField(null=True)

    class Meta:
        db_table = 'student_times'
        unique_together = ['STUDENT', 'SCENARIO', 'COURSE', 'PAGE']


class Coverage(models.Model):

    STAKEHOLDER = models.ForeignKey(
        Stakeholders, on_delete=models.CASCADE,  default=None)
    ISSUE = models.ForeignKey(
        Issue, on_delete=models.CASCADE, default=None)
    COVERAGE_SCORE = models.FloatField(validators=[MinValueValidator(0.0)])

    class Meta:
        unique_together = (('STAKEHOLDER'), ('ISSUE'))
        db_table = 'COVERAGE'

class Student_page_progress(models.Model):
    STUDENT = models.ForeignKey(
        Student, on_delete=models.CASCADE, default = None)
    PAGE = models.ForeignKey(
        Pages, on_delete = models.CASCADE, default = None)
    COMPLETED = models.BooleanField(default = False);

    class Meta:
        unique_together = ('STUDENT',"PAGE")
