# coding=utf-8
from django.db import models


class Person(models.Model):
    SEX_MALE = 0
    SEX_FEMALE = 1
    SEX_CHOICES = (
        (SEX_MALE, u'мужской'),
        (SEX_FEMALE, u'женский'),
    )
    first_name = models.CharField(max_length=80, verbose_name=u'имя')
    last_name = models.CharField(max_length=80, verbose_name=u'фамилия')
    sex = models.SmallIntegerField(verbose_name=u'пол', choices=SEX_CHOICES)
    birth_date = models.DateField(verbose_name=u'дата рождения')
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = u'контактное лицо'
        verbose_name_plural = u'контактные лица'
        ordering = ('first_name', 'last_name')

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        return u'{} {}'.format(self.first_name, self.last_name)
