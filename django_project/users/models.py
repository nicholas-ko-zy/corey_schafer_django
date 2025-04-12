from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    # Create a user with cascading deletes. 
    # Deleting a user, deletes the profile as well. But not the other way around.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    