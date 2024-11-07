from django.shortcuts import render,redirect
from .models import *
from .form import *
import uuid
import datetime
from django.http import HttpResponse
# Create your views here.

def alive_session(request):
    if request.session.get('is_login', None) and request.COOKIES.get('user_id') == request.session.get('user_id', None):
        user = User.objects.filter(userId=request.session.get('user_id'))
        card = Card.objects.filter(cardId=request.session.get('user_id'))
        if user and card:
            return True
    return False

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

def userLogout(request):
    response = redirect('/login/')
    response.delete_cookie('user_id')
    request.session.flush()
    return response

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
            temp_user = User.objects.create(userId=userId,username=username, password=password, userType=userType)
            Card.objects.create(cardId=userId, userId=temp_user, cardBalance=0,cardStatus=True)
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

def index(request):
    if alive_session(request):
        user_id = request.COOKIES.get('user_id')
        user = User.objects.filter(userId=user_id)[0]
        cards = Card.objects.filter(cardId=user_id)
        return render(request, 'index.html', {'user': user, 'cards': cards})
    else:
        return redirect('/login/')

def cardBill(request):
    if alive_session(request):
        user_id = request.COOKIES.get('user_id')
        user = User.objects.filter(userId=user_id)[0]
        cards = Card.objects.filter(cardId=user_id)
        bills = []
        for card in cards:
            billlogs = billLog.objects.filter(cardId=card.cardId)
            bills.extend(billlogs)
        return render(request, 'cardBill.html', {'user': user, 'cards': cards, 'bills': bills})
    else:
        return redirect('/login/')

def account(request):
    if alive_session(request):
        user_id = request.COOKIES.get('user_id')
        user = User.objects.filter(userId=user_id)[0]
        cards = Card.objects.filter(cardId=user_id)
        return render(request, 'account.html', {'user': user, 'cards': cards})
    else:
        return redirect('/login/')

