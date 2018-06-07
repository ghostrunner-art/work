from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add= True)
    last_updated_time = models.DateTimeField(auto_now= True)
    is_deleted = models.BooleanField(default= False)
    readed_num = models.IntegerField(default= 0)
    #def __str__(self):
    #  return '<Article: %s>' % self.title



# Create your models here.
