# coding=utf-8
from django.conf.urls import url
from stock.views import StockList, StockDetail


urlpatterns = [
    url(
        r'^$',
        StockList.as_view(),
        name='stock'
    ),
    url(
        r'^/(?P<pk>\d+)$',
        StockDetail.as_view(),
        name='stock'
    ),
]
