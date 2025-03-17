from django.db import models
from courses.models import Course
from users.models import CustomUser

class Assessment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Submission(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    score = models.FloatField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} - {self.assessment.title}"
