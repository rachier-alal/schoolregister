from django.db import models
# from django.contrib.auth.models import User
from autoslug import AutoSlugField
from students.models import Student
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Scanners(models.Model):
    room = models.CharField(max_length=10)
    pub_date = models.DateField(auto_now_add=True)
    slug = AutoSlugField(populate_from='room', unique_with='pub_date', max_length=5)

    def __str__(self):
        return self.room


class ScannerRecords(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    room = models.ForeignKey(Scanners, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.room
    

