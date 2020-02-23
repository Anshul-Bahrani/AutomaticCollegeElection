import datetime
import os
from enum import Enum

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from core.models import MetaDataModel
from academics.models import Department
from .managers import CustomUserManager


class UserRole(MetaDataModel):

    role_name = models.CharField(max_length=500)
    role_number = models.IntegerField()

    def __str__(self):
        return self.role_name

class CustomUser(AbstractUser):

    class GENDER(Enum):
        male = ('M', 'Male')
        female = ('F', 'Female')
        other = ('Ot', 'Other')

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    DEFAULT_PROFILE_IMAGE = 'nopic.jpg'

    def profile_pic_path(self, filename):
        if filename != self.DEFAULT_PROFILE_IMAGE:
            basefilename, file_extension = os.path.splitext(filename)
            randomstr = datetime.datetime.now().strftime('%d-%m-%Y_%I:%M:%S,%f')
            return 'profile_pics/{userid}/{basename}_{randomstring}{ext}'.format(
                userid=self.id, basename=basefilename, randomstring=randomstr, ext=file_extension)
        return self.DEFAULT_PROFILE_IMAGE

    username = None
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(
        _('Email Address'),
        unique=True,
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    mobile = models.BigIntegerField()
    gender = models.CharField(max_length=10, choices=[x.value for x in GENDER])
    date_Of_birth = models.DateField()
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    profile_pic = models.ImageField(default=DEFAULT_PROFILE_IMAGE, upload_to=profile_pic_path)
    role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:

        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('users:profile')

class Student(MetaDataModel):

    year_choices = [(i, i) for i in range(1984, datetime.datetime.now().year +1)]

    @staticmethod
    def current_year():
        return datetime.date.today().year

    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    admission_year = models.IntegerField(_('year'), choices=year_choices)
    addmission_type = models.BooleanField(default=0)
    division = models.CharField(max_length=5, null=True, blank=True)
