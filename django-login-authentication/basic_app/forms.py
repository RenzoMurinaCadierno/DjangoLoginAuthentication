from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

# A Model Form (to save to DB), for Django's standard User model.
class UserForm(forms.ModelForm):

    # create the field that is absent in User() standard model
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():

        # target this model
        model = User

        # include this fields only
        fields = ('username', 'email', 'password')

# And a Model Form for our own UserProfileInfo model
class UserProfileInfoForm(forms.ModelForm):

    class Meta():

        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
