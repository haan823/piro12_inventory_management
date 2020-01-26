from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from products.models import Product, Seller


def products_list(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'products_list.html', data)

def products_detail(request, pk):
    product = Product.objects.get(pk=pk)
    data = {
        'product': product
    }
    return render(request, 'products_detail.html', data)

def products_registration(request):
    sellers = Seller.objects.all()
    data = {
        'sellers': sellers
    }
    if request.method == 'POST':
        name = request.POST.get('name', None)
        image = request.FILES.get('image', None)
        detail = request.POST.get('detail', None)
        price = request.POST.get('price', None)
        remaining = request.POST.get('remaining', None)
        seller = request.POST.get('seller', None)
        Product.objects.create(
            name=name,
            image=image,
            detail=detail,
            price=price,
            remaining=remaining,
            seller=Seller.objects.get(pk=seller)
        )
        return redirect(reverse('products-list'))
    elif request.method == 'GET':
        return render(request, 'products_registration.html', data)

def sellers_list(request):
    sellers = Seller.objects.all()
    data = {
        'sellers': sellers
    }
    return render(request, 'sellers_list.html', data)

def sellers_detail(request, pk):
    seller = Seller.objects.get(pk=pk)
    products = Product.objects.all().filter(seller=pk)
    data = {
        'seller': seller,
        'products': products
    }
    return render(request, 'sellers_detail.html', data)

def sellers_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        address = request.POST.get('address', None)
        Seller.objects.create(
            name=name,
            phone=phone,
            address=address
        )
        return redirect(reverse('sellers-list'))
    elif request.method == 'GET':
        return render(request, 'sellers_registration.html')

def products_remaining_plus(request, pk):
    product = Product.objects.get(pk=pk)
    Product.objects.filter(pk=pk).update(remaining=product.remaining+1)
    return redirect(reverse('products-list'))

def products_remaining_minus(request, pk):
    product = Product.objects.get(pk=pk)
    Product.objects.filter(pk=pk).update(remaining=product.remaining-1)
    return redirect(reverse('products-list'))

def products_modify(request, pk):
    product = Product.objects.get(pk=pk)
    sellers = Seller.objects.all()
    data = {
        'product': product,
        'sellers': sellers
    }
    if request.method == 'POST':
        name = request.POST.get('name', None)
        image = request.FILES.get('image', None)
        detail = request.POST.get('detail', None)
        price = request.POST.get('price', None)
        remaining = request.POST.get('remaining', None)
        seller = request.POST.get('seller', None)
        if image:
            Product.objects.filter(pk=pk).update(
            name = name,
            image = image,
            detail = detail,
            price = price,
            remaining = remaining,
            seller = Seller.objects.get(pk=seller)
            )
            return redirect(reverse('products-list'))
        else:
            return render(request, 'products_modify.html', data)
    elif request.method == 'GET':
        return render(request, 'products_modify.html', data)

def products_delete(request, pk):
    Product.objects.get(pk=pk).delete()
    return redirect(reverse('products-list'))

def sellers_modify(request, pk):
    seller = Seller.objects.get(pk=pk)
    data = {
        'seller': seller
    }
    if request.method == 'POST':
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        address = request.POST.get('address', None)
        Seller.objects.filter(pk=pk).update(
            name=name,
            phone=phone,
            address=address
        )
        return redirect(reverse('sellers-list'))
    elif request.method == 'GET':
        return render(request, 'sellers_modify.html', data)

def sellers_delete(request, pk):
    Seller.objects.get(pk=pk).delete()
    return redirect(reverse('sellers-list'))