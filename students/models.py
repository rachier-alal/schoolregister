from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.utils.translation import gettext_lazy as _


# Create your models here.

class Student(models.Model):
    name = models.CharField(verbose_name=_("Student Name"), max_length=50)
    rfid_code = models.CharField(verbose_name=_("Scanner ID"), max_length=50,null=False, blank=False)
    pub_date = models.DateField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name', unique_with='name', max_length=10)
    author = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name
    

