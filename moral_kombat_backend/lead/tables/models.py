from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

######################################### new models ########################
class action_page(models.Model):
    action_page_id = models.IntegerField()
    id = models.IntegerField(primary_key = True)
    page = models.ForeignKey('pages', on_delete = models.CASCADE, related_name='action_page1', db_column='page')
    version = models.IntegerField()
    choice = models.TextField()
    result_page = models.IntegerField()

    class Meta:
        unique_together = ('action_page_id', 'version')
        db_table = 'action_page'


class conversations(models.Model):
    conversation = models.AutoField(primary_key=True)
    stakeholder = models.ForeignKey('stakeholders', on_delete = models.CASCADE, related_name='conversations1', db_column='stakeholder')
    question = models.TextField()
    response = models.TextField()
    question_summary = models.TextField()
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
    course = models.ForeignKey('courses', on_delete = models.CASCADE, null = False, db_column='course')
    scenario = models.ForeignKey('scenarios', on_delete = models.CASCADE, null=False, db_column='scenario_id')
    permission = models.IntegerField()

    class Meta:
        unique_together = ('course', 'scenario')
        db_table = 'courses_to_scenario'


class coverage(models.Model):
    stakeholder = models.ForeignKey('stakeholders', on_delete = models.CASCADE, related_name = 'coverage2', db_column='stakeholder')
    issue = models.ForeignKey('issues', on_delete = models.CASCADE, related_name = 'coverage1', db_column='issue')
    coverage_score = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        unique_together = ('stakeholder', 'issue')
        db_table = 'coverage'


class demographics(models.Model):
    student = models.ForeignKey('students', on_delete = models.CASCADE, related_name = 'demographics', unique = True, db_column='student')
    age = models.SmallIntegerField()
    grade_choices = (('0', 'Other'),
                     ('1', 'Freshmen'),
                     ('2', 'Sophomore'),
                     ('3', 'Junior'),
                     ('4', 'Senior'))
    grade = models.CharField(
        max_length=1, choices=grade_choices)
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('OT', 'Other'),
    )
    gender = models.CharField(
        max_length=2, choices=gender_choices)
    race = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    # id = models.AutoField(primary_key = True)

    class Meta:
        db_table = 'demographics'


class generic_page(models.Model):
    generic_page_id = models.IntegerField()
    page = models.ForeignKey('pages', on_delete = models.CASCADE, related_name='generic_page1', db_column='page')
    body = models.TextField()
    version = models.IntegerField()

    class Meta:
        unique_together = ('generic_page_id', 'version')
        db_table = 'generic_page'

class issues(models.Model):
    scenario_id = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name = 'issues1', default = None, db_column='scenario_id')
    issue = models.IntegerField(default = None, primary_key = True, editable = False)
    name = models.CharField(max_length = 1000)
    importance_score = models.IntegerField(validators = [MinValueValidator(0.0)])
    class Meta:
        db_table = 'issues'


class pages(models.Model):
    page = models.IntegerField(unique = True)
    page_choices = (
        ('I', 'INTRO'),
        ('F', 'FEEDBACK'),
        ('G', 'GENERIC'),
        ('R', 'REFLECTION'),
        ('S', 'STAKEHOLDER'),
        ('A', 'ACTION'),
    )
    page_type = models.CharField(max_length=2, choices=page_choices)
    page_title = models.CharField(max_length=1000)
    scenario = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name='pages1', db_column='scenarios_id')
    version = models.IntegerField(default=1, editable=True)
    body = models.TextField(blank=True, null=True)
    id = models.AutoField(primary_key = True)
    next_id = models.ForeignKey('pages', on_delete = models.CASCADE, related_name='pages2', db_column='page')
    x_coordinate = models.IntegerField()
    y_coordinate = models.IntegerField()
    completed = models.BooleanField(default= False)

    class Meta:
        unique_together = ('page', 'version')
        db_table = 'pages'


class pages_to_scenario(models.Model):
    page_id = models.ForeignKey('pages', to_field = 'page', on_delete = models.CASCADE, related_name='stakeholder_page1')
    scenario_id = models.ForeignKey('scenarios', to_field = 'scenario_id', on_delete = models.CASCADE, related_name='stakeholder_page2')

    class Meta:
        unique_together = ('page_id', 'scenario_id')
        db_table = 'pages_to_scenario'


class professors(models.Model):
    professor = models.TextField(primary_key=True)
    fname = models.TextField()
    lname = models.TextField(blank=True)
    class Meta:
        db_table = 'professors'
    # courses = models.ManyToManyField( Courses, related_name='professor',  through='ProfessorsToCourses')



