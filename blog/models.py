from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Post(models.Model):
   title = models.CharField(max_length=250)
   body = models.TextField()
   publish_date = models.DateTimeField('published date')
   gPlus = models.IntegerField()
   tags = TaggableManager()
   
   def __unicode__(self):
      return self.title
