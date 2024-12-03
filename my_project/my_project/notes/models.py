from django.db import models

# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True) #description
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        #return the task title
        return self.title