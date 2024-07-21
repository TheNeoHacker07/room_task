from django.db import models
from django.utils.crypto import get_random_string
from django.contrib.auth.models import AbstractUser, BaseUserManager

class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **extra):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra):
        extra.setdefault('is_active', False)
        user = self._create_user(email, password, **extra)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra):
        extra.setdefault('is_superuser', True)
        extra.setdefault('is_staff', True)
        extra.setdefault('is_active', True)

        if extra.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        return self._create_user(email, password, **extra)

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    activation_code = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def create_activation_code(self):
        self.activation_code = get_random_string(length=30)
        self.save()

    def __str__(self):
        return self.email
