from django.contrib import admin
from django.urls import path
from .import views
from .views.home import Index
from .views.signup import Signup
from .views.login import Login,logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import Order, OrderView
# from .views.team import Team



urlpatterns = [
    path("",Index.as_view(),name="homepage"),
    path('signup/',Signup.as_view(), name='signup'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',logout,name='logout'),
    path('cart/',Cart.as_view(),name='cart'),
    path('check-out/',CheckOut.as_view(),name='checkout'),
    path('orders/',OrderView.as_view(),name='orders'),
    # path('team/',Team.as_view(),name='team'),
    # path('status/',status,name="status")
]
