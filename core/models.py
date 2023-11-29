from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .manager import UserManager

# Create your models here.

class CustomUser(AbstractBaseUser):
    email = models.EmailField(null=False, blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    password=models.CharField(max_length=45, )
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
         return True

    def has_module_perms(self, app_label):
        return True