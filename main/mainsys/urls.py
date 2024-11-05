from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.userLogin, name='login'),
    path('register/', views.userRegister, name='register'),
    path('changePassword/', views.userChangePassword, name='changePassword'),
    # path('cardRegister/', views.cardRegister, name='cardRegister'),
    # path('cardCharge/', views.cardCharge, name='cardCharge'),
    # path('cardConsume/', views.cardConsume, name='cardConsume'),
    # path('bookBorrow/', views.bookBorrow, name='bookBorrow'),
    # path('bookReturn/', views.bookReturn, name='bookReturn'),
]