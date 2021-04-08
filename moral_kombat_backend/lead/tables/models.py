from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MinValueValidator

# Create your models here.

class scenarios(models.Model):
    class Meta:
        unique_together = (('SCENARIO'), ('VERSION'))
    SCENARIO = models.IntegerField(editable=True, unique = True)
    #TODO remove professors
    PROFESSOR = models.ForeignKey('professors', to_field = 'PROFESSOR', on_delete =models.CASCADE, related_name="scenario_creator2", default = 1)
    VERSION = models.IntegerField(default=1, editable=True, unique = True)
    NAME = models.CharField(max_length = 1000)
    PUBLIC = models.BooleanField(default = False)
    NUM_CONVERSATION = models.IntegerField(default = 0)
    IS_FINISHED = models.BooleanField(default = False)
    DATE_CREATED = models.DateField(auto_now_add=True)

    SCENARIO_ID = models.IntegerField(primary_key = True, editable=True)

    # models.OneToOneField('pages', on_delete = models.CASCADE, related_name = "scenarios1", default = 1)
    # def __str__(self):
    #     return "%s the scenario" % self.name


class pages(models.Model):
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
    SCENARIO = models.ForeignKey('scenarios', to_field='SCENARIO_ID', on_delete = models.CASCADE, related_name="pages1")
    VERSION = models.IntegerField(default=1, editable=True, unique = True)
    NEXT_PAGE = models.ForeignKey('pages', to_field='PAGE', on_delete = models.CASCADE, related_name="pages2", unique= True)
    X_COORDINATE = models.IntegerField()
    Y_COORDINATE = models.IntegerField()



class reflection_questions(models.Model):
    class Meta:
        unique_together = (('PAGE'), ('REFLECTION_QUESTION'), ('id'))
    PAGE = models.ForeignKey('pages', to_field = 'PAGE', on_delete = models.CASCADE, related_name="reflection_questions1")
    REFLECTION_QUESTION = models.TextField(unique = True)
    id = models.AutoField(primary_key = True, editable= False)
    VERSION = models.IntegerField(default= 1)

class reflection_question_to_page(models.Model):
    class Meta:
        unique_together = (('page_id'), ('reflection_question_version'), ('reflection_question_id'), ('page_version'))
    page_id = models.ForeignKey('pages', to_field = 'PAGE', on_delete = models.CASCADE, related_name="reflection_questions_to_page1")
    reflection_question_version = models.ForeignKey('reflection_questions', to_field = 'REFLECTION_QUESTION', on_delete = models.CASCADE, related_name="reflection_questions_to_page2")
    reflection_question_id = models.ForeignKey('reflection_questions', to_field = 'id', on_delete = models.CASCADE, related_name="reflection_questions_to_page3")
    page_version = models.ForeignKey('pages', to_field = 'VERSION', on_delete = models.CASCADE, related_name="reflection_questions_to_page4")

class generic_page(models.Model):
    class Meta:
        unique_together = (('PAGE'), ('BODY'), ('id'), ('VERSION'))
    PAGE = models.ForeignKey('pages', to_field= 'PAGE', on_delete = models.CASCADE, related_name="generic_page1", unique= True)
    BODY = models.TextField()
    id = models.AutoField(editable = False, primary_key = True)
    VERSION = models.IntegerField(default = 1)
    

class pages_to_scenario(models.Model):
    class Meta:
        unique_together = (('page_id'), ('scenario_id'), ('page_version'), ('scenario_version'))
    page_id = models.ForeignKey('pages', to_field = 'PAGE', on_delete = models.CASCADE, related_name="stakeholder_page1", primary_key= True)
    scenario_id = models.ForeignKey('scenarios', to_field = 'SCENARIO', on_delete = models.CASCADE, related_name="stakeholder_page2")
    page_version = models.ForeignKey('pages', to_field = 'VERSION', on_delete = models.CASCADE, related_name="stakeholder_page3")
    scenario_version = models.ForeignKey('scenarios', to_field = 'VERSION', on_delete = models.CASCADE, related_name="stakeholder_page4")

