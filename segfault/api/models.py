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

    class Meta:
        db_table = 'PROFESSORS'


class Course(models.Model):
    course = models.AutoField(
        primary_key=True, editable=False, db_column='course_id')
    name = models.CharField(max_length=50, null=False)
    students = models.ManyToManyField(
        Student, related_name='courses', through='Student_to_Course')
    professors = models.ManyToManyField(
        Professor, related_name='courses', through='Professor_to_Course')

    class Meta:
        db_table = 'COURSES'
        ordering = ['name']


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
        db_table = 'PROFESSOR_TO_COURSE'


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


class Scenario(models.Model):

    SCENARIO = models.AutoField(primary_key=True, editable=False)
    VERSION = models.IntegerField(default=1, editable=False)
    name = models.CharField(max_length=50, null=False)
    public = models.BooleanField(default=False)
    NUM_CONVERSATION = models.IntegerField(default=0)
    IS_FINISHED = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'SCENARIOS'
        ordering = ['date_created', 'name']


class Scenarios_for(models.Model):

    SCENARIO = models.ForeignKey('Scenario', on_delete=models.CASCADE,)
    COURSE = models.ForeignKey('course', on_delete=models.CASCADE)
    VERSION = models.IntegerField(default=1, editable=False)

    class Meta:
        # not sure about this
        unique_together = (('SCENARIO'), ('COURSE'))
        db_table = 'SCENARIO_FOR'


class Response(models.Model):
    student = models.ForeignKey('student', on_delete=models.CASCADE)
    scenario = models.ForeignKey('scenario', on_delete=models.CASCADE)
    version = models.IntegerField(default=1, editable=False)
    page = models.ForeignKey('pages', on_delete=models.CASCADE)
    course = models.ForeignKey('course', on_delete=models.CASCADE)
    date_taken = models.DateField(auto_now_add=True)
    choice = models.CharField(max_length=300)

    # TODO: Verify page in scenario

    class Meta:
        db_table = 'RESPONSES'
        ordering = ['scenario', 'page', 'student']


class Issue(models.Model):
    issue = models.AutoField(default=None, primary_key=True, editable=False)
    scenario = models.ForeignKey('Scenario', on_delete=models.CASCADE)
    version = models.IntegerField(default=1, editable=False)
    name = models.CharField(max_length=100)
    importance_score = models.FloatField(validators=[MinValueValidator(0.0)])

    class Meta:
        db_table = 'ISSUES'


