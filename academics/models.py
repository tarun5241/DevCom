# from ssl import _PasswordType
from unicodedata import name
import uuid
from django.db import models
import uuid
# Create your models here.

class Student(models.Model):
    STD_TYPE = (
        ('5','5th'),
         ('6','6th'),
    )
    name   = models.TextField(null=False, blank=False)
    rollno = models.IntegerField(null=False, blank=False)
    password = models.CharField(max_length=200 ,null=False, blank=False)
    std = models.CharField(max_length=200, choices=STD_TYPE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    
    #to encrypt the models in database to view the tables in db
    def __str__(self):
        return self.std


class Marks(models.Model):
    # student = models.ForeignKey(Student, on_delete=models.CASCADE)
    STD_TYPE = (
        ('5','5th'),
         ('6','6th'),
    )

    rollno = models.IntegerField(null=False, blank=False, default=1)
    std = models.CharField(max_length=200, choices=STD_TYPE)

    eng = models.IntegerField(null=False, blank=False)
    math = models.IntegerField(null=False, blank=False)
    sci = models.IntegerField(null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,editable=False)
    

    def __str__(self):
        return self.eng
