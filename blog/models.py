from django.db import models

# Create your models here.
class Blog(models.Model):
   title = models.CharField(max_length=250)
   body = models.TextField()
   publish_date = models.DateTimeField('published date')
   gPlus = models.IntegerField()

   def __unicode__(self):
      return self.title
