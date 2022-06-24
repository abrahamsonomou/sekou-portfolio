from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomerUser(AbstractUser):
    photo=models.ImageField(upload_to='users_images',blank=True,null=True,name="photo",verbose_name='Photo')
    
    class Meta:
        verbose_name="Profil"

    def __str__(self) -> str:
        return self.username