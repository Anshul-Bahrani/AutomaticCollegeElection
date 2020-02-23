from django.forms import ValidationError

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class AccountAdapter(DefaultAccountAdapter):


    def clean_email(self, email):
        if not email.endswith('@ves.ac.in'):
            raise ValidationError('You are restricted from registering.\
                                                  Please contact admin.')
        return email

    # def is_open_for_signup(self, request):
    #     return False

class SocialAccountAdapter(DefaultSocialAccountAdapter):
    pass
