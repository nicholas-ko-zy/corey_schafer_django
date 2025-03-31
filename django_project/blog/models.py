from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    #  Create title attribute, a character field with a max length
    title = models.CharField(max_length=100)
    # Create content attribute as a textfield
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # on_delete removes all the posts if the user is deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
