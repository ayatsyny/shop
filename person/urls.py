# coding=utf-8
from django.conf.urls import url
from person.views import PersonList, PersonDetail


urlpatterns = [
    url(
        r'^$',
        PersonList.as_view(),
        name='person'
    ),
    url(
        r'^/(?P<pk>\d+)$',
        PersonDetail.as_view(),
        name='person'
    ),
]
