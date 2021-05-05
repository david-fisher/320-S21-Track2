from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

######################################### new models ########################
class ACTION_PAGE(models.Model):
    ACTION_PAGE_ID = models.IntegerField()
    ID = models.IntegerField(primary_key = True)
    PAGE = models.ForeignKey('PAGES', to_field='ID', on_delete = models.CASCADE, related_name="action_page1")
    VERSION = models.IntegerField()
    CHOICE = models.TextField()
    RESULT_PAGE = models.IntegerField()

    class Meta:
        unique_together = ('ACTION_PAGE_ID', 'VERSION')
        db_table = 'ACTION_PAGE'


class CONVERSATIONS(models.Model):
    CONVERSATION = models.AutoField(primary_key=True)
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', to_field = 'STAKEHOLDER', on_delete = models.CASCADE, related_name="conversations1")
    QUESTION = models.TextField()
    RESPONSE = models.TextField()
    class Meta:
        db_table = 'CONVERSATIONS'


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
        db_table = 'COURSES'


class COURSES_TO_SCENARIO(models.Model):
    COURSE = models.ForeignKey('COURSES', to_field = 'COURSE', on_delete = models.CASCADE, null = False)
    SCENARIO = models.ForeignKey('SCENARIOS', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, null=False)
    PERMISSION = models.IntegerField()

    class Meta:
        unique_together = ('COURSE', 'SCENARIO')
        db_table = 'COURSES_TO_SCENARIO'


class COVERAGE(models.Model):
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', to_field = 'STAKEHOLDER', on_delete = models.CASCADE, related_name = "coverage2")
    ISSUE = models.ForeignKey('ISSUES', to_field = 'ISSUE', on_delete = models.CASCADE, related_name = "coverage1")
    COVERAGE_SCORE = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('STAKEHOLDER', 'ISSUE')
        db_table = 'COVERAGE'


class DEMOGRAPHICS(models.Model):
    STUDENT = models.ForeignKey('STUDENTS', to_field = 'STUDENT', on_delete = models.CASCADE, related_name = "demographics", unique = True)
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
        db_table = 'DEMOGRAPHICS'


class GENERIC_PAGE(models.Model):
    GENERIC_PAGE_ID = models.IntegerField()
    PAGE = models.ForeignKey('PAGES', to_field= 'PAGE', on_delete = models.CASCADE, related_name="generic_page1")
    BODY = models.TextField()
    VERSION = models.IntegerField()

    class Meta:
        unique_together = ('GENERIC_PAGE_ID', 'VERSION')
        db_table = 'GENERIC_PAGE'

class ISSUES(models.Model):
    SCENARIO_ID = models.ForeignKey('SCENARIOS', to_field= 'SCENARIO_ID', on_delete = models.CASCADE, related_name = "scenario_id1", default = None)
    ISSUE = models.AutoField(default = None, primary_key = True, editable = False)
    NAME = models.CharField(max_length = 1000)
    IMPORTANCE_SCORE = models.IntegerField(validators = [MinValueValidator(0.0)])
    class Meta:
        db_table = 'ISSUES'


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
    SCENARIO = models.ForeignKey('SCENARIOS', to_field='SCENARIO_ID', on_delete = models.CASCADE, related_name="pages1")
    VERSION = models.IntegerField(default=1, editable=True)
    BODY = models.TextField(blank=True, null=True)
    ID = models.IntegerField(primary_key = True)
    NEXT_ID = models.ForeignKey('PAGES', to_field='ID', on_delete = models.CASCADE, related_name="pages2")
    X_COORDINATE = models.IntegerField()
    Y_COORDINATE = models.IntegerField()
    COMPLETED = models.BooleanField(default= False)

    class Meta:
        unique_together = ('PAGE', 'VERSION')
        db_table = 'PAGES'


class PAGES_TO_SCENARIO(models.Model):
    PAGE_ID = models.ForeignKey('PAGES', to_field = 'PAGE', on_delete = models.CASCADE, related_name="stakeholder_page1")
    SCENARIO_ID = models.ForeignKey('SCENARIOS', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name="stakeholder_page2")

    class Meta:
        unique_together = ('PAGE_ID', 'SCENARIO_ID')
        db_table = 'PAGES_TO_SCENARIO'


class PROFESSORS(models.Model):
    PROFESSOR = models.TextField(primary_key=True)
    FNAME = models.TextField()
    LNAME = models.TextField(blank=True)
    class Meta:
        db_table = 'PROFESSORS'
    # courses = models.ManyToManyField( Courses, related_name='professor',  through='ProfessorsToCourses')



