from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class OtherProileData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profileImage = models.ImageField(upload_to="images", height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return self.user.username
    
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.PositiveIntegerField(default=0)