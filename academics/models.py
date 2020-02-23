import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from core.models import MetaDataModel

class Department(MetaDataModel):

    code = models.PositiveIntegerField()
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Term(MetaDataModel):

    year_choices = [(i, i) for i in range(datetime.datetime.now().year, 2000, -1)]

    @staticmethod
    def current_year():
        return datetime.date.now().year

    term_id = models.IntegerField(unique=True)
    academic_year = models.PositiveIntegerField(choices=year_choices)
    department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    sem = models.PositiveIntegerField(choices=[(x, x) for x in range(1, 9)])

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _('Term')
        verbose_name_plural = _('Terms')

    def __str__(self):
        return f"{self.term_id}"

    def get_absolute_url(self):
        return reverse("home")

