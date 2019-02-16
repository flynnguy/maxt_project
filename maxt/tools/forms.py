from django import forms
from django.contrib.auth.models import User

from . models import Tool

class AuthorizeToolForm(forms.Form):
    user_to_authorize = forms.ModelChoiceField(queryset=User.objects.all())
    authorize_tools = forms.ModelMultipleChoiceField(queryset=Tool.objects.all())


