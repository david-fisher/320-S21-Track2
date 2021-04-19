from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

# Create your models here.
# Made everything uppercase or something

#scenarios is updated - 04/12/2021
class SCENARIOS(models.Model):
    class Meta:
        unique_together = (('SCENARIO'), ('VERSION'))
    SCENARIO = models.IntegerField(editable=True, unique = True)
    #TODO remove professors
    PROFESSOR = models.ForeignKey('PROFESSORS', to_field = 'PROFESSOR', on_delete =models.CASCADE, related_name="scenario_creator2", default = 1)
    VERSION = models.IntegerField(default=1, editable=True, unique = True)
    NAME = models.CharField(max_length = 1000)
    PUBLIC = models.BooleanField(default = False)
    NUM_CONVERSATION = models.IntegerField(default = 0)
    IS_FINISHED = models.BooleanField(default = False)
    DATE_CREATED = models.DateField(auto_now_add=True)

    SCENARIO_ID = models.AutoField(primary_key = True)

    # models.OneToOneField('pages', on_delete = models.CASCADE, related_name = "scenarios1", default = 1)
    # def __str__(self):
    #     return "%s the scenario" % self.name

#pages is updated - 04/12/2021
class PAGES(models.Model):
    class Meta:
        unique_together = (('PAGE'), ('VERSION'))
    PAGE = models.AutoField(primary_key= True)
    PAGE_CHOICES = (
        ('I', 'INTRO'),
        ('G', 'GENERIC'),
        ('R', 'REFLECTION'),
        ('S', 'STAKEHOLDER'),
        ('A', 'ACTION'),
    )
    PAGE_TYPE = models.CharField(max_length = 2, choices = PAGE_CHOICES)
    PAGE_TITLE = models.CharField(max_length = 1000)
    BODY = models.TextField(default = "default")
    SCENARIO = models.ForeignKey('SCENARIOS', to_field='SCENARIO_ID', on_delete = models.CASCADE, related_name="pages1")
    VERSION = models.IntegerField(default=1, editable=True, unique = True)
    NEXT_PAGE = models.ForeignKey('PAGES', to_field='PAGE', on_delete = models.CASCADE, related_name="pages2", unique= True)
    X_COORDINATE = models.IntegerField()
    Y_COORDINATE = models.IntegerField()
    NEXT_PAGE_VERSION = models.ForeignKey('PAGES', to_field='VERSION', on_delete = models.CASCADE, related_name="pages3", unique= True)

#updated on 4/12/2021
class REFLECTION_QUESTIONS(models.Model):
    class Meta:
        unique_together = (('VERSION'), ('ID'))
    #PAGE = models.ForeignKey('PAGES', to_field = 'PAGE', on_delete = models.CASCADE, related_name="reflection_questions1")
    REFLECTION_QUESTION = models.TextField(unique = True)
    ID = models.AutoField(primary_key = True, editable= False)
    VERSION = models.IntegerField(default= 1)

#updated on 4/12/2021
class REFLECTION_QUESTION_TO_PAGE(models.Model):
    class Meta:
        unique_together = (('PAGE_ID'), ('REFLECTION_QUESTION_VERSION'), ('REFLECTION_QUESTION_ID'), ('PAGE_VERSION'))
    PAGE_ID = models.ForeignKey('PAGES', to_field = 'PAGE', on_delete = models.CASCADE, related_name="reflection_questions_to_page1")
    REFLECTION_QUESTION_VERSION = models.ForeignKey('REFLECTION_QUESTIONS', to_field = 'REFLECTION_QUESTION', on_delete = models.CASCADE, related_name="reflection_questions_to_page2")
    REFLECTION_QUESTION_ID = models.ForeignKey('REFLECTION_QUESTIONS', to_field = 'ID', on_delete = models.CASCADE, related_name="reflection_questions_to_page3")
    PAGE_VERSION = models.ForeignKey('PAGES', to_field = 'VERSION', on_delete = models.CASCADE, related_name="reflection_questions_to_page4")

#updated on 4/12/2021
class GENERIC_PAGE(models.Model):
    class Meta:
        unique_together = (('ID'), ('VERSION'))
    PAGE = models.ForeignKey('PAGES', to_field= 'PAGE', on_delete = models.CASCADE, related_name="generic_page1", unique= True)
    BODY = models.TextField(default = True)
    ID = models.AutoField(editable = False, primary_key = True)
    VERSION = PAGE = models.ForeignKey('PAGES', to_field= 'VERSION', on_delete = models.CASCADE, related_name="generic_page2", unique= True)
    
