from django.db import models

# Create your models here.
class Post(models.Model):
  sno = models.AutoField(primary_key=True)
  title = models.CharField(max_length=255)
  category = models.CharField(max_length=25)
  content = models.CharField(max_length=1000)
  slug = models.CharField(max_length=50)
  author = models.CharField(max_length=12)
  timeStamp = models.DateTimeField(blank=True)

  def __str__(self):
    return  self.title