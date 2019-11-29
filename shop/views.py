# coding=utf-8
from django.db.models import Prefetch
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from shop.models import ShopType, Shop
from stock.models import Stock


def shoptype_list(request):
    return render(request, 'shop/shoptype_list.html', {
        'shoptypes': ShopType.objects.all(),
        'main_menu_key': 'shoptypes',
    })


class ShopTypeList(ListView):
    model = ShopType
    context_object_name = 'shoptypes'
    template_name = 'shop/shoptype_list.html'

    def get_context_data(self, **kwargs):
        context = super(ShopTypeList, self).get_context_data(**kwargs)
        context['main_menu_key'] = 'shoptypes'
        return context


def shoptype_detail(request, pk):
    return render(request, 'shop/shoptype_detail.html', {
        'shoptype': get_object_or_404(ShopType, pk=pk),
        'main_menu_key': 'shoptypes',
    })


class ShopTypeDetail(DetailView):
    model = ShopType
    context_object_name = 'shoptype'
    template_name = 'shop/shoptype_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ShopTypeDetail, self).get_context_data(**kwargs)
        context['main_menu_key'] = 'shoptypes'
        return context


def shop_list(request):
    return render(request, 'shop/shop_list.html', {
        'shops': Shop.objects.select_related('type', 'city', 'city__country'),
        'main_menu_key': 'shops',
    })


class ShopList(ListView):
    queryset = Shop.objects.select_related('type', 'city', 'city__country')
    context_object_name = 'shops'
    template_name = 'shop/shop_list.html'

    def get_context_data(self, **kwargs):
        context = super(ShopList, self).get_context_data(**kwargs)
        context['main_menu_key'] = 'shops'
        return context


def shop_detail(request, pk):
    qs = Shop.objects.select_related(
        'type', 'owner', 'city', 'city__country'
    ).prefetch_related(
        'sellers', Prefetch('stocks', Stock.objects.select_related('city', 'city__country')),
    )
    return render(request, 'shop/shop_detail.html', {
        'shop': get_object_or_404(qs, pk=pk),
        'main_menu_key': 'shops',
    })


class ShopDetail(DetailView):
    queryset = Shop.objects.select_related(
        'type', 'owner', 'city', 'city__country'
    ).prefetch_related(
        'sellers', Prefetch('stocks', Stock.objects.select_related('city', 'city__country')),
    )
    context_object_name = 'shop'
    template_name = 'shop/shop_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ShopDetail, self).get_context_data(**kwargs)
        # TODO this something doing
        # owner = models.ForenKey()
        # context['main_menu_key'] = 'shops'
        return context


def get_mathematic_result(a, b):
    pass
