from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('description', views.description, name="description"),
    path('cart', views.cart, name="cart"),
    path('cart/remove', views.removefromcart, name="remove"),
    path('cart/checkout', views.checkout, name="checkout"),
    path('cart/checkout/complete', views.completeOrder, name="complete_order"),
    ]