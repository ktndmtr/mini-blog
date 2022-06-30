from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    biography = forms.CharField(
        label='Biography', max_length=300, widget=forms.Textarea(), required=False
    )

    class Meta:
        model = User
        fields = ('username', 'biography', 'password1', 'password2')
