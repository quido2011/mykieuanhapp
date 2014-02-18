# -*- encoding: UTF-8 -*-
from django.db import models

# Create your models here.
class Client(models.Model):
    nomClient = models.CharField(verbose_name=(u"Tên khách hàng"),unique=True, max_length=200, null=False, blank=False)
    telClient = models.CharField(verbose_name=(u"Điện thoại KH"), max_length=50, null=False, blank=False)

    def __unicode__(self):
        return self.nomClient