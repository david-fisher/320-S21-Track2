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
        'Scenarios', related_name='courses',  through='ScenariosFor')

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
        ('F', 'FEEDBACK'),
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


class PROFESSORS_TO_COURSES(models.Model):
    PROFESSOR = models.ForeignKey(PROFESSORS, on_delete = models.CASCADE, db_column='professor')
    COURSE = models.ForeignKey(COURSES, on_delete = models.CASCADE, db_column='course')

    class Meta:
        db_table = 'professors_to_courses'
        unique_together = ('PROFESSOR', 'COURSE')


class PROFESSORS_TO_SCENARIO(models.Model):
    PROFESSOR = models.ForeignKey(PROFESSORS, on_delete = models.CASCADE, db_column='professor')
    SCENARIO = models.ForeignKey('SCENARIOS', on_delete = models.CASCADE, db_column='scenario')
    PERMISSION = models.IntegerField()

    class Meta:
        db_table = 'professors_to_scenario'
        unique_together = ('PROFESSOR', 'SCENARIO')


class QUESTIONS(models.Model):
    QUESTION = models.IntegerField()
    VERSION = models.IntegerField()
    POINTS = models.IntegerField()
    QUESTION_TEXT = models.TextField(blank=True)
    QUESTION_SUMMARY = models.TextField(blank=True)

    class Meta:
        db_table = 'questions'
        unique_together = ('QUESTION', 'VERSION')


class REFLECTION_QUESTION_TO_PAGE(models.Model):
    REFLECTION_QUESTION_ID = models.ForeignKey('REFLECTION_QUESTIONS', on_delete = models.CASCADE)
    PAGE = models.ForeignKey(PAGES, on_delete = models.CASCADE)

    class Meta:
        db_table = 'reflection_question_to_page'
        unique_together = ('REFLECTION_QUESTION_ID', 'PAGE')


class REFLECTION_QUESTIONS(models.Model):
    REFLECTION_QUESTION_ID = models.IntegerField()
    REFLECTION_QUESTION = models.TextField()
    VERSION = models.IntegerField()

    class Meta:
        db_table = 'reflection_questions'
        unique_together = ('REFLECTION_QUESTION_ID', 'VERSION')


class REFLECTIONS_TAKEN(models.Model):
    REFLECTIONS = models.TextField(blank=True)
    RESPONSE_ID = models.OneToOneField('RESPONSES', on_delete = models.CASCADE, primary_key=True)


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
        db_table = 'responses'
        unique_together = ('RESPONSE', 'STUDENT', 'SCENARIO', 'PAGE', 'COURSE', 'DATE_TAKEN')

class RESPONSE_TO_ACTION_PAGE(models.Model):
    RESPONSE_ID = models.ForeignKey('RESPONSES', on_delete = models.CASCADE, )
    ACTION_PAGE = models.ForeignKey(ACTION_PAGE, on_delete = models.CASCADE, db_column='action_page', )

    class Meta:
        db_table = 'response_to_action_page'
        unique_together = ('RESPONSE', 'ACTION_PAGE')

class RESPONSES_TO_CONVERSATIONS(models.Model):
    RESPONSE_ID = models.ForeignKey(RESPONSES, on_delete = models.CASCADE)
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', on_delete = models.CASCADE, db_column='stakeholder')
    STAKEHOLDER_VERSION = models.IntegerField()
    SCORE = models.DecimalField(max_digits=5, decimal_places=2)
    CONVERSATION = models.ForeignKey(CONVERSATIONS, on_delete = models.CASCADE, db_column='conversation')

    class Meta:
        db_table = 'responses_to_conversations'
        unique_together = ('RESPONSE', 'CONVERSATION')


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
        db_table = 'scenarios'
        unique_together = ('SCENARIO', 'VERSION')


class SCENARIOS_FOR(models.Model):
    SCENARIO = models.ForeignKey(SCENARIOS, on_delete = models.CASCADE)
    VERSION = models.IntegerField()
    COURSE = models.ForeignKey(COURSES, on_delete = models.CASCADE, db_column='course')

    class Meta:
        db_table = 'scenarios_for'
        unique_together = ('SCENARIO', 'COURSE')


class STAKEHOLDER_TO_PAGE(models.Model):
    PAGE = models.ForeignKey(PAGES, on_delete = models.CASCADE, db_column='page')
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', on_delete = models.CASCADE, db_column='stakeholder')

    class Meta:
        db_table = 'stakeholder_to_page'
        unique_together = ('PAGE', 'STAKEHOLDER')


class STAKEHOLDERS(models.Model):
    STAKEHOLDER = models.IntegerField()
    SCENARIO = models.ForeignKey(SCENARIOS, on_delete = models.CASCADE, db_column='scenario')
    VERSION = models.IntegerField()
    NAME = models.TextField()
    DESCRIPTION = models.TextField()
    JOB = models.TextField()
    INTRODUCTION = models.TextField()
    ENABLE_MULTI_CONVO = models.BooleanField()

    class Meta:
        db_table = 'stakeholders'
        unique_together = ('STAKEHOLDER', 'VERSION')


class STAKEHOLDERS_TO_QUESTIONS(models.Model):
    STAKEHOLDER = models.ForeignKey(STAKEHOLDERS, on_delete = models.CASCADE, db_column='stakeholder')
    QUESTION = models.ForeignKey(QUESTIONS, on_delete = models.CASCADE, db_column='question')

    class Meta:
        db_table = 'stakeholders_to_questions'
        unique_together = ('STAKEHOLDER', 'QUESTION')


class STUDENT_TIMES(models.Model):
    STUDENT = models.ForeignKey('STUDENTS', on_delete = models.CASCADE, db_column='student')
    COURSE = models.ForeignKey(COURSES, on_delete = models.CASCADE, db_column='course')
    SCENARIO_ID = models.ForeignKey(SCENARIOS, on_delete = models.CASCADE)
    DATE_TAKEN = models.DateField(auto_now = True)
    PAGE = models.IntegerField()
    START_TIME = models.DateField(auto_now_add = True)
    END_TIME = models.DateField(null = True, blank=True)

    class Meta:
        db_table = 'student_times'
        unique_together = ('STUDENT', 'COURSE', 'SCENARIO')


class STUDENTS(models.Model):
    STUDENT = models.TextField(primary_key=True)
    FNAME = models.TextField()
    LNAME = models.TextField()


class STUDENTS_TO_COURSE(models.Model):
    STUDENT = models.ForeignKey(STUDENTS, on_delete = models.CASCADE, db_column='student')
    COURSE = models.ForeignKey(COURSES, on_delete = models.CASCADE, db_column='course')

    class Meta:
        db_table = 'students_to_course'
        unique_together = ('STUDENT', 'COURSE')