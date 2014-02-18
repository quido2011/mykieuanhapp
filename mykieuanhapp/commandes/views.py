# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response


def accueil_commandes(request):
    return render_to_response('home.html',
                              {'PAGE_TITLE': 'Quản lí đơn hàng' ,'WEBSITE_TITLE': 'DNTN Kiều Anh'})