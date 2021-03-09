from django.db import models

# Create your models here.

#Taken from last semester editor backend:

#class scenarios(models.Model):
    #class Meta:
        #unique_together = (('SCENARIO'), ('VERSION'))
    #SCENARIO = models.AutoField(primary_key = True, editable=False)
    #TODO remove professors
    #PROFESSOR = models.ForeignKey('professors', to_field = 'PROFESSOR', on_delete =models.CASCADE, related_name="scenario_creator2", default = 1)
    #VERSION = models.IntegerField(default=1, editable=False)
    #NAME = models.CharField(max_length = 1000)
    #PUBLIC = models.BooleanField(default = False)
    #NUM_CONVERSATION = models.IntegerField(default = 0)
    #IS_FINISHED = models.BooleanField(default = False)
    #DATE_CREATED = models.DateField(auto_now_add=True)