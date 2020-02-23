from django.contrib import admin


from .models import ElectionType, Position, Election, Nominee, ElectedMember, Ballot

admin.site.register(Ballot)

admin.site.register(Election)

admin.site.register(ElectedMember)

admin.site.register(ElectionType)

admin.site.register(Nominee)

admin.site.register(Position)
