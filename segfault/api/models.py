# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import django
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class ActionPage(models.Model):
    action_page_id = models.IntegerField()
    page = models.ForeignKey('Pages', on_delete = models.CASCADE, db_column='page')
    version = models.IntegerField()
    choice = models.TextField()
    result_page = models.IntegerField()

    class Meta:
        db_table = 'action_page'
        unique_together = ('action_page_id', 'version')


class Conversations(models.Model):
    conversation = models.AutoField(primary_key=True)
    stakeholder = models.ForeignKey('Stakeholders', on_delete = models.CASCADE, db_column='stakeholder')
    question = models.TextField()
    response = models.TextField()

    class Meta:
        db_table = 'conversations'


class Courses(models.Model):
    course = models.AutoField(primary_key=True)
    name = models.TextField()
    students = models.ManyToManyField(
        'Students', related_name='courses', through='StudentsToCourse')
    professors = models.ManyToManyField(
        'Professors', related_name='courses', through='ProfessorsToCourses')
    scenarios = models.ManyToManyField(
        'Scenarios', related_name='courses',  through='CoursesToScenario')

    class Meta:
        db_table = 'courses'


class CoursesToScenario(models.Model):
    course = models.ForeignKey('Courses', on_delete = models.CASCADE, db_column='course', null=False)
    scenario = models.ForeignKey('Scenarios',on_delete = models.CASCADE, db_column='scenario', null=False)
    permission = models.IntegerField()

    class Meta:
        db_table = 'courses_to_scenario'
        unique_together = ('course', 'scenario')


class Coverage(models.Model):
    stakeholder = models.ForeignKey('Stakeholders',on_delete = models.CASCADE, db_column='stakeholder')
    issue = models.ForeignKey('Issues', on_delete = models.CASCADE, db_column='issue')
    coverage_score = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = 'coverage'
        unique_together = ('stakeholder', 'issue')


class Demographics(models.Model):
    student = models.OneToOneField('Students', primary_key=True, on_delete=models.CASCADE, related_name="demographics", null=False, db_column='student')
    age = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], db_column='age')
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


class GenericPage(models.Model):
    generic_page_id = models.IntegerField()
    page = models.ForeignKey('Pages', on_delete = models.CASCADE, db_column='page')
    body = models.TextField()
    version = models.IntegerField()

    class Meta:
        db_table = 'generic_page'
        unique_together = ('generic_page_id', 'version')


class Issues(models.Model):
    issue = models.AutoField(primary_key=True)
    scenario = models.ForeignKey('Scenarios', on_delete = models.CASCADE)
    name = models.TextField()
    importance_score = models.IntegerField()

    class Meta:
        db_table = 'issues'


class Pages(models.Model):
    page = models.IntegerField()
    page_choices = (
        ('I', 'INTRO'),
        ('G', 'GENERIC'),
        ('R', 'REFLECTION'),
        ('S', 'STAKEHOLDER'),
        ('A', 'ACTION'),
    )
    page_type = models.CharField(max_length=2, choices=page_choices)
    page_title = models.CharField(max_length=1000)
    scenario = models.ForeignKey('Scenarios', on_delete=models.CASCADE, db_column='scenario')
    version = models.IntegerField(default=1, editable=True)
    body = models.TextField(blank=True, null=True)
    next = models.ForeignKey('self',on_delete = models.CASCADE, null=True)
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    completed = models.BooleanField(default= False)

    class Meta:
        db_table = 'pages'
        unique_together = ('page', 'version')


class PagesToScenario(models.Model):
    page = models.ForeignKey(Pages, on_delete = models.CASCADE)
    scenario = models.ForeignKey('Scenarios', on_delete = models.CASCADE)

    class Meta:
        db_table = 'pages_to_scenario'
        unique_together = ('page', 'scenario')


class Professors(models.Model):
    professor = models.TextField(primary_key=True)
    fname = models.TextField()
    lname = models.TextField(blank=True)
    # courses = models.ManyToManyField( Courses, related_name='professor',  through='ProfessorsToCourses')

    class Meta:
        db_table = 'professors'


class ProfessorsToCourses(models.Model):
    professor = models.ForeignKey(Professors, on_delete = models.CASCADE, db_column='professor')
    course = models.ForeignKey(Courses, on_delete = models.CASCADE, db_column='course')

    class Meta:
        db_table = 'professors_to_courses'
        unique_together = ('professor', 'course')


class ProfessorsToScenario(models.Model):
    professor = models.ForeignKey(Professors, on_delete = models.CASCADE, db_column='professor')
    scenario = models.ForeignKey('Scenarios', on_delete = models.CASCADE, db_column='scenario')
    permission = models.IntegerField()

    class Meta:
        db_table = 'professors_to_scenario'
        unique_together = ('professor', 'scenario')


class Questions(models.Model):
    question = models.IntegerField()
    version = models.IntegerField()
    points = models.IntegerField()
    question_text = models.TextField(blank=True)
    question_summary = models.TextField(blank=True)

    class Meta:
        db_table = 'questions'
        unique_together = ('question', 'version')


