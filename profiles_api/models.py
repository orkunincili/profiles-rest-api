from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionMixin
from django.contrib.auth.models import BaseUserManager


"""
These are standard base classes that we need to use overriding or customizing
the DEFAULT DJANGO USER MODEL
https://docs.djangoproject.com/en/2.2/topics/auth/customizing/#auth-custom-user
"""


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email, name, password=None):
        """
        Create a new user profile

        Note: password=None This means that if you dont specify a password
        the it will be none and because of the way the django
        password checking system works a non password wont work because
        it needs to be a hash so until we set a password we
        wont be able to authenticate with the user
        """

        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        """
        password is a sensitive data and it must to encrypt and by default
        django does this with the set_password
        """

        user.save(using=self._db) #specify to database

        return user


        def create_super_user(self, email, password):
            """Create and save a new super user with given details"""

            user = self.create_user(email, name ,password)

            user.is_superuser = True #created by the PermissionMixin
            user.is_staff = True
            user.save(using=self._db)

            return user


class UserProfile(AbstractBaseUser, PermissionMixin):
    """Database model for users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    """
    Override USERNAME_FIELD (default USERNAME_FIELD is username)
    When we authenticate users instead of them providing a username
    and password.They are going to provide their email and password.
    """

    REQUIRED_FIELDS = ['name']
    """
    That is additional required fields.Users must specify their email address
    and their name.
    """

    def get_full_name(self):
        """Retrieve full name of user"""

        return self.NAME

    def get_short_name(self):
        """Retrieve short name of user"""

        return self.name

    def __str__(self):
        """Return string representation of our user"""

        return self.email
