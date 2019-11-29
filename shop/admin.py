from django.contrib import admin
from shop.models import ShopType, Shop


admin.site.register((ShopType, Shop))
