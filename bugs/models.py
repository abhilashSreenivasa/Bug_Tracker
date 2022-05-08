from django.db import models
from core.models import UserProfile

# Create your models here.
class BugType(models.Model):
    bug_type_id=models.CharField(max_length=5,primary_key=True)
    bug_type=models.CharField(max_length=100)

class BugPriority(models.Model):
    bug_priority_id=models.CharField(max_length=5,primary_key=True)
    bug_priority=models.CharField(max_length=10)

class BugStatus(models.Model):
    bug_status_id=models.CharField(max_length=5,primary_key=True)
    bug_status=models.CharField(max_length=20)

class Bug(models.Model):
     bug_id=models.CharField(max_length=5,primary_key=True)
     bug_type=models.ForeignKey(BugType, on_delete=models.CASCADE )
     bug_priority=models.ForeignKey(BugPriority,on_delete=models.CASCADE)
     bug_desc=models.CharField(max_length=280)
     bug_owner=models.ForeignKey(UserProfile, on_delete=models.CASCADE , default='2')
     bug_status=models.ForeignKey(BugStatus, on_delete=models.CASCADE, default='1')
     
