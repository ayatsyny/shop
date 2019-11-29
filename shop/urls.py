# coding=utf-8
from django.conf.urls import url, include
from shop.views import ShopTypeList, ShopTypeDetail, ShopList, ShopDetail


urlpatterns = [
    url(
        r'^/shoptype', include([
            url(
                r'^$',
                ShopTypeList.as_view(),
                name='shoptype'
            ),
            url(
                r'^/(?P<pk>\d+)$',
                ShopTypeDetail.as_view(),
                name='shoptype'
            ),
        ])
    ),
    url(
        r'^/shop', include([
            url(
                r'^$',
                ShopList.as_view(),
                name='shop'
            ),
            url(
                r'^/(?P<pk>\d+)$',
                ShopDetail.as_view(),
                name='shop'
            ),
        ])
    ),
]
