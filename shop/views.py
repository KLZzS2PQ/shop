from django.shortcuts import render, redirect

from shop.models import Product, Order


def catalog(request):
    return render(request, 'shop/catalog.html', {
        'products': Product.objects.all()
    })


def order_create(request, id):
    if request.method == 'POST':
        Order.objects.create(
            product_id=id,
            delivery_address=request.POST['delivery_address']
        )
        return redirect('orders')
    return render(request, 'shop/order_create.html', {
        'product': Product.objects.get(id=id)
    })


def orders(request):
    orders_list = Order.objects.all()
    return render(request, 'shop/orders.html',
                  context={'orders': orders_list})


def product_info(request, id):
    return render(request, 'shop/product_info.html', {
        'product': Product.objects.get(id=id)
    })
