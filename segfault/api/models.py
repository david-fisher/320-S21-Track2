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
    num_conversation = models.IntegerField(default=0)
    is_finished = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'scenarios'
        unique_together = ('scenario', 'version')


class Student(models.Model):
    student = models.AutoField(
        primary_key=True, editable=False, db_column='student')
    first_name = models.CharField(max_length=50, null=False, db_column='fname')
    last_name = models.CharField(max_length=50, null=False, db_column='lname')

    class Meta:
        db_table = 'students'


class Professor(models.Model):
    professor = models.AutoField(
        primary_key=True, editable=False, db_column='professor')
    first_name = models.CharField(max_length=50, null=False, db_column='fname')
    last_name = models.CharField(max_length=50, null=False, db_column='lname')
    scenarios = models.ManyToManyField(
        Scenario, related_name='professor',  through='Professors_to_scenario')

    class Meta:
        db_table = 'professors'


class Professors_to_scenario(models.Model):
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE)
    scenario = models.ForeignKey(
        Scenario, on_delete=models.CASCADE,)
    permission = models.IntegerField(default=1)
    class Meta:
        unique_together = ('professor','scenario')


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
        db_table = 'courses'


class Student_to_Course(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, db_column='student')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('student', 'course')
        db_table = 'students_to_course'


class Professor_to_Course(models.Model):
    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, db_column='professor')
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('professor', 'course')
        db_table = 'professors_to_courses'


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
        db_table = 'demographics'


class Scenario_to_Course(models.Model):

    scenario = models.ForeignKey(
        Scenario, on_delete=models.CASCADE,)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('scenario', 'course')
        db_table = 'scenarios_for'

class Courses_to_Scenario(models.Model):

    scenario = models.ForeignKey(
        Scenario, on_delete=models.CASCADE,)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('scenario', 'course')
        db_table = 'courses_to_scenario'
        

class Pages(models.Model):
    page = models.AutoField(primary_key=True, editable=False)
    page_choices = (
        ('I', 'INTRO'),
        ('G', 'GENERIC'),
        ('R', 'REFLECTION'),
        ('S', 'STAKEHOLDER'),
        ('A', 'ACTION'),
    )
    page_type = models.CharField(max_length=2, choices=page_choices)
    page_title = models.CharField(max_length=1000)
    scenarios = models.ManyToManyField(
        Scenario, related_name='pages',  through='Pages_to_scenario')
    version = models.IntegerField(default=1, editable=True)
    body = models.TextField()
    next_page = models.ForeignKey("Pages", on_delete= models.SET_NULL, null=True)

    class Meta:
        db_table = 'pages'
        unique_together = 'page','version'

class Pages_to_scenario(models.Model):
    page_id = models.ForeignKey(
        Pages, on_delete = models.CASCADE)
    scenario_id = models.ForeignKey(
        Scenario, on_delete = models.CASCADE)
    class Meta:
        unique_together = 'page_id','scenario_id'


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
        db_table = 'responses'
        ordering = ['scenario', 'page', 'student']
        unique_together = ('scenario', 'page', 'student', 'course')


