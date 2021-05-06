from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

######################################### new models ########################
class ACTION_PAGE(models.Model):
    ACTION_PAGE_ID = models.IntegerField()
    ID = models.IntegerField(primary_key = True)
    PAGE = models.ForeignKey('PAGES', to_field='ID', on_delete = models.CASCADE, related_name='action_page1')
    VERSION = models.IntegerField()
    CHOICE = models.TextField()
    RESULT_PAGE = models.IntegerField()

    class Meta:
        unique_together = ('ACTION_PAGE_ID', 'VERSION')
        db_table = 'action_page'


class CONVERSATIONS(models.Model):
    CONVERSATION = models.AutoField(primary_key=True)
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', to_field = 'STAKEHOLDER', on_delete = models.CASCADE, related_name='conversations1')
    QUESTION = models.TextField()
    RESPONSE = models.TextField()
    class Meta:
        db_table = 'conversations'


class COURSES(models.Model):
    COURSE = models.AutoField(primary_key=True)
    NAME = models.TextField()
    STUDENTS = models.ManyToManyField(
        'STUDENTS', related_name='COURSES', through='STUDENTS_TO_COURSE')
    professors = models.ManyToManyField(
        'PROFESSORS', related_name='COURSES', through='PROFESSORS_TO_COURSES')
    scenarios = models.ManyToManyField(
        'SCENARIOS', related_name='COURSES',  through='SCENARIOS_FOR')
    class Meta:
        db_table = 'courses'


class COURSES_TO_SCENARIO(models.Model):
    COURSE = models.ForeignKey('COURSES', to_field = 'COURSE', on_delete = models.CASCADE, null = False)
    SCENARIO = models.ForeignKey('SCENARIOS', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, null=False)
    PERMISSION = models.IntegerField()

    class Meta:
        unique_together = ('COURSE', 'SCENARIO')
        db_table = 'courses_to_scenario'


class COVERAGE(models.Model):
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', to_field = 'STAKEHOLDER', on_delete = models.CASCADE, related_name = 'coverage2')
    ISSUE = models.ForeignKey('ISSUES', to_field = 'ISSUE', on_delete = models.CASCADE, related_name = 'coverage1')
    COVERAGE_SCORE = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('STAKEHOLDER', 'ISSUE')
        db_table = 'coverage'


class DEMOGRAPHICS(models.Model):
    STUDENT = models.ForeignKey('STUDENTS', to_field = 'STUDENT', on_delete = models.CASCADE, related_name = 'demographics', unique = True)
    AGE = models.SmallIntegerField()
    GRADE_CHOICES = (('0', 'Other'),
                     ('1', 'Freshmen'),
                     ('2', 'Sophomore'),
                     ('3', 'Junior'),
                     ('4', 'Senior'))
    GRADE = models.CharField(
        max_length=1, choices=GRADE_CHOICES)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('OT', 'Other'),
    )
    GENDER = models.CharField(
        max_length=2, choices=GENDER_CHOICES)
    RACE = models.CharField(max_length=30)
    MAJOR = models.CharField(max_length=30)

    class Meta:
        db_table = 'demographics'


class GENERIC_PAGE(models.Model):
    GENERIC_PAGE_ID = models.IntegerField()
    PAGE = models.ForeignKey('PAGES', to_field= 'PAGE', on_delete = models.CASCADE, related_name='generic_page1')
    BODY = models.TextField()
    VERSION = models.IntegerField()

    class Meta:
        unique_together = ('GENERIC_PAGE_ID', 'VERSION')
        db_table = 'generic_page'

class ISSUES(models.Model):
    SCENARIO_ID = models.ForeignKey('SCENARIOS', to_field= 'SCENARIO_ID', on_delete = models.CASCADE, related_name = 'scenario_id1', default = None)
    ISSUE = models.AutoField(default = None, primary_key = True, editable = False)
    NAME = models.CharField(max_length = 1000)
    IMPORTANCE_SCORE = models.IntegerField(validators = [MinValueValidator(0.0)])
    class Meta:
        db_table = 'issues'


