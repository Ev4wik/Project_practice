from django.db import models

class Specialist(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    organization = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class QualificationCourse(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    duration_hours = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Participation(models.Model):
    STATUS_CHOICES = [
        ('attended', 'Attended'),
        ('missed', 'Missed'),
    ]
    specialist = models.ForeignKey(Specialist, on_delete=models.CASCADE)
    course = models.ForeignKey(QualificationCourse, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.specialist} - {self.course}"

# Create your models here.
