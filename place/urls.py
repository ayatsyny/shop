# coding=utf-8
from django.conf.urls import url, include
from place.views import CountryList, CountryDetail, CityList, CityDetail


urlpatterns = [
    url(
        r'^/country', include([
            url(
                r'^$',
                CountryList.as_view(),
                name='country'
            ),
            url(
                r'^/(?P<pk>\d+)$',
                CountryDetail.as_view(),
                name='country'
            ),
        ])
    ),
    url(
        r'^/city', include([
            url(
                r'^$',
                CityList.as_view(),
                name='city'
            ),
            url(
                r'^/(?P<pk>\d+)$',
                CityDetail.as_view(),
                name='city'
            ),
        ])
    ),
]
