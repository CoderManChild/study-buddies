from django.db import models

class studyTime(models.Model):
    name = models.CharField(max_length=120)
    minutesStudied = models.IntegerField()
    def _str_(self):
        return self.name + ":" + self.minutesStudied
