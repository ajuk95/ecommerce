from django.shortcuts import render
from shop.models import Product, Category
from django.db.models import Q

# Create your views here.
def SearchResult(request):
    products = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.filter(Q(name__contains=query) | Q(description__contains=query) | Q(category__name__contains=query))
    return render(request, 'search.html', {'query': query, 'products': products})