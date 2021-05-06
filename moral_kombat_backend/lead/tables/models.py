from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

######################################### new models ########################
class action_page(models.Model):
    action_page_id = models.IntegerField()
    id = models.IntegerField(primary_key = True)
    page = models.ForeignKey('pages', to_field='id', on_delete = models.CASCADE, related_name='action_page1')
    version = models.IntegerField()
    choice = models.TextField()
    result_page = models.IntegerField()

    class Meta:
        unique_together = ('action_page_id', 'version')
        db_table = 'action_page'


class conversations(models.Model):
    conversation = models.AutoField(primary_key=True)
    stakeholder = models.ForeignKey('stakeholders', to_field = 'stakeholder', on_delete = models.CASCADE, related_name='conversations1')
    QUESTION = models.TextField()
    RESPONSE = models.TextField()
    class Meta:
        db_table = 'conversations'


class courses(models.Model):
    course = models.AutoField(primary_key=True)
    name = models.TextField()
    students = models.ManyToManyField(
        'students', related_name='courses', through='students_to_course')
    professors = models.ManyToManyField(
        'professors', related_name='courses', through='professors_to_courses')
    scenarios = models.ManyToManyField(
        'scenarios', related_name='courses',  through='scenarios_for')
    class Meta:
        db_table = 'courses'


class courses_to_scenario(models.Model):
    course = models.ForeignKey('courses', to_field = 'course', on_delete = models.CASCADE, null = False)
    scenario = models.ForeignKey('scenarios', to_field = 'scenario_id', on_delete = models.CASCADE, null=False)
    permission = models.IntegerField()

    class Meta:
        unique_together = ('course', 'scenario')
        db_table = 'courses_to_scenario'


class coverage(models.Model):
    stakeholder = models.ForeignKey('stakeholders', to_field = 'stakeholder', on_delete = models.CASCADE, related_name = 'coverage2')
    issue = models.ForeignKey('issues', to_field = 'issue', on_delete = models.CASCADE, related_name = 'coverage1')
    coverage_score = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('stakeholder', 'issue')
        db_table = 'coverage'


class demographics(models.Model):
    student = models.ForeignKey('students', to_field = 'student', on_delete = models.CASCADE, related_name = 'demographics', unique = True)
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


class REFLECTION_QUESTIONS(models.Model):
    REFLECTION_QUESTION_ID = models.IntegerField()
    REFLECTION_QUESTION = models.TextField()
    VERSION = models.IntegerField()

    class Meta:
        unique_together = ('REFLECTION_QUESTION_ID', 'VERSION')
        db_table = 'reflection_questions'


