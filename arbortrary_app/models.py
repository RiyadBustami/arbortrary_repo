from django.db import models
from login_registration_app.models import User
from django.utils.timezone import now
# Create your models here.

class TreeManager(models.Manager):
    def tree_validator(self,postData):
        errors={}
        if len(postData['species'])<5:
            errors['species']='Species min 5 characters'
        if len(postData['location'])<2:
            errors['location']="Location min 2 characters"
        if len(postData['reason'])>50:
            errors['reason']="Reason max 50 characters"
        return errors




class Tree(models.Model):
    species=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    reason=models.CharField(max_length=255)
    date_planted=models.DateField(default=now)
    planted_by=models.ForeignKey(User,related_name="trees",on_delete=models.CASCADE)
    visited_by=models.ManyToManyField(User,related_name="visited_trees")
    num_of_visits=models.IntegerField(default=0)
    objects= TreeManager()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
