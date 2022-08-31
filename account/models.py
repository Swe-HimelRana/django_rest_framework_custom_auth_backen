from ctypes import addressof
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):

# create a new user
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError('Please provide an email address')
        
        if not username:
            raise ValueError('Please provide a username')

        if not first_name:
            raise ValueError('Please provide a first name')

        if not last_name:
            raise ValueError('Please provide a last_name')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

# create a enw superuser
    def create_superuser(self, email, username, first_name, last_name, password=None):
       
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.is_support_admin=True
        user.save(using=self._db)

        return user



class Account(AbstractBaseUser):

    email = models.CharField(max_length=255, unique=True, verbose_name="email")
    username = models.CharField(max_length=50, unique=True, verbose_name="username")
    phone = models.CharField(max_length=255, verbose_name="phone", blank=True, null=True)
    first_name = models.CharField(max_length=50, verbose_name="first_name")
    last_name = models.CharField(max_length=50, verbose_name="last_name")
    country = models.CharField(max_length=60, verbose_name="country", blank=True, null=True)
    date_of_birth = models.DateField(verbose_name="date_of_birth", blank=True, null=True)
    state = models.CharField(max_length=60, verbose_name="state", blank=True, null=True)
    city = models.CharField(max_length=60, verbose_name="city", blank=True, null=True)
    zipcode = models.CharField(max_length=60, verbose_name="zipcode", blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name="address", blank=True, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    last_login_ip = models.CharField(max_length=50, default="0.0.0.0")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_support_admin = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)
    recovery_codes = models.CharField(max_length=255, blank=True, null=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def get_email(self):
        return self.email

    def get_recovery_codes(self):
        return self.recovery_codes

    def get_recovery_codes_by_position(self, position):

        text = self.recovery_codes
        try:
            x = text.split(",")
            return x[position - 1]
        except:
            x = ""
            return x
    
    
    

    
    