#updated on 4/12/2021
class PAGES_TO_SCENARIO(models.Model):
    class Meta:
        unique_together = (('PAGE_ID'), ('SCENARIO_ID'), ('PAGE_VERSION'))
    PAGE_ID = models.ForeignKey('PAGES', to_field = 'PAGE', on_delete = models.CASCADE, related_name="stakeholder_page1", primary_key= True)
    SCENARIO_ID = models.ForeignKey('SCENARIOS', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name="stakeholder_page2")
    PAGE_VERSION = models.ForeignKey('PAGES', to_field = 'VERSION', on_delete = models.CASCADE, related_name="stakeholder_page3")
    SCENARIO_VERSION = models.ForeignKey('SCENARIOS', to_field = 'VERSION', on_delete = models.CASCADE, related_name="stakeholder_page4")

#updated 4/14
class STAKEHOLDER_TO_PAGE(models.Model):
    class Meta:
        unique_together = (('PAGE'), ('PAGE_VERSION'), ('STAKEHOLDER'), ('STAKEHOLDER_VERSION'))
    PAGE = models.ForeignKey('PAGES', to_field = "PAGE", on_delete = models.CASCADE, related_name="stakeholder_page5")
    PAGE_VERSION = models.ForeignKey('PAGES', to_field = "VERSION", on_delete = models.CASCADE, related_name="stakeholder_page7")
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', to_field = 'STAKEHOLDER', on_delete = models.CASCADE, related_name="stakeholder_page6")
    STAKEHOLDER_VERSION = models.ForeignKey('STAKEHOLDERS', to_field = 'VERSION', on_delete = models.CASCADE, related_name="stakeholder_page8")

# class choices_for(models.Model):
#     class Meta:
#         unique_together = (('SCENARIO_ID'), ('VERSION_ID'), ('CHOICES'))
#     SCENARIO_ID = models.ForeignKey('scenarios', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name="choices_for1")
#     VERSION_ID = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name="choices_for2")
#     CHOICES = models.TextField()

#updated 4/14
class STAKEHOLDERS(models.Model):
    class Meta:
        unique_together = (('STAKEHOLDER'), ('VERSION'))
    STAKEHOLDER = models.AutoField(primary_key = True, editable = False)
    SCENARIO = models.ForeignKey('SCENARIOS', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name="stakeholders1", default = 1)
    VERSION = models.IntegerField(default=1, editable=True)
    NAME = models.CharField(max_length = 1000, default = "default")
    DESCRIPTION = models.TextField(default = "default")
    JOB = models.TextField(default = "default")
    # MATRIX = ArrayField(ArrayField(models.IntegerField(), size = 15), size = 15)
    INTRODUCTION = models.TextField(default = 'default')
    ENABLE_MULTI_CONVO = models.BooleanField(default = False)

# class stakeholders_in(models.Model):
#     class Meta:
#         unique_together = (('STAKEHOLDER_ID'), ('SCENARIO_ID'))
#     STAKEHOLDER_ID = models.ForeignKey('stakeholders', on_delete = models.CASCADE, related_name="stakeholder1")
#     SCENARIO_ID = models.ForeignKey('scenarios', to_field = 'SCENARIO_ID', on_delete =models.CASCADE, related_name="stakeholder2")
    # VERSION_ID = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name="stakeholder3")

#updated 4/14
class CONVERSATIONS(models.Model):
    # class Meta:
    #     unique_together = (('STAKEHOLDER'), ('CONVERSATION'))
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', to_field = 'STAKEHOLDER', on_delete = models.CASCADE, related_name="conversations1")
    STAKEHOLDER_VERSION = models.ForeignKey('STAKEHOLDERS', to_field = 'VERSION', on_delete = models.CASCADE, related_name="conversations2")
    CONVERSATION = models.AutoField(default = None, primary_key = True)
    QUESTION = models.TextField(default = "default")
    RESPONSE = models.TextField(default = "default")

