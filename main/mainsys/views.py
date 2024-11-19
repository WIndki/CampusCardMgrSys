from django.shortcuts import render, redirect, get_object_or_404  # 导入Django的快捷方法
from django.views.decorators.csrf import csrf_exempt, csrf_protect  # 导入CSRF装饰器
from .models import User, Card, billLog, good  # 导入模型
from .form import *  # 导入表单
import uuid  # 导入UUID模块
import datetime  # 导入日期时间模块
from django.http import HttpResponse  # 导入HttpResponse
import json  # 导入JSON模块
from django.db.models import Q  # 导入Q对象

# 创建视图

def alive_session(request):  # 检查会话是否有效
    if request.session.get('is_login', None) and request.COOKIES.get('user_id') == request.session.get('user_id', None):  # 检查会话和Cookie中的用户ID是否匹配
        user_exists = User.objects.filter(userId=request.session.get('user_id'))  # 检查用户是否存在
        card_exists = Card.objects.filter(userId=request.session.get('user_id'))  # 检查卡片是否存在
        if user_exists:  # 如果用户存在
            return True  # 返回True
    return False  # 返回False

def recordBill(card, amount, billType):  # 记录账单
    try:
        billLog.objects.create(cardId=card, billType=billType, billAmount=amount, billTime=datetime.datetime.now())  # 创建账单记录
        return True  # 返回True
    except Exception as e:  # 捕获异常
        print(e)  # 打印异常
        return False  # 返回False

def userLogin(request):  # 用户登录
    if request.method == 'POST':  # 如果请求方法是POST
        username = request.POST.get('username')  # 获取用户名
        password = request.POST.get('password')  # 获取密码
        user = User.objects.filter(username=username, password=password).first()  # 查询用户
        if user:  # 如果用户存在
            user.lastLogin = datetime.datetime.now()  # 更新最后登录时间
            user.save()  # 保存用户
            request.session['user_id'] = user.userId  # 设置会话中的用户ID
            request.session['is_login'] = True  # 设置会话中的登录状态
            request.session.set_expiry(3600)  # 设置会话过期时间
            response = render(request, 'login.html', {'message': '登录成功', 'status': 'success'})  # 渲染登录成功页面
            response.set_cookie('user_id', user.userId, max_age=3600)  # 设置Cookie
            return response  # 返回响应
        else:  # 如果用户不存在
            return render(request, 'login.html', {'message': '用户名或密码错误', 'status': 'error'})  # 渲染登录失败页面
    return render(request, 'login.html')  # 渲染登录页面

def userLogout(request):  # 用户登出
    response = redirect('/login/')  # 重定向到登录页面
    response.delete_cookie('user_id')  # 删除Cookie
    request.session.flush()  # 清空会话
    return response  # 返回响应

def userRegister(request):  # 用户注册
    if request.method == 'POST':  # 如果请求方法是POST
        username = request.POST.get('username')  # 获取用户名
        password = request.POST.get('password')  # 获取密码
        userType = request.POST.get('userType')  # 获取用户类型
        if User.objects.filter(username=username).exists():  # 如果用户名已存在
            return render(request, 'register.html', {'message': '用户名已存在', 'status': 'error'})  # 渲染注册失败页面
        else:  # 如果用户名不存在
            userId = str(uuid.uuid4())[:10]  # 生成用户ID
            while User.objects.filter(userId=userId).exists():  # 如果用户ID已存在
                userId = str(uuid.uuid4())[:10]  # 重新生成用户ID
            temp_user = User.objects.create(userId=userId, username=username, password=password, userType=userType)  # 创建用户
            Card.objects.create(cardId=userId, userId=temp_user, cardBalance=0, cardStatus=True)  # 创建卡片
            return render(request, 'register.html', {'message': '注册成功', 'status': 'success'})  # 渲染注册成功页面
    return render(request, 'register.html')  # 渲染注册页面

def userChangePassword(request):  # 用户修改密码
    if request.method == 'POST':  # 如果请求方法是POST
        username = request.POST.get('username')  # 获取用户名
        password = request.POST.get('password')  # 获取密码
        newPassword = request.POST.get('newPassword')  # 获取新密码
        user = User.objects.filter(username=username, password=password).first()  # 查询用户
        if user and newPassword != password and newPassword:  # 如果用户存在且新密码不等于旧密码且新密码不为空
            user.password = newPassword  # 更新密码
            user.save()  # 保存用户
            return render(request, 'changePassword.html', {'message': '修改成功', 'status': 'success'})  # 渲染修改成功页面
        else:  # 如果用户不存在或新密码等于旧密码或新密码为空
            return render(request, 'changePassword.html', {'message': '用户名或密码错误', 'status': 'error'})  # 渲染修改失败页面
    return render(request, 'changePassword.html')  # 渲染修改密码页面

def index(request):  # 首页
    if alive_session(request):  # 如果会话有效
        user_id = request.COOKIES.get('user_id')  # 获取用户ID
        user = get_object_or_404(User, userId=user_id)  # 获取用户
        cards = Card.objects.filter(userId=user_id)  # 获取用户的卡片
        return render(request, 'index.html', {'user': user, 'cards': cards})  # 渲染首页
    return redirect('/login/')  # 重定向到登录页面

def cardBill(request):  # 卡片账单
    if alive_session(request):  # 如果会话有效
        user_id = request.COOKIES.get('user_id')  # 获取用户ID
        user = get_object_or_404(User, userId=user_id)  # 获取用户
        cards = Card.objects.filter(userId=user_id)  # 获取用户的卡片
        bills = billLog.objects.filter(cardId__in=[card.cardId for card in cards])  # 获取卡片的账单
        return render(request, 'cardBill.html', {'user': user, 'cards': cards, 'bills': bills})  # 渲染卡片账单页面
    return redirect('/login/')  # 重定向到登录页面

