from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # Added a related_name attribute to make it easier to access all posts by a user, e.g., user.posts.all().


    class Meta:
        ordering = ['-date_posted']  # Ensures that posts are ordered by date_posted in descending order (newest posts first).
        verbose_name = 'Post'  # Provides readable names for the model in the Django admin interface.
        verbose_name_plural = 'Posts'

    
    # Added a __str__ method to return the post's title, which is useful in Django admin and other interfaces.
    def __str__(self):
        return self.title
    
    
    # Added get_absolute_url to provide a URL for each post. This is useful when redirecting after creating or editing a post
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})



