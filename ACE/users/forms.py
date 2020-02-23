from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm

from allauth.account.forms import SignupForm
from academics.models import Department
from .models import CustomUser, UserRole



class UserRegisterForm(UserCreationForm):

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': ''}))
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(label="Email Address")
    mobile = forms.IntegerField(min_value=1000000000, max_value=9999999999)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=[x.value for x in CustomUser.GENDER])
    BIRTH_YEAR_CHOICES = range(1950, datetime.now().year +1)
    date_Of_birth = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),
                                    input_formats=['%Y-%m-%d'], help_text='Format:YYYY-MM-DD')


    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name', 'mobile', 'gender', 'date_Of_birth', ]


class CustomSignupForm(SignupForm):

    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': ''}))
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(label="Email Address")
    mobile = forms.IntegerField(min_value=1000000000, max_value=9999999999)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=[x.value for x in CustomUser.GENDER])
    BIRTH_YEAR_CHOICES = range(1950, datetime.now().year +1)
    date_Of_birth = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),
                                    input_formats=['%Y-%m-%d'], help_text='Format:YYYY-MM-DD')

    def signup(self, request, user):
        user.mobile = 0
        user.gender =  'M'
        user.date_Of_birth =  '1999-12-16'
        student = UserRole.objects.get(role_number=2)
        user.role = student
        user.department_id = Department.objects.get(code=2)
        user.save()
        return user


class UserUpdateForm(forms.ModelForm):

    error_css_class = 'error'
    required_css_class = 'required'

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(label="Email Address")
    mobile = forms.IntegerField(min_value=1000000000, max_value=9999999999)
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=[x.value for x in CustomUser.GENDER])
    BIRTH_YEAR_CHOICES = range(1950, datetime.now().year +1)
    date_Of_birth = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES),
                                    input_formats=['%Y-%m-%d'], help_text='Format:YYYY-MM-DD')

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'mobile', 'gender', 'date_Of_birth', 'profile_pic']