class PAGES(models.Model):
    PAGE = models.IntegerField(unique = True)
    PAGE_CHOICES = (
        ('I', 'INTRO'),
        ('F', 'FEEDBACK'),
        ('G', 'GENERIC'),
        ('R', 'REFLECTION'),
        ('S', 'STAKEHOLDER'),
        ('A', 'ACTION'),
    )
    PAGE_TYPE = models.CharField(max_length=2, choices=PAGE_CHOICES)
    PAGE_TITLE = models.CharField(max_length=1000)
    SCENARIO = models.ForeignKey('SCENARIOS', to_field='SCENARIO_ID', on_delete = models.CASCADE, related_name='pages1')
    VERSION = models.IntegerField(default=1, editable=True)
    BODY = models.TextField(blank=True, null=True)
    ID = models.IntegerField(primary_key = True)
    NEXT_ID = models.ForeignKey('PAGES', to_field='ID', on_delete = models.CASCADE, related_name='pages2')
    X_COORDINATE = models.IntegerField()
    Y_COORDINATE = models.IntegerField()
    COMPLETED = models.BooleanField(default= False)

    class Meta:
        unique_together = ('PAGE', 'VERSION')
        db_table = 'pages'


class PAGES_TO_SCENARIO(models.Model):
    PAGE_ID = models.ForeignKey('PAGES', to_field = 'PAGE', on_delete = models.CASCADE, related_name='stakeholder_page1')
    SCENARIO_ID = models.ForeignKey('SCENARIOS', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name='stakeholder_page2')

    class Meta:
        unique_together = ('PAGE_ID', 'SCENARIO_ID')
        db_table = 'pages_to_scenario'


class PROFESSORS(models.Model):
    PROFESSOR = models.TextField(primary_key=True)
    FNAME = models.TextField()
    LNAME = models.TextField(blank=True)
    class Meta:
        db_table = 'professors'
    # courses = models.ManyToManyField( Courses, related_name='professor',  through='ProfessorsToCourses')



