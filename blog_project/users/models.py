from django.db import models
from django.contrib.auth.models import User
# import imahe from pillow
from PIL import Image

# Create your models here.
class Profile(models.Model):
    # 1 image have one a/c
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        # save the parent IMAGE
        super().save()
        # import pillow library
        # resize the image
        img = Image.open(self.image.path)
        if img.width >= 300 or img.heght >= 300:
            # this will be a tuple
            output_img = (300,300)
            img.thumbnail(output_img)
            img.save(self.image.path)
