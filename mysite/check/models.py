from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Program(models.Model):
    program_text = models.CharField(max_length=50)
    classes = ArrayField(
            models.CharField(max_length=30,blank=True)
    )
    def __str__(self):
        return self.program_text;
    
