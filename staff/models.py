# from enum import Enum

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from core.models import MetaDataModel
from academics.models import Department, Term
from ACE.users.models import CustomUser


# class Staff(MetaDataModel):

#     id = models.BigAutoField(primary_key=True)
#     user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class StaffCtCcAllotment(MetaDataModel):

    id = models.BigAutoField(primary_key=True)
    term_id = models.ForeignKey(Term, on_delete=models.CASCADE)
    division = models.CharField(max_length=5)
    class_teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='class_teacher')
    class_counsellor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='class_counsellor')



    class Meta:
        ordering = ["-created_at"]
        verbose_name = _('ctcc')
        verbose_name_plural = _('ctcc')

    def __str__(self):
        return f"{self.term_id}"

    def get_absolute_url(self):
        return reverse("staff:ctcc_list")
