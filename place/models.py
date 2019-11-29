# coding=utf-8
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=80, verbose_name=u'название')

    class Meta:
        verbose_name = u'страна'
        verbose_name_plural = u'страны'
        ordering = ('name',)

    def __unicode__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, verbose_name=u'страна')
    name = models.CharField(max_length=80, verbose_name=u'название')

    class Meta:
        verbose_name = u'город'
        verbose_name_plural = u'города'
        ordering = ('name',)

    def __unicode__(self):
        return u'{} ({})'.format(self.name, self.country)
