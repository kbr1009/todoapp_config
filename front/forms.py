from django import forms
from django.contrib.auth.models import User
from .models import List, Card

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ("username", "last_name", "first_name", "email",)

class ListForm(forms.ModelForm):

    class Meta:
        model = List
        fields = ("title",)

class CardForm(forms.ModelForm):

    class Meta:
        model = Card
        fields = ("title", "description", "list")

class CardCreateFromHomeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CardCreateFromHomeForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Card
        fields = ("title", "description",)
