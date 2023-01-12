from django import forms
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (
    Submit,
    Div,
)

from .models import *


class AddRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalImage
        fields = (
            'patient',
            'Description',
            'Medical Image',
        )

    visited_date = forms.DateTimeField(input_formats=['%Y-%m-%d'], help_text='Year-Month-Day')


class AddAccountForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = '__all__'


class AddUserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(AddUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    class Meta:
        model = User
        fields = ('username', 'email',)