class stakeholder_to_page(models.Model):
    class Meta:
        unique_together = (('PAGE'), ('STAKEHOLDER'))
    PAGE = models.ForeignKey('pages', to_field = "PAGE", on_delete = models.CASCADE, related_name="stakeholder_page5")
    STAKEHOLDER = models.ForeignKey('stakeholders', to_field = 'STAKEHOLDER', on_delete = models.CASCADE, related_name="stakeholder_page6")


# class choices_for(models.Model):
#     class Meta:
#         unique_together = (('SCENARIO_ID'), ('VERSION_ID'), ('CHOICES'))
#     SCENARIO_ID = models.ForeignKey('scenarios', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name="choices_for1")
#     VERSION_ID = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name="choices_for2")
#     CHOICES = models.TextField()



class stakeholders(models.Model):
    class Meta:
        unique_together = (('STAKEHOLDER'), ('VERSION'))
    STAKEHOLDER = models.AutoField(primary_key = True, editable = False)
    SCENARIO = models.ForeignKey('scenarios', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name="stakeholders1", default = 1)
    VERSION = models.IntegerField(default=1, editable=True)
    NAME = models.CharField(max_length = 1000, default = "default")
    DESCRIPTION = models.TextField(default = "default")
    JOB = models.TextField(default = "default")
    # MATRIX = ArrayField(ArrayField(models.IntegerField(), size = 15), size = 15)
    INTRODUCTION = models.TextField(default = 'default')



# class stakeholders_in(models.Model):
#     class Meta:
#         unique_together = (('STAKEHOLDER_ID'), ('SCENARIO_ID'))
#     STAKEHOLDER_ID = models.ForeignKey('stakeholders', on_delete = models.CASCADE, related_name="stakeholder1")
#     SCENARIO_ID = models.ForeignKey('scenarios', to_field = 'SCENARIO_ID', on_delete =models.CASCADE, related_name="stakeholder2")
    # VERSION_ID = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name="stakeholder3")



class conversations(models.Model):
    # class Meta:
    #     unique_together = (('STAKEHOLDER'), ('CONVERSATION'))
    STAKEHOLDER = models.ForeignKey('stakeholders', to_field = 'STAKEHOLDER', on_delete = models.CASCADE, related_name="conversations1")
    CONVERSATION = models.AutoField(default = None, primary_key = True)
    QUESTION = models.TextField(default = "default")
    RESPONSE = models.TextField(default = "default")


class responses(models.Model):
    class Meta:
        unique_together = (('RESPONSE'), ('STUDENT'),('SCENARIO'),('PAGE'),('COURSE'),('DATE_TAKEN'))
    RESPONSE_ID = models.AutoField(primary_key = True, editable = False, default = None)
    RESPONSE = models.IntegerField()
    CHOICE = models.TextField()
    STUDENT = models.ForeignKey('students', to_field= 'STUDENT', on_delete = models.CASCADE, related_name="responses1")
    PAGE = models.ForeignKey('pages', to_field= 'PAGE', on_delete = models.CASCADE, related_name="responses3")
    SCENARIO = models.ForeignKey('scenarios', to_field= 'SCENARIO_ID', on_delete = models.CASCADE, related_name="responses2")
    VERSION = models.IntegerField(default=1, editable=True)
    COURSE = models.ForeignKey('courses', to_field= 'COURSE', on_delete = models.CASCADE, related_name="responses4")
    DATE_TAKEN = models.DateField(auto_now_add=True)

class responses_to_conversations(models.Model):
    class Meta:
        unique_together = (('RESPONSE_ID'), ('CONVERSATION'))
    RESPONSE_ID = models.ForeignKey('responses', to_field ='RESPONSE_ID', on_delete = models.CASCADE, related_name="responsesTC1")
    STAKEHOLDER = models.ForeignKey('stakeholders', to_field= 'STAKEHOLDER', on_delete = models.CASCADE, related_name="responsesTC2")
    SCORE = models.FloatField(validators = [MinValueValidator(0.0)])
    CONVERSATION = models.ForeignKey('conversations', to_field= 'CONVERSATION', on_delete = models.CASCADE, related_name="responsesTC3")

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



