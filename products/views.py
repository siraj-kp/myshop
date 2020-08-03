from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product, Order


def cartItems(cart):
    items = []
    for item in cart:
        items.append(Product.objects.get(id=item))
    return items


def genItemsList(cart):
    cart_items = cartItems(cart)
    item_list = ""
    for item in cart_items:
        item_list += str(item.name)
        item_list += ","
    return item_list


def priceCart(cart):
    cart_items = cartItems(cart)
    price = 0
    for item in cart_items:
        price += item.price
    return price


def index(request):
    if 'cart' not in request.session:
        request.session['cart'] = []
    cart = request.session['cart']
    request.session.set_expiry(0)
    products = Product.objects.all()
    ctx = {'products': products, 'cart_size': len(cart)}

    if request.method == "POST":
        cart.append(int(request.POST['obj_id']))
        return redirect('index')
    return render(request, "products/index.html", ctx)


def description(request):


    return render(request, "products/description.html",)


def cart(request):
    cart = request.session['cart']
    request.session.set_expiry(0)
    ctx = {'cart': cart, 'cart_size': len(cart), 'cart_items': cartItems(cart),
           'total_price': priceCart(cart)}
    return render(request, "products/cart.html", ctx)


def removefromcart(request):
    request.session.set_expiry(0)
    obj_to_remove = int(request.POST['obj_id'])
    obj_index = request.session['cart'].index(obj_to_remove)
    request.session['cart'].pop(obj_index)
    return redirect('cart')


def checkout(request):
    request.session.set_expiry(0)
    cart = request.session['cart']
    ctx = {'cart': cart, 'cart_size': len(cart), 'cart_items': cartItems(cart), 'total_price': priceCart(cart)}
    return render(request, "products/checkout.html", ctx)


def completeOrder(request):
    request.session.set_expiry(0)
    cart = request.session['cart']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    address = request.POST['address']
    city = request.POST['city']
    phone = request.POST['phone']
    total = request.POST['total']
    item_name = request.POST['item_name']
    order_info = Order(first_name=first_name, last_name=last_name, address=address, city=city, phone=phone, total=total, item_name=item_name)
    order_info.save()
    Order.items = genItemsList(cart)
    request.session['cart'] = []
    return render(request, "products/complete_order.html")





