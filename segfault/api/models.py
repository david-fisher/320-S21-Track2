# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ActionPage(models.Model):
    action_page_id = models.IntegerField(blank=True, null=True)
    page = models.ForeignKey('Pages', models.DO_NOTHING, db_column='page', blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    choice = models.TextField(blank=True, null=True)
    result_page = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'action_page'
        unique_together = (('action_page_id', 'version'),)


class Conversations(models.Model):
    conversation = models.IntegerField(primary_key=True)
    stakeholder = models.ForeignKey('Stakeholders', models.DO_NOTHING, db_column='stakeholder', blank=True, null=True)
    question = models.TextField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conversations'


class Courses(models.Model):
    course = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses'


class CoursesToScenario(models.Model):
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_column='course', blank=True, null=True)
    scenario = models.ForeignKey('Scenarios', models.DO_NOTHING, db_column='scenario', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'courses_to_scenario'
        unique_together = (('course', 'scenario'),)


class Coverage(models.Model):
    stakeholder = models.ForeignKey('Stakeholders', models.DO_NOTHING, db_column='stakeholder', blank=True, null=True)
    issue = models.ForeignKey('Issues', models.DO_NOTHING, db_column='issue', blank=True, null=True)
    coverage_score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'coverage'
        unique_together = (('stakeholder', 'issue'),)


class Demographics(models.Model):
    student = models.OneToOneField('Students', models.DO_NOTHING, db_column='student', primary_key=True)
    age = models.IntegerField(blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    race = models.TextField(blank=True, null=True)
    major = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'demographics'


class GenericPage(models.Model):
    generic_page_id = models.IntegerField(blank=True, null=True)
    page = models.ForeignKey('Pages', models.DO_NOTHING, db_column='page', blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'generic_page'
        unique_together = (('generic_page_id', 'version'),)


class Issues(models.Model):
    issue = models.IntegerField(primary_key=True)
    scenario = models.ForeignKey('Scenarios', models.DO_NOTHING, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    importance_score = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'issues'


class Pages(models.Model):
    page = models.IntegerField(blank=True, null=True)
    page_type = models.TextField(blank=True, null=True)
    page_title = models.TextField(blank=True, null=True)
    scenario = models.ForeignKey('Scenarios', models.DO_NOTHING, db_column='scenario', blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    next = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    x_coordinate = models.IntegerField(blank=True, null=True)
    y_coordinate = models.IntegerField(blank=True, null=True)
    completed = models.BooleanField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pages'
        unique_together = (('page', 'version'),)


class PagesToScenario(models.Model):
    page = models.ForeignKey(Pages, models.DO_NOTHING, blank=True, null=True)
    scenario = models.ForeignKey('Scenarios', models.DO_NOTHING, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'pages_to_scenario'
        unique_together = (('page', 'scenario'),)


class Professors(models.Model):
    professor = models.TextField(primary_key=True)
    fname = models.TextField(blank=True, null=True)
    lname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'professors'


class ProfessorsToCourses(models.Model):
    professor = models.ForeignKey(Professors, models.DO_NOTHING, db_column='professor', blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_column='course', blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'professors_to_courses'
        unique_together = (('professor', 'course'),)


class ProfessorsToScenario(models.Model):
    professor = models.ForeignKey(Professors, models.DO_NOTHING, db_column='professor', blank=True, null=True)
    scenario = models.ForeignKey('Scenarios', models.DO_NOTHING, db_column='scenario', blank=True, null=True)
    permission = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'professors_to_scenario'
        unique_together = (('professor', 'scenario'),)


class Questions(models.Model):
    question = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    question_text = models.TextField(blank=True, null=True)
    question_summary = models.TextField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'questions'
        unique_together = (('question', 'version'),)


class ReflectionQuestionToPage(models.Model):
    reflection_question = models.ForeignKey('ReflectionQuestions', models.DO_NOTHING, blank=True, null=True)
    page = models.ForeignKey(Pages, models.DO_NOTHING, blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'reflection_question_to_page'
        unique_together = (('reflection_question', 'page'),)


class ReflectionQuestions(models.Model):
    reflection_question_id = models.IntegerField(blank=True, null=True)
    reflection_question = models.TextField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'reflection_questions'
        unique_together = (('reflection_question_id', 'version'),)


class ReflectionsTaken(models.Model):
    reflections = models.TextField(blank=True, null=True)
    response = models.OneToOneField('Responses', models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'reflections_taken'


class ResponseToActionPage(models.Model):
    response = models.ForeignKey('Responses', models.DO_NOTHING, blank=True, null=True)
    action_page = models.ForeignKey(ActionPage, models.DO_NOTHING, db_column='action_page', blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'response_to_action_page'


class Responses(models.Model):
    response_id = models.IntegerField(primary_key=True)
    response = models.IntegerField(blank=True, null=True)
    student = models.ForeignKey('Students', models.DO_NOTHING, db_column='student', blank=True, null=True)
    scenario = models.ForeignKey('Scenarios', models.DO_NOTHING, db_column='scenario', blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    page = models.ForeignKey(Pages, models.DO_NOTHING, db_column='page', blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_column='course', blank=True, null=True)
    date_taken = models.DateField(blank=True, null=True)
    choice = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'responses'
        unique_together = (('response', 'student', 'scenario', 'page', 'course', 'date_taken'),)


class ResponsesToConversations(models.Model):
    response = models.ForeignKey(Responses, models.DO_NOTHING, blank=True, null=True)
    stakeholder = models.ForeignKey('Stakeholders', models.DO_NOTHING, db_column='stakeholder', blank=True, null=True)
    stakeholder_version = models.IntegerField(blank=True, null=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    conversation = models.ForeignKey(Conversations, models.DO_NOTHING, db_column='conversation', blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'responses_to_conversations'
        unique_together = (('response', 'conversation'),)


class Scenarios(models.Model):
    scenario = models.IntegerField(blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    public = models.BooleanField(blank=True, null=True)
    num_conversation = models.IntegerField(blank=True, null=True)
    is_finished = models.BooleanField(blank=True, null=True)
    date_created = models.DateField(blank=True, null=True)
    scenario_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scenarios'
        unique_together = (('scenario', 'version'),)


class ScenariosFor(models.Model):
    scenario = models.ForeignKey(Scenarios, models.DO_NOTHING, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_column='course', blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'scenarios_for'
        unique_together = (('scenario', 'course'),)


class StakeholderToPage(models.Model):
    page = models.ForeignKey(Pages, models.DO_NOTHING, db_column='page', blank=True, null=True)
    stakeholder = models.ForeignKey('Stakeholders', models.DO_NOTHING, db_column='stakeholder', blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'stakeholder_to_page'
        unique_together = (('page', 'stakeholder'),)


class Stakeholders(models.Model):
    stakeholder = models.IntegerField(blank=True, null=True)
    scenario = models.ForeignKey(Scenarios, models.DO_NOTHING, db_column='scenario', blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    job = models.TextField(blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    enable_multi_convo = models.BooleanField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'stakeholders'
        unique_together = (('stakeholder', 'version'),)


class StakeholdersToQuestions(models.Model):
    stakeholder = models.ForeignKey(Stakeholders, models.DO_NOTHING, db_column='stakeholder', blank=True, null=True)
    question = models.ForeignKey(Questions, models.DO_NOTHING, db_column='question', blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'stakeholders_to_questions'
        unique_together = (('stakeholder', 'question'),)


class StudentTimes(models.Model):
    student = models.ForeignKey('Students', models.DO_NOTHING, db_column='student', blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_column='course', blank=True, null=True)
    scenario = models.ForeignKey(Scenarios, models.DO_NOTHING, blank=True, null=True)
    date_taken = models.DateField(blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    start_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'student_times'
        unique_together = (('student', 'course', 'scenario', 'date_taken', 'page'),)


class Students(models.Model):
    student = models.TextField(primary_key=True)
    fname = models.TextField(blank=True, null=True)
    lname = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'students'


class StudentsToCourse(models.Model):
    student = models.ForeignKey(Students, models.DO_NOTHING, db_column='student', blank=True, null=True)
    course = models.ForeignKey(Courses, models.DO_NOTHING, db_column='course', blank=True, null=True)
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'students_to_course'
        unique_together = (('student', 'course'),)
