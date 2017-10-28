from django import forms
from wimm.models import Wimm, DayState
from django.contrib.auth import authenticate


class WimmForm(forms.ModelForm):
    class Meta:
        model = Wimm
        fields = ['text', 'img']


class WimmFormWithDate(forms.ModelForm):
    class Meta:
        model = Wimm
        fields = ['text', 'img', 'pub_date']


class StateForm(forms.ModelForm):
    class Meta:
        model = DayState
        fields = ['state']


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}), max_length=24)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Invalid username or password.")

    def login(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
