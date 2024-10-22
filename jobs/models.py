from django.db import models
from django.contrib.auth.models import User

### model for job ###
class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    responsibility = models.TextField()
    experience = models.TextField()
    benfits = models.TextField()
    salary = models.FloatField()

## enumerate levels ##
experience_levels = [
    ("Jenior","Jenior"),
    ("Mid-level","Mid-level"),
    ("Senior","Senior"),
]

## model for aplication ##
class Application(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    # user = models.ForeignKey(User,on_delete=models.CASCADE,null=True, blank=True)
    github_link = models.URLField()
    website_link = models.URLField(null=True,blank=True)
    cv = models.FileField(upload_to="application/")
    image = models.ImageField(upload_to="application/")
    experience = models.CharField(max_length=10,choices=experience_levels,default="Jenior")

    ## prevent one user apply twice in the same job ##
    # class Meta:
    #     unique_together = ['job','user'] 