from django import forms
from django.contrib import admin
from models import Technology


class StopAdminForm(forms.ModelForm):
  class Meta:
    model = Technology
    widgets = {
      'name': CheckboxSelectMultiple(),
    }
    fields = '__all__'