#updated 4/12 by Cooper (hope it works, if it doesnt then it was chirag)
class RESPONSES(models.Model):
    class Meta:
        unique_together = (('RESPONSE'), ('STUDENT'),('SCENARIO'),('PAGE'),('COURSE'),('DATE_TAKEN'))
    RESPONSE_ID = models.AutoField(primary_key = True, editable = False, default = None)
    RESPONSE = models.IntegerField()
    STUDENT = models.ForeignKey('STUDENTS', to_field= 'STUDENT', on_delete = models.CASCADE, related_name="responses1")
    PAGE = models.ForeignKey('PAGES', to_field= 'PAGE', on_delete = models.CASCADE, related_name="responses3")
    PAGE_VERSION = models.ForeignKey('PAGES', to_field = 'VERSION', on_delete = models.CASCADE, related_name="responses69")
    SCENARIO = models.ForeignKey('SCENARIOS', to_field= 'SCENARIO_ID', on_delete = models.CASCADE, related_name="responses2")
    VERSION = models.IntegerField(default=1, editable=True)
    COURSE = models.ForeignKey('COURSES', to_field= 'COURSE', on_delete = models.CASCADE, related_name="responses4")
    DATE_TAKEN = models.DateField(auto_now_add=True)
    CHOICE = models.TextField()

#Updated 4/12 by Cooper
class RESPONSES_TO_CONVERSATIONS(models.Model):
    class Meta:
        unique_together = (('RESPONSE_ID'), ('CONVERSATION'))
    RESPONSE_ID = models.ForeignKey('RESPONSES', to_field ='RESPONSE_ID', on_delete = models.CASCADE, related_name="responsesTC1")
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', to_field= 'STAKEHOLDER', on_delete = models.CASCADE, related_name="responsesTC2")
    STAKEHOLDER_VERSION = models.ForeignKey('STAKEHOLDERS', to_field = 'VERSION', on_delete = models.CASCADE, related_name="responsesTC69")
    SCORE = models.FloatField(validators = [MinValueValidator(0.0)])
    CONVERSATION = models.ForeignKey('CONVERSATIONS', to_field= 'CONVERSATION', on_delete = models.CASCADE, related_name="responsesTC3")

# class actions_taken(models.Model):
#     RESPONSE = models.ForeignKey('responses', on_delete = models.CASCADE, related_name="actions_taken1")
#     ACTION_PAGE = models.ForeignKey('action_page', on_delete = models.CASCADE, related_name="actions_taken2")

# class conversations_had(models.Model):
#     STUDENT = models.ForeignKey('students', on_delete = models.CASCADE, related_name="conversations_had1")
#     COURSE = models.ForeignKey('responses', on_delete = models.CASCADE, related_name="conversations_had2")
#     SCENARIO = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name="conversations_had3")
#     VERSION = models.IntegerField(default=1, editable=False)
#     DATE_TAKEN = models.ForeignKey('responses', on_delete = models.CASCADE, related_name="conversations_had5")
#     STAKEHOLDER = models.ForeignKey('stakeholders', on_delete = models.CASCADE, related_name="conversations_had6")
#     SCORE = models.IntegerField()
#     CONVERSATION = models.ForeignKey('conversations', on_delete = models.CASCADE, related_name="conversations_had7")

#Updated 4/12 by Cooper (Nothing actually changed just verified)
class REFLECTIONS_TAKEN(models.Model):
    # class Meta:
    #     unique_together = (('REFLECTIONS'), ('STUDENT'), ('COURSE'), ('SCENARIO'), ('VERSION'), ('DATE_TAKEN'))
    REFLECTIONS = models.TextField(default= 'default')
    RESPONSE_ID = models.ForeignKey('RESPONSES', to_field = 'RESPONSE_ID', on_delete = models.CASCADE, related_name="conversations_had5")
    # STUDENT = models.ForeignKey('students', on_delete = models.CASCADE, related_name="reflections_taken1")
    # COURSE = models.ForeignKey('responses', on_delete = models.CASCADE, related_name="reflections_taken2")
    # SCENARIO = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name="reflections_taken3")
    # VERSION = models.IntegerField(default=1, editable=False)
    # DATE_TAKEN = models.ForeignKey('responses', on_delete = models.CASCADE, related_name="reflections_taken5")
    # REFLECTION_PAGE = models.ForeignKey('pages',null = True, on_delete = models.CASCADE, related_name = 'reflections_taken6')

#Updated 4/12 by Cooper (just verified, nothing actually changed)
class COURSES(models.Model):
    COURSE = models.AutoField(default = None, primary_key = True)
    NAME = models.CharField(max_length = 1000)