def account(request):  # 账户页面
    if alive_session(request):  # 如果会话有效
        user_id = request.COOKIES.get('user_id')  # 获取用户ID
        user = get_object_or_404(User, userId=user_id)  # 获取用户
        cards = Card.objects.filter(userId=user_id)  # 获取用户的卡片
        bills = billLog.objects.filter(cardId__in=[card.cardId for card in cards])  # 获取卡片的账单
        for bill in bills:  # 遍历账单
            bill.billType = '充值' if bill.billType == 'charge' else '消费'  # 转换账单类型
            bill.billTime = bill.billTime.strftime('%Y-%m-%d %H:%M:%S')  # 格式化账单时间
        bills = sorted(bills, key=lambda x: x.billTime, reverse=True)  # 按时间倒序排序账单
        message = request.session.pop('message', None)  # 获取会话中的消息
        return render(request, 'account.html', {'user': user, 'cards': cards, 'bills': bills, 'message': message, 'status': 'success' if message else None})  # 渲染账户页面
    return redirect('/login/')  # 重定向到登录页面

def cardCharge(request):  # 卡片充值
    if alive_session(request) and request.method == "POST":  # 如果会话有效且请求方法是POST
        chargeCardId = request.POST.get('cardId')  # 获取充值卡片ID
        chargeUserId = request.POST.get('userId')  # 获取充值用户ID
        chargeMoney = request.POST.get('chargeMoney')  # 获取充值金额
        card = get_object_or_404(Card, cardId=chargeCardId)  # 获取卡片
        if chargeUserId == card.userId.userId:  # 如果充值用户ID等于卡片用户ID
            card.cardBalance += float(chargeMoney)  # 增加卡片余额
            card.save()  # 保存卡片
            recordBill(card, chargeMoney, 'charge')  # 记录账单
            request.session['message'] = '充值成功'  # 设置会话中的消息
            return redirect('/account/')  # 重定向到账户页面
        request.session['message'] = '充值失败'  # 设置会话中的消息
        return redirect('/account/')  # 重定向到账户页面
    return redirect('/login/')  # 重定向到登录页面

def shop(request):  # 商店页面
    if alive_session(request):  # 如果会话有效
        user_id = request.COOKIES.get('user_id')  # 获取用户ID
        user = get_object_or_404(User, userId=user_id)  # 获取用户
        cards = Card.objects.filter(userId=user_id)  # 获取用户的卡片
        goods = good.objects.filter(goodAmount__gt=0)  # 获取库存大于0的商品
        return render(request, 'shop.html', {'user': user, 'cards': cards, 'goods': goods})  # 渲染商店页面
    return redirect('/login/')  # 重定向到登录页面

def shopAPI(request):  # 商店API
    if alive_session(request) and request.method == "POST":  # 如果会话有效且请求方法是POST
        user_id = request.COOKIES.get('user_id')  # 获取用户ID
        user = get_object_or_404(User, userId=user_id)  # 获取用户
        cards = Card.objects.filter(cardId=user_id)  # 获取用户的卡片
        try:
            messageBody = json.loads(request.body.decode('utf-8'))  # 解析请求体
            payCard = messageBody.get('cardId')  # 获取支付卡片ID
            items = messageBody.get('cartItems')  # 获取购物车商品
            if any(card.cardId == payCard for card in cards):  # 如果支付卡片ID在用户的卡片中
                card = get_object_or_404(Card, cardId=payCard)  # 获取卡片
                item_dict = {}  # 创建商品字典
                for item in items:  # 遍历商品
                    if item['id'] in item_dict:  # 如果商品ID在字典中
                        item_dict[item['id']]['quantity'] += 1  # 增加商品数量
                    else:  # 如果商品ID不在字典中
                        item_dict[item['id']] = {'id': item['id'], 'quantity': 1}  # 添加商品到字典
                items = list(item_dict.values())  # 转换字典为列表
                unEnough = []  # 创建库存不足列表
                for item in items:  # 遍历商品
                    item_object = get_object_or_404(good, goodId=item['id'])  # 获取商品
                    if item_object.goodAmount >= item['quantity'] and card.cardBalance >= float(item_object.goodPrice * item['quantity']):  # 如果商品库存足够且卡片余额足够
                        item_object.goodAmount -= item['quantity']  # 减少商品库存
                        card.cardBalance -= float(item_object.goodPrice * item['quantity'])  # 减少卡片余额
                        recordBill(card, float(item_object.goodPrice * item['quantity']), '购物')  # 记录账单
                        item_object.save()  # 保存商品
                        card.save()  # 保存卡片
                    else:  # 如果商品库存不足或卡片余额不足
                        unEnough.append(item)  # 添加商品到库存不足列表
                if not unEnough:  # 如果库存不足列表为空
                    return HttpResponse(json.dumps({'message': 'success'}), content_type="application/json", status=200)  # 返回成功响应
                return HttpResponse(json.dumps({'message': '购买失败，可能是余额不足或库存不足'}), content_type="application/json", status=200)  # 返回失败响应
        except json.JSONDecodeError:  # 捕获JSON解析错误
            return HttpResponse(json.dumps({'message': 'Invalid JSON'}), content_type="application/json", status=200)  # 返回无效JSON响应
    return redirect('/shop/')  # 重定向到商店页面