# from enum import Enum

from django.db import models
# from django.utils.translation import ugettext_lazy as _
# from django.urls import reverse

from core.models import MetaDataModel
from ACE.users.models import CustomUser


class ElectionType(MetaDataModel):

    type = models.CharField(max_length=100)

class Position(MetaDataModel):

    name = models.CharField(max_length=100)
    type = models.ForeignKey(ElectionType, on_delete=models.DO_NOTHING)

class Nominee(MetaDataModel):

    id = models.BigAutoField(primary_key=True)
    nominee_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    agenda = models.TextField()
    election = models.ForeignKey('Election', on_delete=models.CASCADE)
    is_Verified = models.BooleanField(default=False)

class Election(MetaDataModel):

    id = models.BigAutoField(primary_key=True)
    registrar = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    position = models.ForeignKey(Position, on_delete=models.DO_NOTHING)
    term = models.IntegerField()
    start_at = models.DateTimeField()
    duration = models.TimeField()
    nomination_deadline = models.DateTimeField()

class ElectedMember(MetaDataModel):

    id = models.BigAutoField(primary_key=True)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    member = models.ForeignKey(Nominee, on_delete=models.CASCADE)

class Ballot(MetaDataModel):

    id = models.BigAutoField(primary_key=True)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    nominee = models.ForeignKey(Nominee, on_delete=models.CASCADE)
    voter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

# class Prerequisite(MetaDataModel):

#     Position = models.ForeignKey('Position', on_delete=models.DO_NOTHING)
