from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.userLogin, name='login'),
    path('logout/',views.userLogout, name='logout'),
    path('register/', views.userRegister, name='register'),
    path('changepassword/', views.userChangePassword, name='changePassword'),
    path('index/', views.index, name='index'),
    path('account/', views.account, name='account'),
    # path('cardRegister/', views.cardRegister, name='cardRegister'),
    path('cardCharge/', views.cardCharge, name='cardCharge'),
    path('shop/', views.shop, name='shop'),
    path('shop/api/', views.shopAPI, name='shopAPI'),
    path('library/', views.library, name='library'),
    path('library/borrow/', views.library_borrow, name='library_borrow'),
    path('library/return/', views.library_return, name='library_return'),
    path('library/renew/', views.library_renew, name='library_renew'),
    # path('cardConsume/', views.cardConsume, name='cardConsume'),
    # path('bookBorrow/', views.bookBorrow, name='bookBorrow'),
    # path('bookReturn/', views.bookReturn, name='bookReturn'),
]