class ReflectionQuestionToPage(models.Model):
    reflection_question = models.ForeignKey('ReflectionQuestions', on_delete = models.CASCADE)
    page = models.ForeignKey(Pages, on_delete = models.CASCADE)

    class Meta:
        db_table = 'reflection_question_to_page'
        unique_together = ('reflection_question', 'page')


class ReflectionQuestions(models.Model):
    reflection_question_id = models.IntegerField()
    reflection_question = models.TextField()
    version = models.IntegerField()

    class Meta:
        db_table = 'reflection_questions'
        unique_together = ('reflection_question_id', 'version')


class ReflectionsTaken(models.Model):
    reflections = models.TextField(blank=True)
    response = models.OneToOneField('Responses', on_delete = models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'reflections_taken'


class Responses(models.Model):
    response_id = models.AutoField(primary_key=True)
    response = models.IntegerField()
    student = models.ForeignKey('Students', on_delete = models.CASCADE, db_column='student', )
    scenario = models.ForeignKey('Scenarios', on_delete = models.CASCADE, db_column='scenario', )
    version = models.IntegerField()
    page = models.ForeignKey(Pages, on_delete = models.CASCADE, db_column='page', )
    course = models.ForeignKey(Courses, on_delete = models.CASCADE, db_column='course', )
    date_taken = models.DateField(auto_now_add=True)
    choice = models.TextField()

    class Meta:
        db_table = 'responses'
        unique_together = ('response', 'student', 'scenario', 'page', 'course', 'date_taken')

class ResponseToActionPage(models.Model):
    response = models.ForeignKey('Responses', on_delete = models.CASCADE, )
    action_page = models.ForeignKey(ActionPage, on_delete = models.CASCADE, db_column='action_page', )

    class Meta:
        db_table = 'response_to_action_page'
        unique_together = ('response', 'action_page')

class ResponsesToConversations(models.Model):
    response = models.ForeignKey(Responses, on_delete = models.CASCADE)
    stakeholder = models.ForeignKey('Stakeholders', on_delete = models.CASCADE, db_column='stakeholder')
    stakeholder_version = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    conversation = models.ForeignKey(Conversations, on_delete = models.CASCADE, db_column='conversation')

    class Meta:
        db_table = 'responses_to_conversations'
        unique_together = ('response', 'conversation')


class Scenarios(models.Model):
    scenario_id = models.AutoField(primary_key=True, editable=False)
    scenario = models.IntegerField(default=1, editable=True)
    version = models.IntegerField(default=1, editable=True)
    name = models.TextField(max_length=50, null=False)
    public = models.BooleanField(default=False)
    num_conversation = models.IntegerField(default=0)
    is_finished = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'scenarios'
        unique_together = ('scenario', 'version')


class ScenariosFor(models.Model):
    scenario = models.ForeignKey(Scenarios, on_delete = models.CASCADE)
    version = models.IntegerField()
    course = models.ForeignKey(Courses, on_delete = models.CASCADE, db_column='course')

    class Meta:
        db_table = 'scenarios_for'
        unique_together = ('scenario', 'course')


class StakeholderToPage(models.Model):
    page = models.ForeignKey(Pages, on_delete = models.CASCADE, db_column='page')
    stakeholder = models.ForeignKey('Stakeholders', on_delete = models.CASCADE, db_column='stakeholder')

    class Meta:
        db_table = 'stakeholder_to_page'
        unique_together = ('page', 'stakeholder')


class Stakeholders(models.Model):
    stakeholder = models.IntegerField()
    scenario = models.ForeignKey(Scenarios, on_delete = models.CASCADE, db_column='scenario')
    version = models.IntegerField()
    name = models.TextField()
    description = models.TextField()
    job = models.TextField()
    introduction = models.TextField()
    enable_multi_convo = models.BooleanField()

    class Meta:
        db_table = 'stakeholders'
        unique_together = ('stakeholder', 'version')


class StakeholdersToQuestions(models.Model):
    stakeholder = models.ForeignKey(Stakeholders, on_delete = models.CASCADE, db_column='stakeholder')
    question = models.ForeignKey(Questions, on_delete = models.CASCADE, db_column='question')

    class Meta:
        db_table = 'stakeholders_to_questions'
        unique_together = ('stakeholder', 'question')


class StudentTimes(models.Model):
    student = models.ForeignKey('Students', on_delete = models.CASCADE, db_column='student')
    course = models.ForeignKey(Courses, on_delete = models.CASCADE, db_column='course')
    scenario = models.ForeignKey(Scenarios, on_delete = models.CASCADE)
    date_taken = models.DateField()
    page = models.IntegerField()
    start_time = models.DateField()
    end_time = models.DateField()

    class Meta:
        db_table = 'student_times'
        unique_together = ('student', 'course', 'scenario', 'date_taken', 'page')


class Students(models.Model):
    student = models.TextField(primary_key=True)
    fname = models.TextField()
    lname = models.TextField()

    class Meta:
        db_table = 'students'


class StudentsToCourse(models.Model):
    student = models.ForeignKey(Students, on_delete = models.CASCADE, db_column='student')
    course = models.ForeignKey(Courses, on_delete = models.CASCADE, db_column='course')

    class Meta:
        db_table = 'students_to_course'
        unique_together = ('student', 'course')