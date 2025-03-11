from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db.models.signals import post_save
from django.conf import settings

# Create your models here.

class CustomUser(AbstractUser):
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class LocalNewsSite(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255,unique=True)
    Owner = models.ForeignKey(CustomUser,on_delete=models.CASCADE , related_name = 'owned_sites')

    def __str__(self):
        return self.name


SAAS_ADMIN_GROUP = "SaaS Admin"
LOCAL_OWNER_GROUP = "Local News Owner"
EDITOR_GROUP = "Editor"

def create_groups():
    saas_admin_group,_ = Group.objects.get_or_create(name=SAAS_ADMIN_GROUP)
    localowner_group,_ = Group.objects.get_or_create(name=LOCAL_OWNER_GROUP)
    editor_group,_ = Group.objects.get_or_create(name=EDITOR_GROUP)



'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

post_save.connect(createProfile, sender=User)
'''