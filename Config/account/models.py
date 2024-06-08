# from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import gettext_lazy as _ # bu ilovani ko'p tilli qilish uchun ham ishlatiladi
# from django.db import models
# from django.contrib.auth.models import AbstractUser, PermissionsMixin
#
# class CustomUserManager(BaseUserManager):
#     """
#     Custom user model manager where email is the unique identifiers
#     for authentication instead of usernames.
#     """
#     def create_user(self, email, password, **extra_fields):
#         """
#         Create and save a user with the given email and password.
#         """
#         if not email:
#             raise ValueError(_("The Email must be set"))
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save()
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#         """
#         Create and save a SuperUser with the given email and password.
#         """
#         extra_fields.setdefault("is_staff", True)
#         extra_fields.setdefault("is_superuser", True)
#         extra_fields.setdefault("is_active", True)
#
#         if extra_fields.get("is_staff") is not True:
#             raise ValueError(_("Superuser must have is_staff=True."))
#         if extra_fields.get("is_superuser") is not True:
#             raise ValueError(_("Superuser must have is_superuser=True."))
#         return self.create_user(email, password, **extra_fields)
#
# class CustomUser(AbstractUser, PermissionsMixin):
#     email = models.CharField(max_length=255, unique=True)
#     username = None
#     first_name = models.CharField(max_length=255, blank=True, null=True)
#     last_name = models.CharField(max_length=255, blank=True, null=True)
#     password = models.CharField(max_length=255)
#
#     is_staff = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = CustomUserManager()
#
#     def __str__(self):
#         return self.email
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class CustomUserManager(BaseUserManager): # bu model emas. bu funksiyani bajaradigan class
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError(_('The given email must be set'))
        email = self.normalize_email(email) # this chick requirement for email
        user = self.model(email=email, **extra_fields) # this is opening new user
        user.set_password(password) # this is adding password to user (heslash)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_stuff=True'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True'))

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser): # bu model
    email = models.CharField(max_length=255, unique=True) # our email should be unique and this do this
    username = None
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False) # if someone is staff it is altered into True
    is_active = models.BooleanField(default=False) # it looks like asking permession after join close telegram channael
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email' # we want to regester with what # createsuper qilganda kerak bo'ladi
    REQUIRED_FIELDS = [] # kiritilishi shart fieldlar # createsuper qilganda kerak bo'ladi

    objects = CustomUserManager() # superuser va oddiy user ochish uchun birmarta chaqirib ketyapmiz

    def __str__(self):
        return self.email

class CodeConfirmation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_code')
    code = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.email} --- {self.code}'