class REFLECTIONS_TAKEN(models.Model):
    REFLECTIONS = models.TextField(blank=True)
    RESPONSE_ID = models.OneToOneField('RESPONSES', on_delete = models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'reflections_taken'


class RESPONSES(models.Model):
    RESPONSE_ID = models.AutoField(primary_key=True)
    RESPONSE = models.IntegerField()
    STUDENT = models.ForeignKey('STUDENTS', on_delete = models.CASCADE, db_column='student', )
    SCENARIO = models.ForeignKey('SCENARIOS', on_delete = models.CASCADE, db_column='scenario', )
    VERSION = models.IntegerField()
    PAGE = models.ForeignKey(PAGES, on_delete = models.CASCADE, db_column='page', )
    COURSE = models.ForeignKey(COURSES, on_delete = models.CASCADE, db_column='course', )
    DATE_TAKEN = models.DateField(auto_now_add=True)
    CHOICE = models.TextField()

    class Meta:
        unique_together = ('RESPONSE', 'STUDENT', 'SCENARIO', 'PAGE', 'COURSE', 'DATE_TAKEN')
        db_table = 'responses'

class RESPONSE_TO_ACTION_PAGE(models.Model):
    RESPONSE_ID = models.ForeignKey('RESPONSES', on_delete = models.CASCADE, )
    ACTION_PAGE = models.ForeignKey(ACTION_PAGE, on_delete = models.CASCADE, db_column='action_page', )

    class Meta:
        unique_together = ('RESPONSE_ID', 'ACTION_PAGE')
        db_table = 'response_to_action_page'

class RESPONSES_TO_CONVERSATIONS(models.Model):
    RESPONSE_ID = models.ForeignKey(RESPONSES, on_delete = models.CASCADE)
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', on_delete = models.CASCADE, db_column='stakeholder')
    STAKEHOLDER_VERSION = models.IntegerField()
    SCORE = models.DecimalField(max_digits=5, decimal_places=2)
    CONVERSATION = models.ForeignKey(CONVERSATIONS, on_delete = models.CASCADE, db_column='conversation')

    class Meta:
        unique_together = ('RESPONSE_ID', 'CONVERSATION')
        db_table = 'responses_to_conversations'


class SCENARIOS(models.Model):
    SCENARIO_ID = models.AutoField(primary_key=True)
    SCENARIO = models.IntegerField(default=1, editable=True)
    VERSION = models.IntegerField(default=1, editable=True)
    NAME = models.TextField(max_length=50, null=False)
    PUBLIC = models.BooleanField(default=False)
    NUM_CONVERSATION = models.IntegerField(default=0)
    IS_FINISHED = models.BooleanField(default=False)
    DATE_CREATED = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('SCENARIO', 'VERSION')
        db_table = 'scenarios'


class SCENARIOS_FOR(models.Model):
    SCENARIO = models.ForeignKey(SCENARIOS, on_delete = models.CASCADE)
    VERSION = models.IntegerField()
    COURSE = models.ForeignKey(COURSES, on_delete = models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('SCENARIO', 'COURSE')
        db_table = 'scenarios_for'


class STAKEHOLDER_TO_PAGE(models.Model):
    PAGE = models.ForeignKey(PAGES, on_delete = models.CASCADE, db_column='page')
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', on_delete = models.CASCADE, db_column='stakeholder')

    class Meta:
        unique_together = ('PAGE', 'STAKEHOLDER')
        db_table = 'stakeholder_to_page'


class STAKEHOLDERS(models.Model):
    STAKEHOLDER = models.IntegerField(unique = True)
    SCENARIO = models.ForeignKey(SCENARIOS, on_delete = models.CASCADE, db_column='scenario')
    VERSION = models.IntegerField()
    NAME = models.TextField()
    DESCRIPTION = models.TextField()
    JOB = models.TextField()
    INTRODUCTION = models.TextField()
    ENABLE_MULTI_CONVO = models.BooleanField()

    class Meta:
        unique_together = ('STAKEHOLDER', 'VERSION')
        db_table = 'stakeholders'


class STAKEHOLDERS_TO_QUESTIONS(models.Model):
    STAKEHOLDER = models.ForeignKey(STAKEHOLDERS, on_delete = models.CASCADE, db_column='stakeholder')
    QUESTION = models.ForeignKey(QUESTIONS, on_delete = models.CASCADE, db_column='question')

    class Meta:
        unique_together = ('STAKEHOLDER', 'QUESTION')
        db_table = 'stakeholders_to_questions'


class STUDENT_TIMES(models.Model):
    STUDENT = models.ForeignKey('STUDENTS', on_delete = models.CASCADE, db_column='student')
    COURSE = models.ForeignKey(COURSES, on_delete = models.CASCADE, db_column='course')
    SCENARIO_ID = models.ForeignKey(SCENARIOS, on_delete = models.CASCADE)
    DATE_TAKEN = models.DateField(auto_now = True)
    PAGE = models.IntegerField()
    START_TIME = models.DateField(auto_now_add = True)
    END_TIME = models.DateField(null = True, blank=True)

    class Meta:
        unique_together = ('STUDENT', 'COURSE', 'SCENARIO_ID')
        db_table = 'student_times'


class STUDENTS(models.Model):
    STUDENT = models.TextField(primary_key=True)
    FNAME = models.TextField()
    LNAME = models.TextField()

    class Meta:
        db_table = 'students'


class STUDENTS_TO_COURSE(models.Model):
    STUDENT = models.ForeignKey(STUDENTS, on_delete = models.CASCADE, db_column='student')
    COURSE = models.ForeignKey(COURSES, on_delete = models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('STUDENT', 'COURSE')
        db_table = 'students_to_course'