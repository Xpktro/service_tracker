# coding:utf-8
from django import forms

from suscription.models import Suscriber


class SuscriptionForm(forms.ModelForm):
    class Meta:
        model = Suscriber
        fields = ('email',)
