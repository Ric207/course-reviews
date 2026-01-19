from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    min_grade = models.CharField(max_length=2)

    def _str_(self):
        return self.name