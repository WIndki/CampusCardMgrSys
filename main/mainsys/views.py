from django.shortcuts import render
from .models import *
from .form import *
import uuid
import datetime
from django.http import HttpResponse
# Create your views here.

def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password)
        if user:
            user.update(lastLogin=datetime.datetime.now())
            request.session['user_id'] = user[0].userId
            request.session['is_login'] = True
            request.session.set_expiry(3600)
            response = render(request, 'login.html', {'message': '登录成功', 'status': 'success'})
            response.set_cookie('user_id', user[0].userId, max_age=3600)
            return response
        else:
            return render(request, 'login.html', {'message': '用户名或密码错误', 'status': 'error'})
    else:
        return render(request, 'login.html')

def userRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        userType = request.POST.get('userType')
        user = User.objects.filter(username=username)
        if user:
            return render(request, 'register.html', {'message': '用户名已存在', 'status': 'error'})
        else:
            userId = str(uuid.uuid4())[:10]
            while User.objects.filter(userId=userId):
                userId = str(uuid.uuid4())[:10]
            User.objects.create(userId=userId,username=username, password=password, userType=userType)
            Card.objects.create(cardId=userId, userId=userId, balance=0,cardStatus=True)
            return render(request, 'register.html', {'message': '注册成功', 'status': 'success'})
    else:
        return render(request, 'register.html')

def userChangePassword(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        newPassword = request.POST.get('newPassword')
        user = User.objects.filter(username=username, password=password)
        if user and newPassword!=password and newPassword:
            user.update(password=newPassword)
            return render(request, 'changePassword.html', {'message': '修改成功', 'status': 'success'})
        else:
            return render(request, 'changePassword.html', {'message': '用户名或密码错误', 'status': 'error'})
    else:
        return render(request, 'changePassword.html')