class professors_to_courses(models.Model):
    professor = models.ForeignKey(professors, on_delete = models.CASCADE, db_column='professor')
    course = models.ForeignKey(courses, on_delete = models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('professor', 'course')
        db_table = 'professors_to_courses'


class professors_to_scenario(models.Model):
    professor = models.ForeignKey('professors', on_delete = models.CASCADE, db_column='professor', related_name = "pts1")
    scenario = models.ForeignKey('scenarios', on_delete = models.CASCADE, db_column='scenario', related_name = "pts2")
    permission = models.IntegerField()
    id = models.AutoField(primary_key = True)

    class Meta:
        unique_together = ('professor', 'scenario')
        db_table = 'professors_to_scenario'


class questions(models.Model):
    question = models.IntegerField()
    version = models.IntegerField()
    points = models.IntegerField()
    question_text = models.TextField(blank=True)
    question_summary = models.TextField(blank=True)
    id = models.AutoField(primary_key = True)

    class Meta:
        unique_together = ('question', 'version')
        db_table = 'questions'

#pretty broken
class reflection_question_to_page(models.Model):
    reflection_question_id = models.ForeignKey('reflection_questions', to_field = 'id', on_delete = models.CASCADE)
    #page = models.ForeignKey(pages, on_delete = models.CASCADE, related_name = 'reflection_questions_to_page1', db_column = 'id')
    page_id = models.ForeignKey(pages, to_field = 'id', on_delete = models.CASCADE, related_name = 'reflection_questions_to_page1')
    class Meta:
        unique_together = ('reflection_question_id', 'page_id')
        db_table = 'reflection_question_to_page'


class reflection_questions(models.Model):
    reflection_question_id = models.IntegerField()
    reflection_question = models.TextField()
    version = models.IntegerField()
    id = models.AutoField(primary_key = True)

    class Meta:
        unique_together = ('reflection_question_id', 'version')
        db_table = 'reflection_questions'


class responses(models.Model):
    response_id = models.AutoField(primary_key=True)
    response = models.IntegerField()
    student = models.ForeignKey('students', on_delete = models.CASCADE, db_column='student', )
    scenario = models.ForeignKey('scenarios', on_delete = models.CASCADE, db_column='scenario', )
    version = models.IntegerField()
    page = models.ForeignKey(pages, on_delete = models.CASCADE, db_column='page', )
    course = models.ForeignKey(courses, on_delete = models.CASCADE, db_column='course', )
    date_taken = models.DateField(auto_now_add=True)
    choice = models.TextField()

    class Meta:
        unique_together = ('response', 'student', 'scenario', 'page', 'course', 'date_taken')
        db_table = 'responses'


class reflections_taken(models.Model):
    reflections = models.TextField(blank=True)
    response_id = models.OneToOneField('responses', on_delete = models.CASCADE, primary_key=True, db_column = 'response_id')

    class Meta:
        db_table = 'reflections_taken'


class response_to_action_page(models.Model):
    response_id = models.ForeignKey('responses', to_field = 'response_id', on_delete = models.CASCADE, )
    action_page = models.ForeignKey('action_page', to_field='id', on_delete = models.CASCADE )

    class Meta:
        unique_together = ('response_id', 'action_page')
        db_table = 'response_to_action_page'

class responses_to_conversations(models.Model):
    response_id = models.ForeignKey('responses', to_field = 'response_id', on_delete = models.CASCADE)
    stakeholder = models.ForeignKey('stakeholders', to_field = 'id', on_delete = models.CASCADE, db_column='stakeholder')
    stakeholder_version = models.IntegerField()
    score = models.DecimalField(max_digits=5, decimal_places=2)
    conversation = models.ForeignKey(conversations, on_delete = models.CASCADE, to_field='conversation')

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
    scenario_id = models.ForeignKey('scenarios', on_delete = models.CASCADE, db_column='scenario_id')
    version = models.IntegerField()
    course = models.ForeignKey('courses', on_delete = models.CASCADE, db_column='course')
    id = models.AutoField(primary_key = True)

    class Meta:
        unique_together = ('scenario_id', 'course')
        db_table = 'scenarios_for'


class stakeholder_to_page(models.Model):
    page = models.ForeignKey('pages', to_field = 'id', on_delete = models.CASCADE)
    stakeholder = models.ForeignKey('stakeholders', to_field = 'id', on_delete = models.CASCADE)

    class Meta:
        unique_together = ('page', 'stakeholder')
        db_table = 'stakeholder_to_page'


class stakeholders(models.Model):
    stakeholder = models.IntegerField()
    scenario = models.ForeignKey('scenarios', on_delete = models.CASCADE, db_column='scenario')
    version = models.IntegerField()
    name = models.TextField()
    description = models.TextField()
    job = models.TextField()
    introduction = models.TextField()
    enable_multi_convo = models.BooleanField()
    id = models.AutoField(primary_key = True)

    class Meta:
        unique_together = ('stakeholder', 'version')
        db_table = 'stakeholders'


class stakeholders_to_questions(models.Model):
    stakeholder = models.ForeignKey('stakeholders', to_field ='id', on_delete = models.CASCADE)
    question = models.ForeignKey('questions', to_field ='id', on_delete = models.CASCADE)

    class Meta:
        unique_together = ('stakeholder', 'question')
        db_table = 'stakeholders_to_questions'


class student_times(models.Model):
    student = models.ForeignKey('students', on_delete = models.CASCADE, db_column='student')
    course = models.ForeignKey('courses', on_delete = models.CASCADE, db_column='course')
    scenario_id = models.ForeignKey('scenarios', on_delete = models.CASCADE)
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
    student = models.ForeignKey('students', on_delete = models.CASCADE, db_column='student')
    course = models.ForeignKey('courses', on_delete = models.CASCADE, db_column='course')

    class Meta:
        unique_together = ('student', 'course')
        db_table = 'students_to_course'
