# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from mykieuanhapp.clients.models import Client



class ClientForm(ModelForm):
    nomClient = forms.CharField(label=(u"Tên khách hàng"),required = True)
    telClient = forms.CharField(label=(u"Điện thoại KH"), required = True)

    class Meta:
        model= Client