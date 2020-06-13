from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.db import models

from accounts.utils import mobile_regex
from accounts.utils import profile_upload_location


class SiteUser(AbstractUser):
    avatar = models.ImageField(upload_to=profile_upload_location)
    phone = models.CharField(max_length=10, validators=[mobile_regex])
    about_me = models.TextField()
    profile = models.CharField(max_length=32)
    experience_from = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.get_full_name() if self.get_full_name() else self.get_username()


class Skill(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    skill = models.CharField(max_length=64)
    percentage = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    position = models.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.skill


class Designation(models.Model):
    user = models.ForeignKey(SiteUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
