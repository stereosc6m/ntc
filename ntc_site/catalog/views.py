from django.shortcuts import render, get_object_or_404
from django.conf import settings

from .models import Product

def catalog(request):
    template_name = 'catalog/catalog.html'
    products = Product.objects.values(
        'title',
        'text',
        'image',
        'id',
    ).order_by('-created_at')
    context = {
        'products': products,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, template_name, context)

def product_detail(request, pk):
    template_name = 'catalog/product_detail.html'
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product,
        'MEDIA_URL': settings.MEDIA_URL,
    }
    return render(request, template_name, context)