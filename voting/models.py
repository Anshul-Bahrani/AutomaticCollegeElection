# from enum import Enum

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse

from core.models import MetaDataModel
from ACE.users.models import CustomUser


class ElectionType(MetaDataModel):

    type = models.CharField(max_length=100)
    def __str__(self):
        return self.type

class Position(MetaDataModel):

    name = models.CharField(max_length=100)
    type = models.ForeignKey(ElectionType, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _('Position')
        verbose_name_plural = _('Positions')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("voting:position_list")

class Nominee(MetaDataModel):

    id = models.BigAutoField(primary_key=True)
    nominee_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    agenda = models.TextField()
    election = models.ForeignKey('Election', on_delete=models.CASCADE)
    is_Verified = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _('Nominee')
        verbose_name_plural = _('Nominees')

    def __str__(self):
        return self.nominee_id

    def get_absolute_url(self):
        return reverse("voting:position_list")

class Election(MetaDataModel):

    id = models.BigAutoField(primary_key=True)
    registrar = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    term = models.IntegerField()
    start_at = models.DateTimeField()
    duration = models.TimeField()
    nomination_deadline = models.DateTimeField()
    def __str__(self):
        return f"{self.term}-{self.position}"

class ElectedMember(MetaDataModel):

    id = models.BigAutoField(primary_key=True)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    member = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    def __str__(self):
        return "{self.election}-{self.member}"

class Ballot(MetaDataModel):

    id = models.BigAutoField(primary_key=True)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    voter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return "{self.election}-{self.nominee}-{self.voter}"

# class Prerequisite(MetaDataModel):

#     Position = models.ForeignKey('Position', on_delete=models.DO_NOTHING)
