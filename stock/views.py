# coding=utf-8
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from stock.models import Stock


def stock_list(request):
    return render(request, 'stock/stock_list.html', {
        'stocks': Stock.objects.select_related('city', 'city__country'),
        'main_menu_key': 'stocks',
    })


class StockList(ListView):
    queryset = Stock.objects.select_related('city', 'city__country')
    context_object_name = 'stocks'
    template_name = 'stock/stock_list.html'

    def get_context_data(self, **kwargs):
        context = super(StockList, self).get_context_data(**kwargs)
        context['main_menu_key'] = 'stocks'
        return context


def stock_detail(request, pk):
    return render(request, 'stock/stock_detail.html', {
        'stock': get_object_or_404(Stock.objects.select_related('city', 'city__country'), pk=pk),
        'main_menu_key': 'stocks',
    })


class StockDetail(DetailView):
    queryset = Stock.objects.select_related('city', 'city__country')
    context_object_name = 'stock'
    template_name = 'stock/stock_detail.html'

    def get_context_data(self, **kwargs):
        context = super(StockDetail, self).get_context_data(**kwargs)
        context['main_menu_key'] = 'stocks'
        return context
