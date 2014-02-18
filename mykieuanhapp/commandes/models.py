# -*- coding: utf-8 -*-
from django.db import models
from mykieuanhapp.clients.models import Client


class Commande(models.Model):
    nomCom = models.CharField(verbose_name=(u"Tên đơn hàng"),max_length=200, null=False, blank=False)
    client = models.ForeignKey(Client,verbose_name=(u"Khách hàng"),null=False, blank=False)
    date_commande = models.DateField(verbose_name=(u"Ngày đặt hàng"), null=True, blank=True,auto_now_add=True)
    date_livraison = models.DateField(verbose_name=(u"Ngày giao hàng"), null=True, blank=True)
    total = models.FloatField(verbose_name=(u"Tổng cộng"), default=0,null=True, blank=False)
    commentaires = models.TextField(verbose_name=(u"Ghi chú"),null=True, blank=True)

    def __unicode__(self):
        return self.nomCom


class Service(models.Model):
    nomS = models.CharField(verbose_name=(u"Tên dịch vụ"),max_length=200, null=False, blank=False)
    commandeS = models.ForeignKey(Commande,verbose_name=(u"Đơn hàng"),null=False, blank=False)
    quantiteS = models.FloatField(verbose_name=(u"Số lượng"), null=False, blank=False)
    uniteS = models.CharField(verbose_name=(u"Đơn vị"),max_length=200, null=False, blank=False)
    prixS = models.FloatField(verbose_name=(u"Đơn vị giá"), null=False, blank=False)
    totalS = models.FloatField(verbose_name=(u"Tổng cộng"), default=0,null=True, blank=False)
    commentaires = models.TextField(verbose_name=(u"Ghi chú"),null=True, blank=True)

    def __unicode__(self):
        return self.nomS