class PROFESSORS_TO_COURSES(models.Model):
    PROFESSOR = models.ForeignKey(PROFESSORS, on_delete = models.CASCADE, db_column='professor')
    COURSE = models.ForeignKey(COURSES, on_delete = models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('PROFESSOR', 'COURSE')
        db_table = 'professors_to_courses'


class PROFESSORS_TO_SCENARIO(models.Model):
    PROFESSOR = models.ForeignKey(PROFESSORS, on_delete = models.CASCADE, db_column='professor')
    SCENARIO = models.ForeignKey('SCENARIOS', on_delete = models.CASCADE, db_column='scenario')
    PERMISSION = models.IntegerField()

    class Meta:
        unique_together = ('PROFESSOR', 'SCENARIO')
        db_table = 'professors_to_scenario'


class QUESTIONS(models.Model):
    QUESTION = models.IntegerField()
    VERSION = models.IntegerField()
    POINTS = models.IntegerField()
    QUESTION_TEXT = models.TextField(blank=True)
    QUESTION_SUMMARY = models.TextField(blank=True)

    class Meta:
        unique_together = ('QUESTION', 'VERSION')
        db_table = 'questions'


class REFLECTION_QUESTION_TO_PAGE(models.Model):
    REFLECTION_QUESTION_ID = models.ForeignKey('REFLECTION_QUESTIONS', on_delete = models.CASCADE)
    PAGE = models.ForeignKey(PAGES, on_delete = models.CASCADE)

    class Meta:
        unique_together = ('REFLECTION_QUESTION_ID', 'PAGE')
        db_table = 'reflection_question_to_page'


class reflection_questions(models.Model):
    reflection_question_id = models.IntegerField()
    reflection_question = models.TextField()
    version = models.IntegerField()

    class Meta:
        unique_together = ('reflection_question_id', 'version')
        db_table = 'reflection_questions'


class reflections_taken(models.Model):
    reflections = models.TextField(blank=True)
    response_id = models.OneToOneField(responses, on_delete = models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'reflections_taken'


class responses(models.Model):
    response_id = models.AutoField(primary_key=True)
    response = models.IntegerField()
    student = models.ForeignKey(students, on_delete = models.CASCADE, db_column='student', )
    scenario = models.ForeignKey(scenarios, on_delete = models.CASCADE, db_column='scenario', )
    version = models.IntegerField()
    page = models.ForeignKey(pages, on_delete = models.CASCADE, db_column='page', )
    course = models.ForeignKey(courses, on_delete = models.CASCADE, db_column='course', )
    date_taken = models.DateField(auto_now_add=True)
    choice = models.TextField()

    class Meta:
        unique_together = ('response', 'student', 'scenario', 'page', 'course', 'date_taken')
        db_table = 'responses'

class response_to_action_page(models.Model):
    response_id = models.ForeignKey(responses, on_delete = models.CASCADE, )
    action_page = models.ForeignKey(action_page, on_delete = models.CASCADE, db_column='action_page', )

    class Meta:
        unique_together = ('response_id', 'action_page')
        db_table = 'response_to_action_page'

class responses_to_conversations(models.Model):
    response_id = models.ForeignKey(responses, on_delete = models.CASCADE)
    stakeholder = models.ForeignKey(stakeholders, on_delete = models.CASCADE, db_column='stakeholder')
    stakeholder_version = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    conversation = models.ForeignKey(conversations, on_delete = models.CASCADE, db_column='conversation')

    class Meta:
        unique_together = ('response_id', 'conversation')
        db_table = 'responses_to_conversations'


class scenarios(models.Model):
    scenario_id = models.AutoField(primary_key=True)
    scenario = models.IntegerField(default=1, editable=True)
    version = models.IntegerField(default=1, editable=True)
    name = models.TextField(max_length=50, null=False)
    public = models.BooleanField(default=False)
    num_conversation = models.IntegerField(default=0)
    is_finished = models.BooleanField(default=False)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('scenario', 'version')
        db_table = 'scenarios'


class scenarios_for(models.Model):
    scenario = models.ForeignKey(scenarios, on_delete = models.CASCADE)
    version = models.IntegerField()
    course = models.ForeignKey(courses, on_delete = models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('scenario', 'course')
        db_table = 'scenarios_for'


class stakeholder_to_page(models.Model):
    page = models.ForeignKey(pages, on_delete = models.CASCADE, db_column='page')
    stakeholder = models.ForeignKey(stakeholders, on_delete = models.CASCADE, db_column='stakeholder')

    class Meta:
        unique_together = ('page', 'stakeholder')
        db_table = 'stakeholder_to_page'


class stakeholders(models.Model):
    stakeholder = models.IntegerField(unique = True)
    scenario = models.ForeignKey(scenarios, on_delete = models.CASCADE, db_column='scenario')
    version = models.IntegerField()
    name = models.TextField()
    description = models.TextField()
    job = models.TextField()
    introduction = models.TextField()
    enable_multi_convo = models.BooleanField()

    class Meta:
        unique_together = ('stakeholder', 'version')
        db_table = 'stakeholders'


class stakeholders_to_questions(models.Model):
    stakeholder = models.ForeignKey(stakeholders, on_delete = models.CASCADE, db_column='stakeholder')
    question = models.ForeignKey(questions, on_delete = models.CASCADE, db_column='question')

    class Meta:
        unique_together = ('stakeholder', 'question')
        db_table = 'stakeholders_to_questions'


class student_times(models.Model):
    student = models.ForeignKey(students, on_delete = models.CASCADE, db_column='student')
    course = models.ForeignKey(courses, on_delete = models.CASCADE, db_column='course')
    scenario_id = models.ForeignKey(scenarios, on_delete = models.CASCADE)
    date_taken = models.DateField(auto_now = True)
    page = models.IntegerField()
    start_time = models.DateField(auto_now_add = True)
    end_time = models.DateField(null = True, blank=True)

    class Meta:
        unique_together = ('student', 'course', 'scenario_id')
        db_table = 'student_times'


class students(models.Model):
    student = models.TextField(primary_key=True)
    fname = models.TextField()
    lname = models.TextField()

    class Meta:
        db_table = 'students'


class students_to_course(models.Model):
    student = models.ForeignKey(students, on_delete = models.CASCADE, db_column='student')
    course = models.ForeignKey(courses, on_delete = models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('student', 'course')
        db_table = 'students_to_course'