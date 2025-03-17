from django.db import models
from courses.models import Course

class Assessment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.title
