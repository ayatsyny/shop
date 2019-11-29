# coding=utf-8
from django.contrib import admin
from place.models import Country, City


admin.site.register((Country, City))
