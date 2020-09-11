from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='image', default="images/default.png")
    info = models.TextField(null=True, blank=True)
    followings = models.ManyToManyField("self", related_name="followers", symmetrical=False) #symmetrical=False 대칭깨트림

@receiver(post_save, sender=User) #User모델 변화
def create_user_profile(sender, instance, created, **kwargs): #user모델, 업데이트된 객체, 객체새로생성?, 키워드arguments
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

    
# Create your models here.
