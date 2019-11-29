# coding=utf-8
from django.conf.urls import include, url
from django.contrib import admin
from django.templatetags.static import static
from django.views.generic import TemplateView, RedirectView


urlpatterns = [
    url(
        r'^$',
        TemplateView.as_view(template_name='netshop/main.html'),
        name='main'
    ),
    url(
        r'^admin',
        include(admin.site.urls)
    ),
    url(
        r'^person',
        include('person.urls')
    ),
    url(
        r'^place',
        include('place.urls')
    ),
    url(
        r'^stock',
        include('stock.urls')
    ),
    url(
        r'^shop',
        include('shop.urls')
    ),
    url(
        r'^favicon\.ico$',
        RedirectView.as_view(url=static('netshop/img/favicon.ico'))
    ),
]
