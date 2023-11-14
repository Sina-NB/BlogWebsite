from django.db import models
from account.models import User

class Post(models.Model):
    '''
    This class implements post model for blog app
    '''
    title = models.CharField(max_length= 250)
    content = models.TextField()
    image = models.ImageField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField('Category')
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Category(models.Model):
    '''
    This class implements category model for blog app
    '''
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    