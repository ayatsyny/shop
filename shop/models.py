# coding=utf-8
from django.db import models


class ShopType(models.Model):
    name = models.CharField(max_length=50, verbose_name=u'название')

    class Meta:
        verbose_name = u'тип магазина'
        verbose_name_plural = u'типы магазина'
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class Shop(models.Model):
    type = models.ForeignKey(ShopType, verbose_name=u'тип магазина')
    name = models.CharField(max_length=80, verbose_name=u'название')
    owner = models.ForeignKey('person.Person', verbose_name=u'владелец', related_name='own_shops')
    sellers = models.ManyToManyField('person.Person', verbose_name=u'продавцы', related_name='shops')
    stocks = models.ManyToManyField('stock.Stock', verbose_name=u'склады')
    city = models.ForeignKey('place.City', verbose_name=u'город')
    address = models.CharField(max_length=250, verbose_name=u'адрес')
    website = models.URLField(verbose_name=u'веб-сайт', blank=True)

    class Meta:
        verbose_name = u'магазин'
        verbose_name_plural = u'магазины'
        ordering = ('name',)

    def __unicode__(self):
        return self.name
