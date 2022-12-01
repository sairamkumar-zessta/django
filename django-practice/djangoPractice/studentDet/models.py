from numbers import Number
from django.db import models
from datetime import date
from django.dispatch import receiver 
# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length = 100)
    class_name = models.IntegerField()
    date_of_birth = models.DateField() 
    age = models.IntegerField(editable = False)

    @property
    def age_add (self):
        today = date.today()
        self.age = today.year - self.date_of_birth.year - ((today.month, today.day) <(self.date_of_birth.month, self.date_of_birth.day))
    


@receiver(models.signals.pre_save, sender=StudentModel) 
def add_age(sender , instance, **kwargs):
    instance.age_add 