class reflections_taken(models.Model):
    # class Meta:
    #     unique_together = (('REFLECTIONS'), ('STUDENT'), ('COURSE'), ('SCENARIO'), ('VERSION'), ('DATE_TAKEN'))
    REFLECTIONS = models.TextField(default= 'default')
    RESPONSE_ID = models.ForeignKey('responses', to_field = 'RESPONSE_ID', on_delete = models.CASCADE, related_name="conversations_had5")
    # STUDENT = models.ForeignKey('students', on_delete = models.CASCADE, related_name="reflections_taken1")
    # COURSE = models.ForeignKey('responses', on_delete = models.CASCADE, related_name="reflections_taken2")
    # SCENARIO = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name="reflections_taken3")
    # VERSION = models.IntegerField(default=1, editable=False)
    # DATE_TAKEN = models.ForeignKey('responses', on_delete = models.CASCADE, related_name="reflections_taken5")
    # REFLECTION_PAGE = models.ForeignKey('pages',null = True, on_delete = models.CASCADE, related_name = 'reflections_taken6')



class courses(models.Model):
    COURSE = models.AutoField(default = None, primary_key = True)
    NAME = models.CharField(max_length = 1000)

class courses_to_scenario(models.Model):
    class Meta:
        unique_together = (('COURSE'), ('SCENARIO'))
    COURSE = models.ForeignKey('courses', to_field = 'COURSE', on_delete = models.CASCADE, related_name="reflections_taken1", primary_key= True)
    SCENARIO = models.ForeignKey('scenarios', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name="reflections_taken2")
    PERMISSION = models.IntegerField()


class scenarios_for(models.Model):
    class Meta:
        unique_together = (('SCENARIO_ID'), ('COURSE'))
    SCENARIO_ID = models.ForeignKey('scenarios', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name='scenarios_for1', primary_key= True)
    COURSE = models.ForeignKey('courses', to_field = 'COURSE', on_delete = models.CASCADE, related_name='scenarios_for2')
    VERSION = models.IntegerField(default=1, editable=True)


class students(models.Model):
    STUDENT = models.IntegerField(primary_key = True)
    FNAME = models.CharField(max_length = 100, default= "default")
    LNAME = models.CharField(max_length = 100, default= "default")

class demographics(models.Model):
    STUDENT = models.ForeignKey('students',to_field = 'STUDENT', on_delete = models.CASCADE, related_name = "demographics", primary_key = True)
    AGE = models.SmallIntegerField()
    GRADE = models.IntegerField()
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('OT', 'OTHER'),
    )
    GENDER = models.CharField(max_length = 2, choices = GENDER_CHOICES)
    RACE = models.CharField(max_length = 50)
    MAJOR = models.CharField(max_length = 100)


class students_to_course(models.Model):
    class Meta:
        unique_together = (('STUDENT'), ('COURSE'))
    STUDENT = models.ForeignKey('students', to_field = 'STUDENT', on_delete = models.CASCADE, related_name="students_to_course1", primary_key= True)
    COURSE = models.ForeignKey('courses', to_field = 'COURSE', on_delete = models.CASCADE, related_name="students_to_couse2")

class professors_to_courses(models.Model):
    class Meta:
        unique_together = (('PROFESSOR'), ('COURSE'))    
    PROFESSOR = models.ForeignKey('professors', to_field = 'PROFESSOR', on_delete = models.CASCADE, related_name="professors_to_courses1", primary_key= True)
    COURSE = models.ForeignKey('courses', to_field = 'COURSE', on_delete = models.CASCADE, related_name="professors_to_courses2")

class professors(models.Model):
    # class Meta:
    #    unique_together = (('PROFESSOR_ID'), ('NAME'))
    PROFESSOR = models.IntegerField(primary_key = True)
    FNAME = models.CharField(max_length = 1000, default= "default")
    LNAME = models.CharField(max_length = 1000, default= "default")

