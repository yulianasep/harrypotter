from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='auth_user_set',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='auth_user_set',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "name", "last_name"]

    def __str__(self):
        return self.username

class House(models.Model):
    name = models.CharField(max_length=50)
    mascot = models.CharField(max_length=50)
    head_of_house = models.CharField(max_length=50)
    house_ghost = models.CharField(max_length=50)
    founder = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Spell(models.Model):
    spellName = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return f"{self.spellName}"