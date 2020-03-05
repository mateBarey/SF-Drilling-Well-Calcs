from django.db import models
from django.contrib.auth.models import User
import datetime
from django.db.models.query import QuerySet
from django.http import HttpResponse
# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    #additional
    portfolio_site = models.URLField(blank=True)
    
    def __str__(self):
        return self.user.username


class AcFlaggedWell(models.Model):
    sf_one = models.DecimalField(max_digits=30,decimal_places=4)
    sf_two = models.DecimalField(max_digits=30,decimal_places=4)
    api = models.IntegerField(max_length=None)
    center_center_distance = models.DecimalField(max_digits=30,decimal_places=4)
    traj = models.CharField(max_length=200)
    survey = models.CharField(max_length=200)
    tvd = models.DecimalField(max_digits=50, decimal_places=4)
    well = models.CharField(max_length=50)
    x = models.DecimalField(max_digits=40, decimal_places=4)
    y = models.DecimalField(max_digits=40, decimal_places=4)
    case = models.IntegerField(max_length=None)
    lateral_distance = models.DecimalField(max_digits=30, decimal_places=4)
    def __str__(self):
        return self.sf_one
        return self.sf_two
        return self.api
        return self.center_center_distance
        return self.traj
        return self.survey
        return self.tvd
        return self.well
        return self.x
        return self.y 
        return self.case 
        return self.lateral_distance

'''
class AcNotFlaggedWells(models.Model):
    sep_fac_one = models.DecimalField(max_digits=10, decimal_places=3)
    sep_fac_two = models.DecimalField(max_digits=10, decimal_places=3)
    api = models.IntegerField(max_length=None)
    center_center_distance = models.DecimalField(max_digits=10,decimal_places=3)
    traj = models.CharField(max_length=200)
    survey = models.CharField(max_length=200)
    tvd = models.DecimalField(max_digits=50,decimal_places=2)
    well = models.CharField(max_length=50)
    x = models.DecimalField(max_digits=20, decimal_places=3)
    y = models.DecimalField(max_digits=20, decimal_places=3)
    case = models.IntegerField(max_length=None)
    def __str__(self):
        return self.sep_fac_one
        return self.sep_fac_two
        return self.api
        return self.center_center_distance
        return self.traj
        return self.survey
        return self.tvd
        return self.well
        return self.x
        return self.y 
        return self.case 


class FlaggedLabels(models.Model):
    api = models.IntegerField(max_length=None)
    string = models.CharField(max_length=200)
    x = models.DecimalField(max_digits=20,decimal_places=3)
    y = models.DecimalField(max_digits=20,decimal_places=3)
    def __str__(self):
        return self.api 
        return self.string 
        return self.x
        return self.y 

class OffsetLabels(models.Model):
    api = models.IntegerField(max_length=None)
    string = models.CharField(max_length=200)
    x = models.DecimalField(max_digits=20,decimal_places=3)
    y = models.DecimalField(max_digits=20,decimal_places=3)
    def __str__(self):
        return self.api 
        return self.string 
        return self.x
        return self.y

'''
