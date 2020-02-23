# from enum import Enum

from django.db import models
# from django.utils.translation import ugettext_lazy as _
# from django.urls import reverse

from core.models import MetaDataModel
from academics.models import Department
from ACE.users.models import CustomUser


# class Staff(MetaDataModel):

#     id = models.BigAutoField(primary_key=True)
#     user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class StaffCtCcAllotment(MetaDataModel):

    id = models.BigAutoField(primary_key=True)
    term = models.IntegerField()
    division = models.ForeignKey(Department, on_delete=models.CASCADE)
    class_teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='class_teacher')
    class_counsellor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='class_counsellor')

    def __str__(self):
        return self.term
