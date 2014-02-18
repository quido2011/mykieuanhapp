# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from mykieuanhapp.clients.forms import ClientForm
from django.contrib import messages


def addclient(request):
    form = ClientForm()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            id_client = form.instance.pk
            messages.success(request, '%s' %"Tạo khách hàng thành công")
            return HttpResponseRedirect('/' %id_client)
        else:
            messages.error(request, '%s' %form.errors)
            return HttpResponseRedirect('/')
    else:
        return render_to_response('form.html',
                                    {'form': form,
                                     'titre':"Tạo khách hàng mới!",
                                      'url': '/clients/addclient/'},
                                      context_instance = RequestContext(request))