#Updated 4/12 by Cooper (just verified, nothing actually changed)
class COURSES_TO_SCENARIO(models.Model):
    class Meta:
        unique_together = (('COURSE'), ('SCENARIO'))
    COURSE = models.ForeignKey('COURSES', to_field = 'COURSE', on_delete = models.CASCADE, related_name="reflections_taken1", primary_key= True)
    SCENARIO = models.ForeignKey('SCENARIOS', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name="reflections_taken2")
    PERMISSION = models.IntegerField()

#Updated 4/12 by Cooper (just verified, nothing actually changed)
class SCENARIOS_FOR(models.Model):
    class Meta:
        unique_together = (('SCENARIO_ID'), ('COURSE'))
    SCENARIO_ID = models.ForeignKey('SCENARIOS', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name='scenarios_for1', primary_key= True)
    COURSE = models.ForeignKey('COURSES', to_field = 'COURSE', on_delete = models.CASCADE, related_name='scenarios_for2')
    VERSION = models.IntegerField(default=1, editable=True)

#updated according to schema: 4/12/2021
class STUDENTS(models.Model):
    STUDENT = models.IntegerField(primary_key = True)
    FNAME = models.CharField(max_length = 100, default= "default")
    LNAME = models.CharField(max_length = 100, default= "default")

#Updated 4/12 by Cooper (just verified, nothing actually changed)
class DEMOGRAPHICS(models.Model):
    STUDENT = models.ForeignKey('STUDENTS',to_field = 'STUDENT', on_delete = models.CASCADE, related_name = "demographics", primary_key = True)
    AGE = models.SmallIntegerField()
    GRADE = models.CharField(max_length = 10, default = "default")
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('OT', 'OTHER'),
    )
    GENDER = models.CharField(max_length = 2, choices = GENDER_CHOICES)
    RACE = models.CharField(max_length = 50)
    MAJOR = models.CharField(max_length = 100)

#Updated 4/12 by Cooper (just verified, nothing actually changed)
class STUDENTS_TO_COURSE(models.Model):
    class Meta:
        unique_together = (('STUDENT'), ('COURSE'))
    STUDENT = models.ForeignKey('STUDENTS', to_field = 'STUDENT', on_delete = models.CASCADE, related_name="students_to_course1", primary_key= True)
    COURSE = models.ForeignKey('COURSES', to_field = 'COURSE', on_delete = models.CASCADE, related_name="students_to_couse2")

#Updated 4/12 by Cooper (just verified, nothing actually changed)
class PROFESSORS_TO_COURSES(models.Model):
    class Meta:
        unique_together = (('PROFESSOR'), ('COURSE'))    
    PROFESSOR = models.ForeignKey('PROFESSORS', to_field = 'PROFESSOR', on_delete = models.CASCADE, related_name="professors_to_courses1", primary_key= True)
    COURSE = models.ForeignKey('COURSES', to_field = 'COURSE', on_delete = models.CASCADE, related_name="professors_to_courses2")

#Updated 4/12 by Cooper (just verified, nothing actually changed)
class PROFESSORS(models.Model):
    # class Meta:
    #    unique_together = (('PROFESSOR_ID'), ('NAME'))
    PROFESSOR = models.IntegerField(primary_key = True)
    FNAME = models.CharField(max_length = 1000, default= "default")
    LNAME = models.CharField(max_length = 1000, default= "default")

#Updated 4/12 by Cooper (just verified, nothing actually changed)
class PROFESSORS_TO_SCENARIO(models.Model):
    class Meta:
        unique_together = (('PROFESSOR'), ('SCENARIO'))
    PROFESSOR = models.ForeignKey('PROFESSORS', to_field = 'PROFESSOR', on_delete = models.CASCADE, related_name="professors_to_scenario1", primary_key= True)
    SCENARIO = models.ForeignKey('SCENARIOS', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name="professors_to_scenario2")
    PERMISSION = models.IntegerField()

#updated 4/14
class ISSUES(models.Model):
    # class Meta:
    #     unique_together = (('SCENARIO'),('ISSUE'),('VERSION'))
    SCENARIO_ID = models.ForeignKey('SCENARIOS', to_field= 'SCENARIO_ID', on_delete = models.CASCADE, related_name = "scenario_id1", default = None)
    ISSUE = models.AutoField(default = None, primary_key = True, editable = False)
    # VERSION = models.IntegerField(default=1, editable=False)
    NAME = models.CharField(max_length = 1000)
    IMPORTANCE_SCORE = models.IntegerField(validators = [MinValueValidator(0.0)])

