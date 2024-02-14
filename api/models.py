# api\models.py
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)

# Create your models here.
# custom User model process


# manager power dey ORM ba base model use korar
class UserManager(BaseUserManager):
    # ei create_user call hbe jokhon kono user / superuser create kri
    def create_user(self, email, password):
        if not email:
            raise ValueError("Please insert user Email")

        # normalize email: jemon uppercase / lowercase jhamela thake ta resolve kore
        email = self.normalize_email(email)

        # current model er under e user
        user = self.model(email=email)

        # encrypt password
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self.db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
