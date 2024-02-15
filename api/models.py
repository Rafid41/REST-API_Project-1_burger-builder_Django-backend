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
    # login to admin panel
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    # manager er name
    objects = UserManager()
    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email


###################### Models for burger builder backebd #####################
# ingredient count
class Ingredient(models.Model):
    salad = models.IntegerField(default=0)
    cheese = models.IntegerField(default=0)
    meat = models.IntegerField(default=0)

    def __str__(self):
        return f" salad: {self.salad}, cheese: {self.cheese}, meat: {self.meat}"


class CustomerDetail(models.Model):
    deliveryAddress = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    paymentType = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Customer Details: {self.deliveryAddress} , phone: {self.phone}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # OneToOneField is similar to Foreignkey
    # ingrediet id
    ingredients = models.OneToOneField(Ingredient, on_delete=models.CASCADE)
    customer = models.OneToOneField(CustomerDetail, on_delete=models.CASCADE)
    price = models.CharField(max_length=10, default="0")
    orderTime = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return f" Order: {self.user.email}"

