from django.db import models
from django.utils import timezone
from django.urls import  reverse
from django.contrib.auth.models import User
# Create your models here

class PostCategory(models.Model):
	name = models.CharField(max_length=30 ) 

	def __str__(self):
		return self.name 


class Post(models.Model):
	title = models.CharField(max_length=100)
	category =models.ForeignKey(PostCategory,on_delete=models.CASCADE)
	content = models.TextField(max_length=4000)
	date_posted = models.DateTimeField(default=timezone.now)
	author = models.CharField(max_length=100)
	blog_img = models.ImageField(default='default.png',upload_to='profile_pics')
	is_trending = models.BooleanField(default=False)

	def __str__(self):
		return self.title
	
	def get_absolute_url(self):
		return reverse('blog_detail',args=[self.id,])	