class PROFESSORS_TO_COURSES(models.Model):
    PROFESSOR = models.ForeignKey(PROFESSORS, on_delete = models.CASCADE, db_column='professor')
    COURSE = models.ForeignKey(COURSES, on_delete = models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('PROFESSOR', 'COURSE')
        db_table = 'PROFESSORS_TO_COURSES'


class PROFESSORS_TO_SCENARIO(models.Model):
    PROFESSOR = models.ForeignKey(PROFESSORS, on_delete = models.CASCADE, db_column='professor')
    SCENARIO = models.ForeignKey('SCENARIOS', on_delete = models.CASCADE, db_column='scenario')
    PERMISSION = models.IntegerField()

    class Meta:
        unique_together = ('PROFESSOR', 'SCENARIO')
        db_table = 'PROFESSORS_TO_SCENARIO'


class QUESTIONS(models.Model):
    QUESTION = models.IntegerField()
    VERSION = models.IntegerField()
    POINTS = models.IntegerField()
    QUESTION_TEXT = models.TextField(blank=True)
    QUESTION_SUMMARY = models.TextField(blank=True)

    class Meta:
        unique_together = ('QUESTION', 'VERSION')
        db_table = 'QUESTIONS'


class REFLECTION_QUESTION_TO_PAGE(models.Model):
    REFLECTION_QUESTION_ID = models.ForeignKey('REFLECTION_QUESTIONS', on_delete = models.CASCADE)
    PAGE = models.ForeignKey(PAGES, on_delete = models.CASCADE)

    class Meta:
        unique_together = ('REFLECTION_QUESTION_ID', 'PAGE')
        db_table = 'REFLECTION_QUESTION_TO_PAGE'


class REFLECTION_QUESTIONS(models.Model):
    REFLECTION_QUESTION_ID = models.IntegerField()
    REFLECTION_QUESTION = models.TextField()
    VERSION = models.IntegerField()

    class Meta:
        unique_together = ('REFLECTION_QUESTION_ID', 'VERSION')
        db_table = 'REFLECTION_QUESTIONS'


class REFLECTIONS_TAKEN(models.Model):
    REFLECTIONS = models.TextField(blank=True)
    RESPONSE_ID = models.OneToOneField('RESPONSES', on_delete = models.CASCADE, primary_key=True)

    class Meta:
        db_table = 'REFLECTIONS_TAKEN'


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
        db_table = 'RESPONSES'

class RESPONSE_TO_ACTION_PAGE(models.Model):
    RESPONSE_ID = models.ForeignKey('RESPONSES', on_delete = models.CASCADE, )
    ACTION_PAGE = models.ForeignKey(ACTION_PAGE, on_delete = models.CASCADE, db_column='action_page', )

    class Meta:
        unique_together = ('RESPONSE_ID', 'ACTION_PAGE')
        db_table = 'RESPONSE_TO_ACTION_PAGE'

class RESPONSES_TO_CONVERSATIONS(models.Model):
    RESPONSE_ID = models.ForeignKey(RESPONSES, on_delete = models.CASCADE)
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', on_delete = models.CASCADE, db_column='stakeholder')
    STAKEHOLDER_VERSION = models.IntegerField()
    SCORE = models.DecimalField(max_digits=5, decimal_places=2)
    CONVERSATION = models.ForeignKey(CONVERSATIONS, on_delete = models.CASCADE, db_column='conversation')

    class Meta:
        unique_together = ('RESPONSE_ID', 'CONVERSATION')
        db_table = 'RESPONSES_TO_CONVERSATIONS'


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
        db_table = 'SCENARIOS'


class SCENARIOS_FOR(models.Model):
    SCENARIO = models.ForeignKey(SCENARIOS, on_delete = models.CASCADE)
    VERSION = models.IntegerField()
    COURSE = models.ForeignKey(COURSES, on_delete = models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('SCENARIO', 'COURSE')
        db_table = 'SCENARIOS_FOR'


class STAKEHOLDER_TO_PAGE(models.Model):
    PAGE = models.ForeignKey(PAGES, on_delete = models.CASCADE, db_column='page')
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', on_delete = models.CASCADE, db_column='stakeholder')

    class Meta:
        unique_together = ('PAGE', 'STAKEHOLDER')
        db_table = 'STAKEHOLDER_TO_PAGE'


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
        db_table = 'STAKEHOLDERS'


class STAKEHOLDERS_TO_QUESTIONS(models.Model):
    STAKEHOLDER = models.ForeignKey(STAKEHOLDERS, on_delete = models.CASCADE, db_column='stakeholder')
    QUESTION = models.ForeignKey(QUESTIONS, on_delete = models.CASCADE, db_column='question')

    class Meta:
        unique_together = ('STAKEHOLDER', 'QUESTION')
        db_table = 'STAKEHOLDERS_TO_QUESTIONS'


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
        db_table = 'STUDENT_TIMES'


class STUDENTS(models.Model):
    STUDENT = models.TextField(primary_key=True)
    FNAME = models.TextField()
    LNAME = models.TextField()

    class Meta:
        db_table = 'STUDENTS'


class STUDENTS_TO_COURSE(models.Model):
    STUDENT = models.ForeignKey(STUDENTS, on_delete = models.CASCADE, db_column='student')
    COURSE = models.ForeignKey(COURSES, on_delete = models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('STUDENT', 'COURSE')
        db_table = 'STUDENTS_TO_COURSE'