from django.db import models
from django.db.models import fields
from django.forms import widgets
from django.forms.fields import EmailField
from . models import transfer,customerdata
from django import forms

class transaction(forms.ModelForm):
    fromaccount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    toaccount = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    amount=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    class Meta:
        model=transfer
        fields='__all__'

class customerdataform(forms.ModelForm):
    class Meta:
        model = customerdata
        fields = '__all__'

class checkdetailForm(forms.Form):
    account_num=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))