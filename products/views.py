from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q
from django.core.paginator import Paginator


def product_list(request):

    query = request.GET.get('q')

    products = Product.objects.all()

    if query:

        products = products.filter(
            Q(title__icontains=query) |
            Q(short_description__icontains=query)
        )

    paginator = Paginator(products, 6)

    page_number = request.GET.get('page')

    products = paginator.get_page(page_number)

    context = {
        'products': products
    }

    return render(
        request,
        'products/product_list.html',
        context
    )

def product_detail(request, slug):

    product = get_object_or_404(
        Product,
        slug=slug
    )

    context = {
        'product': product
    }

    return render(
        request,
        'products/product_detail.html',
        context
    )