from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Div


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            Div(
                Submit(
                    'signup',
                    'Register',
                    css_class='btn btn-danger btn-block signup-btn'
                )
                , css_class='d-block'
            )
        )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
