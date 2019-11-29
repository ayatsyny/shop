# coding=utf-8
from django.core.urlresolvers import reverse_lazy


MAIN_MENU = (
    ('shops', {'url': reverse_lazy('shop'), 'title': u'Магазины'}),
    ('shoptypes', {'url': reverse_lazy('shoptype'), 'title': u'Типы магазинов'}),
    ('persons', {'url': reverse_lazy('person'), 'title': u'Контактные лица'}),
    ('stocks', {'url': reverse_lazy('stock'), 'title': u'Склады'}),
    ('countries', {'url': reverse_lazy('country'), 'title': u'Страны'}),
    ('cities', {'url': reverse_lazy('city'), 'title': u'Города'}),
)


def main(request):
    return {
        'DEFAULT_TITLE': 'NetShop',
        'MAIN_MENU': MAIN_MENU,
    }
