from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        """create and save new user"""

        if not email:
            raise ValueError("Email must be provieded")

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,  password):
        """create new super user"""

        if not email:
            raise ValueError("Email must be provieded")

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        user.role = "admin"
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model """
    """
        Fields: role , email: (username) , password , is_active, is_staff
    """

    USER_CHOICES = (
        ("reception", "Reception"),
        ("admin", "Admin"),
        ("technician", "Technician"),
        ("inspector", "Inspector"),
    )

    role = models.CharField(choices=USER_CHOICES, max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'


class Car(models.Model):
    """Car object"""
    """
        Fields: name , model , is_repaired , is_finished, part
    """
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    is_repaired = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)
    part = models.ManyToManyField('Part')


class Part(models.Model):
    """Car object"""
    """
        Fields: name , price
    """
    name = models.CharField(max_length=255)
    price = models.IntegerField()