#updated 4/14
class COVERAGE(models.Model):
    class Meta:
        unique_together = (('STAKEHOLDER'),('ISSUE'))
    STAKEHOLDER = models.ForeignKey('STAKEHOLDERS', to_field = 'STAKEHOLDER', on_delete = models.CASCADE, related_name = "coverage2", default = None, primary_key = True)
    STAKEHOLDER_VERSION = models.ForeignKey('STAKEHOLDERS', to_field = 'VERSION', on_delete=models.CASCADE, related_name = "coverage4")
    ISSUE = models.ForeignKey('ISSUES', to_field = 'ISSUE', on_delete = models.CASCADE, related_name = "coverage1", default = None)
    # VERSION_ID = models.ForeignKey('stakeholders',on_delete = models.CASCADE, related_name = "coverage3", default = None)
    COVERAGE_SCORE = models.FloatField(validators = [MinValueValidator(0.0)])

# action page updated - 04/12/2021
class ACTION_PAGE(models.Model):
    class Meta:
        unique_together = (('PAGE'),('CHOICE'), ('ID'), ('RESULT_PAGE'))
    PAGE = models.ForeignKey('PAGES', to_field = 'PAGE', on_delete = models.CASCADE, related_name = 'action_page1')
    CHOICE = models.TextField(default = 'default')
    RESULT_PAGE = models.IntegerField(null=True)
    ID = models.AutoField(primary_key = True)
    VERSION = models.ForeignKey('PAGES', to_field = 'VERSION', on_delete = models.CASCADE, related_name = 'action_page2')
    
#Updated 4/12
class RESPONSE_TO_ACTION_PAGE(models.Model):

    RESPONSE_ID = models.ForeignKey('RESPONSES', to_field = 'RESPONSE_ID', on_delete = models.CASCADE, related_name = 'action_page2')
    ACTION_PAGE = models.ForeignKey('ACTION_PAGE', to_field = 'ID', on_delete = models.CASCADE, related_name = 'action_page3')
    ACTION_PAGE_VERSION = models.ForeignKey('ACTION_PAGE', to_field='VERSION', on_delete=models.CASCADE, related_name = 'action_page4')

# class assigned_to(models.Model):
#     class Meta:
#         unique_together = (('STUDENT'),('SCENARIO'),('VERSION'))
#     STUDENT = models.ForeignKey('students', on_delete = models.CASCADE, related_name="assigned_to1")
#     SCENARIO = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name="assigned_to2")
#     VERSION = models.IntegerField(default=1, editable=False)

#done - Chirag - 04/12/2021
class STUDENT_TIMES(models.Model):
    class Meta:
        unique_together = (('STUDENT'),('SCENARIO_ID'),('COURSE'),('DATE_TAKEN'),('PAGE'))
    STUDENT = models.ForeignKey('STUDENTS', to_field = 'STUDENT', on_delete = models.CASCADE, related_name="student_times1")
    SCENARIO_ID = models.ForeignKey('SCENARIOS', to_field= 'SCENARIO_ID', on_delete = models.CASCADE, related_name="student_times2")
    
    COURSE = models.ForeignKey('COURSES', to_field = 'COURSE', on_delete = models.CASCADE,related_name = "student_times3")
    DATE_TAKEN = models.DateField(auto_now_add=True)
    PAGE = models.IntegerField()
    START_TIME = models.DateField(null = True)
    END_TIME = models.DateField(null = True)

#questions is complete - 04/12/2021
class QUESTIONS(models.Model):
    class Meta:
        unique_together = (('QUESTION'),('QUESTION_VERSION'))
    QUESTION = models.AutoField(primary_key= True)
    VERSION = models.IntegerField(default = 1)
    POINTS = models.IntegerField(default = 1)
    QUESTION_TEXT = models.TextField(default = 'default')
    QUESTION_SUMMARY = models.TextField(default = 'default')


"""class scenario_creator(models.Model):
    SCENARIO = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name="scenario_creator1")
    PROFESSOR = models.ForeignKey('professors', to_field = 'PROFESSOR', on_delete =models.CASCADE, related_name="scenario_creator2", default = 1)"""