class Issue(models.Model):
    issue = models.AutoField(default=None, primary_key=True, editable=False)
    scenario_id = models.ForeignKey(
        Scenario, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    importance_score = models.FloatField(validators=[MinValueValidator(0.0)])

    class Meta:
        db_table = 'issues'


class Stakeholders(models.Model):
    stakeholder = models.IntegerField(default = 1)
    version = models.IntegerField(default = 1)
    scenario = models.ForeignKey(
        Scenario, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=1000,  null=False)
    description = models.TextField(default="")
    job = models.TextField(default="default")
    introduction = models.TextField(default='default')
    enable_multi_convo = models.BooleanField(default = False)

    class Meta:
        db_table = 'stakeholders'
        unique_together = 'stakeholder','version'



class Questions(models.Model):
    question = models.IntegerField(default = 1)
    version = models.IntegerField(default = 1)
    points = models.IntegerField(default = 1)
    question_text = models.TextField()
    question_summary = models.TextField()
    class Meta:
        unique_together = 'question','version'
        
class Stakeholders_to_questions(models.Model):
    stakeholder_id = models.ForeignKey(
        Stakeholders, on_delete = models.CASCADE)
    question_id = models.ForeignKey(
        Questions, on_delete = models.CASCADE)
    class Meta:
        unique_together = 'stakeholder_id','question_id'

class Conversations(models.Model):
    conversation = models.AutoField(primary_key=True, editable=False)
    stakeholder = models.ForeignKey(
        Stakeholders, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    response = models.TextField(max_length=100)

    class Meta:
        db_table = 'conversations'


class Reflection_questions(models.Model):
    reflection_question = models.TextField()
    version = models.IntegerField(default = 1)

    class Meta:
        db_table = 'reflection_questions'

class Reflection_question_to_page(models.Model):
    reflection_questions_id = models.ForeignKey(
        Reflection_questions, on_delete = models.CASCADE)
    page_id = models.ForeignKey(
        Pages, on_delete = models.CASCADE)
    class Meta: 
        unique_together = 'page_id', 'reflection_questions_id'

class Generic_page(models.Model):

    page = models.ForeignKey(
        Pages, on_delete=models.CASCADE)
    body = models.TextField()
    version = models.IntegerField(default = 1)

    class Meta:
        db_table = 'generic_page'


class Stakeholder_to_page(models.Model):
    class Meta:
        unique_together = ['page', 'stakeholder']
        db_table = 'stakeholder_to_page'
    page = models.ForeignKey(
        Pages, on_delete=models.CASCADE)
    stakeholder = models.ForeignKey(
        Stakeholders, on_delete=models.CASCADE)


class Action_page(models.Model):
    class Meta:
        unique_together = ['page', 'choice']
        db_table = 'action_page'
    page = models.ForeignKey(
        Pages, on_delete=models.CASCADE)
    version = models.IntegerField(default = 1)
    choice = models.TextField()
    result_page = models.IntegerField(null=True)


class Reflections_taken(models.Model):
    reflections = models.TextField(max_length=100)
    response = models.ForeignKey(
        Response, on_delete=models.CASCADE)

    class Meta:
        db_table = 'reflections_taken'


class Response_to_action_page(models.Model):
    response = models.ForeignKey(
        Response, on_delete=models.CASCADE)
    action_page = models.ForeignKey(
        Action_page, on_delete=models.CASCADE)

    class Meta:
        db_table = 'response_to_action_page'
        unique_together = ['response', 'action_page']


class Responses_to_conversations(models.Model):
    response = models.ForeignKey(
        Response, on_delete=models.CASCADE)
    stakeholder = models.ForeignKey(
        Stakeholders, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    conversation = models.ForeignKey(
        Conversations, on_delete=models.CASCADE)

    class Meta:
        db_table = 'responses_to_conversations'


class Student_times(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE)
    scenario_id = models.ForeignKey(
        Scenario, on_delete=models.CASCADE)
    date_taken = models.DateField(auto_now_add=True)
    page = models.ForeignKey(
        Pages, on_delete=models.CASCADE)
    start_time = models.DateField(auto_now_add=True)
    end_time = models.DateField(null=True)

    class Meta:
        db_table = 'student_times'
        unique_together = ['student', 'scenario_id', 'course', 'page']


class Coverage(models.Model):

    stakeholder = models.ForeignKey(
        Stakeholders, on_delete=models.CASCADE,  default=None)
    issue = models.ForeignKey(
        Issue, on_delete=models.CASCADE, default=None)
    coverage_score = models.FloatField(validators=[MinValueValidator(0.0)])

    class Meta:
        unique_together = (('stakeholder'), ('issue'))
        db_table = 'coverage'


class Student_page_progress(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, default=None)
    page = models.ForeignKey(
        Pages, on_delete=models.CASCADE, default=None)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('student', "page")
