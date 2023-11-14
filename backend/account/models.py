from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    '''
    Custom user manager for User model.
    '''
    def create_user(self, email, password, **kwargs):
        '''
        Create and save a user with the given email and password
        '''
        if not email:
            raise ValueError(_("The email must be set"))
        self.email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        '''
        Create and save a superuser with the given email and password
        '''
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        if kwargs.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff=True"))
        if kwargs.get('is_superuser') is not True:
            raise ValueError(_("Superuser must have is_superuser=True"))
        self.create_user(email, password, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    '''
    Custom user model that uses email as the username.
    '''
    email = models.EmailField(max_length=255, unique=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
