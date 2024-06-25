from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name="homepage"),
    path('lumiar/', lumiar, name="lumiar"),
    path('olivais/', olivais, name="olivais"),
    path('alvalade/', alvalade, name="alvalade"),
    path('minhaconta/', minha_conta, name="minha_conta"),
    path('login/', login, name="login"),
    path('carrinho/', carrinho, name="carrinho"),
    path('checkout/', checkout, name="checkout")
]