class professors_to_scenario(models.Model):
    class Meta:
        unique_together = (('PROFESSOR'), ('SCENARIO'))
    PROFESSOR = models.ForeignKey('professors', to_field = 'PROFESSOR', on_delete = models.CASCADE, related_name="professors_to_scenario1", primary_key= True)
    SCENARIO = models.ForeignKey('scenarios', to_field = 'SCENARIO_ID', on_delete = models.CASCADE, related_name="professors_to_scenario2")
    PERMISSION = models.IntegerField()


class Issues(models.Model):
    # class Meta:
    #     unique_together = (('SCENARIO'),('ISSUE'),('VERSION'))
    SCENARIO_ID = models.ForeignKey('scenarios', to_field= 'SCENARIO_ID', on_delete = models.CASCADE, related_name = "scenario_id1", default = None)
    ISSUE = models.AutoField(default = None, primary_key = True, editable = False)
    VERSION = models.IntegerField(default=1, editable=False)
    NAME = models.CharField(max_length = 1000)
    IMPORTANCE_SCORE = models.IntegerField(validators = [MinValueValidator(0.0)])


class coverage(models.Model):
    class Meta:
        unique_together = (('STAKEHOLDER'),('ISSUE'))
    STAKEHOLDER = models.ForeignKey('stakeholders', to_field = 'STAKEHOLDER', on_delete = models.CASCADE, related_name = "coverage2", default = None)
    ISSUE = models.ForeignKey('Issues', to_field = 'ISSUE', on_delete = models.CASCADE, related_name = "coverage1", default = None)
    # VERSION_ID = models.ForeignKey('stakeholders',on_delete = models.CASCADE, related_name = "coverage3", default = None)
    COVERAGE_SCORE = models.FloatField(validators = [MinValueValidator(0.0)])

class action_page(models.Model):
    class Meta:
        unique_together = (('PAGE'),('CHOICE'), ('id'), ('RESULT_PAGE'))
    PAGE = models.ForeignKey('pages',on_delete = models.CASCADE, related_name = 'action_page1')
    CHOICE = models.TextField(default = 'default')
    RESULT_PAGE = models.IntegerField(null=True)
    id = models.AutoField(primary_key = True)

class response_to_action_page(models.Model):
    RESPONSE_ID = models.ForeignKey('responses', to_field = 'RESPONSE_ID', on_delete = models.CASCADE, related_name = 'action_page2')
    ACTION_PAGE = models.ForeignKey('action_page', to_field = 'id', on_delete = models.CASCADE, related_name = 'action_page3')

# class assigned_to(models.Model):
#     class Meta:
#         unique_together = (('STUDENT'),('SCENARIO'),('VERSION'))
#     STUDENT = models.ForeignKey('students', on_delete = models.CASCADE, related_name="assigned_to1")
#     SCENARIO = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name="assigned_to2")
#     VERSION = models.IntegerField(default=1, editable=False)

class student_times(models.Model):
    class Meta:
        unique_together = (('STUDENT'),('SCENARIO_ID'),('COURSE'),('DATE_TAKEN'),('PAGE'))
    STUDENT = models.ForeignKey('students', to_field= 'STUDENT', on_delete = models.CASCADE, related_name="student_times1")
    SCENARIO_ID = models.ForeignKey('scenarios', to_field= 'SCENARIO_ID', on_delete = models.CASCADE, related_name="student_times2")
    
    COURSE = models.ForeignKey('courses', to_field = 'COURSE', on_delete = models.CASCADE,related_name = "student_times3")
    DATE_TAKEN = models.DateField(auto_now_add=True)
    PAGE = models.IntegerField()
    START_TIME = models.DateField(null = True)
    END_TIME = models.DateField(null = True)


"""class scenario_creator(models.Model):
    SCENARIO = models.ForeignKey('scenarios', on_delete = models.CASCADE, related_name="scenario_creator1")
    PROFESSOR = models.ForeignKey('professors', to_field = 'PROFESSOR', on_delete =models.CASCADE, related_name="scenario_creator2", default = 1)"""
