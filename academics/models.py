import datetime
from django.db import models

from core.models import MetaDataModel

class Department(MetaDataModel):

    code = models.PositiveIntegerField()
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name

class Term(MetaDataModel):

    year_choices = [(i, i) for i in range(1984, datetime.datetime.now().year +1)]

    @staticmethod
    def current_year():
        return datetime.date.now().year

    term_id = models.IntegerField(unique=True)
    academic_year = models.PositiveIntegerField(choices=year_choices)
    deptartment = models.ForeignKey(Department, on_delete=models.CASCADE)
    sem = models.PositiveIntegerField(choices=[(x, x) for x in range(1, 9)])

    def __str__(self):
        return self.term_id
