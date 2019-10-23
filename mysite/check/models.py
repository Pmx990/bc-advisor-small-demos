from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class Program(models.Model):
    program_text = models.CharField(max_length=50)
    classes = ArrayField(
            models.CharField(max_length=30,blank=True)
    )

    #get_classes_str = str(classes)

    def __str__(self):
        #return self.program_text;
        temp = str(self.classes)
        temp = temp.replace(",","")
        temp = temp.replace("'","")
        temp = temp.replace(" ",",")
        return temp


# q = Program(program_text = "Math",classes=["Math002","Math003","Math004"])
# q = Program.object.get(id=2)