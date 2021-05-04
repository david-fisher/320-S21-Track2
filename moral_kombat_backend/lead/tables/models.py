from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

######################################### new models ########################
class ACTION_PAGE(models.Model):
    ACTION_PAGE_ID = models.IntegerField()
    PAGE = models.ForeignKey('Pages', on_delete = models.CASCADE, db_column='page')
    VERSION = models.IntegerField()
    CHOICE = models.TextField()
    RESULT_PAGE = models.IntegerField()

    class Meta:
        unique_together = ('ACTION_PAGE_ID', 'VERSION')


class CONVERSATIONS(models.Model):
    CONVERSATION = models.AutoField(primary_key=True)
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', to_field = 'STAKEHOLDER', on_delete = models.CASCADE, related_name="conversations1")
    QUESTION = models.TextField()
    RESPONSE = models.TextField()


class COURSES(models.Model):
    COURSE = models.AutoField(primary_key=True)
    NAME = models.TextField()
    STUDENTS = models.ManyToManyField(
        'STUDENTS', related_name='COURSES', through='STUDENTS_TO_COURSE')
    professors = models.ManyToManyField(
        'PROFESSORS', related_name='COURSES', through='PROFESSORS_TO_COURSES')
    scenarios = models.ManyToManyField(
        'SCENARIOS', related_name='COURSES',  through='SCENARIOS_FOR')



class COURSES_TO_SCENARIO(models.Model):
    COURSE = models.ForeignKey('COURSES', to_field = 'COURSE', on_delete = models.CASCADE, null = False)
    SCENARIO = models.ForeignKey('SCENARIOS', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, null=False)
    PERMISSION = models.IntegerField()

    class Meta:
        unique_together = ('COURSE', 'SCENARIO')


class COVERAGE(models.Model):
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', to_field = 'STAKEHOLDER', on_delete = models.CASCADE, related_name = "coverage2")
    ISSUE = models.ForeignKey('ISSUES', to_field = 'ISSUE', on_delete = models.CASCADE, related_name = "coverage1")
    COVERAGE_SCORE = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('STAKEHOLDER', 'ISSUE')


class DEMOGRAPHICS(models.Model):
    STUDENT = models.ForeignKey('STUDENTS', to_field = 'STUDENT', on_delete = models.CASCADE, related_name = "demographics", unique = True)
    AGE = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
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


class GENERIC_PAGE(models.Model):
    GENERIC_PAGE_ID = models.IntegerField()
    PAGE = models.ForeignKey('PAGES', to_field= 'PAGE', on_delete = models.CASCADE, related_name="generic_page1")
    BODY = models.TextField()
    VERSION = models.IntegerField()

    class Meta:
        unique_together = ('GENERIC_PAGE_ID', 'VERSION')


class ISSUES(models.Model):
    SCENARIO_ID = models.ForeignKey('SCENARIOS', to_field= 'SCENARIO_ID', on_delete = models.CASCADE, related_name = "scenario_id1", default = None)
    ISSUE = models.AutoField(default = None, primary_key = True, editable = False)
    NAME = models.CharField(max_length = 1000)
    IMPORTANCE_SCORE = models.IntegerField(validators = [MinValueValidator(0.0)])


class PAGES(models.Model):
    PAGE = models.IntegerField()
    PAGE_CHOICES = (
        ('I', 'INTRO'),
        ('F', 'FEEDBACK'),
        ('G', 'GENERIC'),
        ('R', 'REFLECTION'),
        ('S', 'STAKEHOLDER'),
        ('A', 'ACTION'),
    )
    PAGE_TYPE = models.CharField(max_length=2, choices=page_choices)
    PAGE_TITLE = models.CharField(max_length=1000)
    SCENARIO = models.ForeignKey('SCENARIOS', to_field='SCENARIO_ID', on_delete = models.CASCADE, related_name="pages1")
    VERSION = models.IntegerField(default=1, editable=True)
    BODY = models.TextField(blank=True, null=True)
    NEXT_ID = models.ForeignKey('PAGES', to_field='ID', on_delete = models.CASCADE, related_name="pages2")
    X_COORDINATE = models.IntegerField()
    Y_COORDINATE = models.IntegerField()
    COMPLETED = models.BooleanField(default= False)

    class Meta:
        unique_together = ('PAGE', 'VERSION')


class PAGES_TO_SCENARIO(models.Model):
    PAGE_ID = models.ForeignKey('PAGES', to_field = 'PAGE', on_delete = models.CASCADE, related_name="stakeholder_page1")
    SCENARIO_ID = models.ForeignKey('SCENARIOS', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name="stakeholder_page2")

    class Meta:
        unique_together = ('PAGE', 'SCENARIO')


class PROFESSORS(models.Model):
    PROFESSOR = models.TextField(primary_key=True)
    FNAME = models.TextField()
    LNAME = models.TextField(blank=True)
    # courses = models.ManyToManyField( Courses, related_name='professor',  through='ProfessorsToCourses')



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
    scenario_id = models.AutoField(primary_key=True)
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
    date_taken = models.DateField(auto_now = True)
    page = models.IntegerField()
    start_time = models.DateField(auto_now_add = True)
    end_time = models.DateField(null = True, blank=True)

    class Meta:
        db_table = 'student_times'
        unique_together = ('student', 'course', 'scenario')


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