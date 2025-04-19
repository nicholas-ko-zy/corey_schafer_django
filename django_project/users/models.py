from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    # Create a user with cascading deletes. 
    # Deleting a user, deletes the profile as well. But not the other way around.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self):
        # Use the save method of our parent class
        super().save()

        # Open image of the current profile instance
        img = Image.open(self.image.path)

        # Check if image is large
        if img.height > 300 or img.width > 300:
            # Set the desired output image size
            output_size = (300, 300)
            # Resize image with the thumbnail method
            img.thumbnail(output_size)
            # Override the large image, with the resized smaller image
            img.save(self.image.path)