class Conversations(models.Model):
    CONVERSATION = models.AutoField(primary_key=True, editable=False)
    STAKEHOLDER = models.ForeignKey(
        'Stakeholders', on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    response = models.TextField(max_length=100)

    class Meta:
        db_table = 'CONVERSATIONS'


class Stakeholders(models.Model):
    STAKEHOLDER = models.AutoField(primary_key=True, editable=False)
    SCENARIO = models.ForeignKey('Scenario',
                                 on_delete=models.CASCADE, null=False)
    VERSION = models.IntegerField(default=1, editable=False)
    NAME = models.CharField(max_length=1000,  null=False)
    DESCRIPTION = models.TextField(default="")
    JOB = models.TextField(default="default")
    INTRODUCTION = models.TextField(default='default')

    class Meta:
        db_table = 'STAKEHOLDERS'


class pages(models.Model):
    class Meta:
        unique_together = ['PAGE', 'SCENARIO', 'VERSION']
        db_table = 'pages'
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
    SCENARIO = models.ForeignKey('scenario', on_delete=models.CASCADE)
    VERSION = models.IntegerField(default=1, editable=False)
    BODY = models.TextField()
    NEXT_PAGE = models.IntegerField(null=True)
    X_COORDINATE = models.IntegerField()
    Y_COORDINATE = models.IntegerField()


class reflection_questions(models.Model):
    class Meta:
        unique_together = ['PAGE', 'REFLECTION_QUESTION']
        db_table = 'reflection_questions'
    PAGE = models.ForeignKey('pages', on_delete=models.CASCADE)
    REFLECTION_QUESTION = models.TextField()
    id = models.AutoField(primary_key=True, editable=False)


class generic_page(models.Model):
    class Meta:
        unique_together = ['PAGE', 'BODY']
        db_table = 'generic_page'
    PAGE = models.ForeignKey('pages', on_delete=models.CASCADE)
    BODY = models.TextField()
    id = models.AutoField(primary_key=True, editable=False)


class stakeholder_page(models.Model):
    class Meta:
        unique_together = ['PAGE', 'STAKEHOLDER']
        db_table = 'stakeholder_page'
    PAGE = models.ForeignKey('pages', on_delete=models.CASCADE)
    STAKEHOLDER = models.ForeignKey('stakeholders', on_delete=models.CASCADE)


class action_page(models.Model):
    class Meta:
        unique_together = ['PAGE', 'CHOICE']
        db_table = 'action_page'
    PAGE = models.ForeignKey('pages', on_delete=models.CASCADE)
    CHOICE = models.TextField()
    RESULT_PAGE = models.IntegerField(null=True)
    id = models.AutoField(primary_key=True, editable=False)

# response, reflections taken, response_to_action_page, conversations had, student times


class reflections_taken(models.Model):
    REFLECTIONS = models.TextField(max_length=100)
    STUDENT = models.ForeignKey('student', on_delete=models.CASCADE)
    COURSE = models.ForeignKey('course', on_delete=models.CASCADE)
    SCENARIO = models.ForeignKey('scenario', on_delete=models.CASCADE)
    VERSION = models.IntegerField(default=1, editable=False)
    DATE_TAKEN = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'reflections_taken'
        unique_together = ['SCENARIO', 'VERSION', 'COURSE', 'STUDENT']


class response_to_action_page(models.Model):
    RESPONSE = models.ForeignKey('response', on_delete=models.CASCADE)
    ACTION_PAGE = models.ForeignKey('action_page', on_delete=models.CASCADE)

    class Meta:
        db_table = 'response_to_action_page'
        unique_together = ['RESPONSE', 'ACTION_PAGE']


class conversations_had(models.Model):
    STUDENT = models.ForeignKey('student', on_delete=models.CASCADE)
    COURSE = models.ForeignKey('course', on_delete=models.CASCADE)
    SCENARIO = models.ForeignKey('scenario', on_delete=models.CASCADE)
    VERSION = models.IntegerField(default=1, editable=False)
    DATE_TAKEN = models.DateField(auto_now_add=True)
    STAKEHOLDER = models.ForeignKey('stakeholders', on_delete=models.CASCADE)
    SCORE = models.DecimalField(max_digits=5, decimal_places=2)
    CONVERSATION = models.ForeignKey('conversations', on_delete=models.CASCADE)

    class Meta:
        db_table = 'conversations_had'


class student_times(models.Model):
    STUDENT = models.ForeignKey('student', on_delete=models.CASCADE)
    COURSE = models.ForeignKey('course', on_delete=models.CASCADE)
    SCENARIO = models.ForeignKey('scenario', on_delete=models.CASCADE)
    VERSION = models.IntegerField(default=1, editable=False)
    DATE_TAKEN = models.DateField(auto_now_add=True)
    PAGE = models.ForeignKey('pages', on_delete=models.CASCADE)
    START_TIME = models.DateField(null=True)
    END_TIME = models.DateField(null=True)

    class Meta:
        db_table = 'student_times'
        unique_together = ['STUDENT', 'SCENARIO', 'VERSION', 'PAGE']


class Coverage(models.Model):

    STAKEHOLDER = models.ForeignKey(
        'Stakeholders', on_delete=models.CASCADE, related_name="coverage2", default=None)
    ISSUE = models.ForeignKey(
        'Issues', on_delete=models.CASCADE, related_name="coverage1", default=None)
    COVERAGE_SCORE = models.FloatField(validators=[MinValueValidator(0.0)])

    class Meta:
        unique_together = (('STAKEHOLDER'), ('ISSUE'))
        db_table = 'COVERAGE'
