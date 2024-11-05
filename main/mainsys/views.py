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
            return render(request, 'login.html', {'message': '登录成功'})
        else:
            return render(request, 'login.html', {'message': '用户名或密码错误'})
    else:
        return render(request, 'login.html')

def userRegister(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        userType = request.POST.get('userType')
        user = User.objects.filter(username=username)
        if user:
            return render(request, 'register.html', {'message': '用户名已存在'})
        else:
            userId = str(uuid.uuid4())[:10]
            User.objects.create(userId=userId,username=username, password=password, userType=userType)
            return render(request, 'register.html', {'message': '注册成功'})
    else:
        return render(request, 'register.html')

def userChangePassword(request):
    if request.method == 'POST':
        changePasswordFrom = userChangePasswordForm(request.POST)
        if changePasswordFrom.is_valid():
            username = changePasswordFrom.cleaned_data['username']
            oldPassword = changePasswordFrom.cleaned_data['oldPassword']
            newPassword = changePasswordFrom.cleaned_data['newPassword']
            try:
                user = User.objects.get(username=username)
                if user.check.password(oldPassword):
                    user.password = newPassword
                    user.save()
                    return render(request, 'changePassword.html', {'message': '修改成功'})
                else:
                    return render(request, 'changePassword.html', {'message': '原密码错误'})
            except:
                return render(request, 'changePassword.html', {'message': '用户名不存在'})
    else:
        return render(request, 'changePassword.html')

