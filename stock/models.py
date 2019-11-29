# coding=utf-8
from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=80, verbose_name=u'название')
    city = models.ForeignKey('place.City', verbose_name=u'город')
    address = models.CharField(max_length=250, verbose_name=u'адрес')

    class Meta:
        verbose_name = u'склад'
        verbose_name_plural = u'склады'
        ordering = ('name',)

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.city)
