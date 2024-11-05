from django import forms
from .models import *

class userLoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=50, required=True)
    password = forms.CharField(label="密码", max_length=50, required=True)
    class Meta:
        model = User
        fields = ['username', 'password']

class userRegisterForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=50, required=True)
    password = forms.CharField(label="密码", max_length=50, required=True)
    userType = forms.CharField(label="用户类型", max_length=50, required=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'userType']

class userChangePasswordForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=50, required=True)
    oldPassword = forms.CharField(label="原密码", max_length=50, required=True)
    password = forms.CharField(label="新密码", max_length=50, required=True)
    class Meta:
        model = User
        fields = ['username', 'password']

# class cardRegisterForm(forms.Form):
#     cardId = forms.CharField(label="卡号", max_length=8, required=True)
#     userId = forms.CharField(label="用户ID", max_length=8, required=True)
#     class Meta:
#         model = Contact
#         fields = ['cardId', 'cardBalance']

# class cardChargeForm(forms.Form):
#     cardId = forms.CharField(label="卡号", max_length=8, required=True)
#     cardBalance = forms.FloatField(label="充值金额", required=True)
#     class Meta:
#         model = Contact
#         fields = ['cardId', 'cardBalance']

# class cardConsumeForm(forms.Form):
#     cardId = forms.CharField(label="卡号", max_length=8, required=True)
#     cardBalance = forms.FloatField(label="消费金额", required=True)
#     class Meta:
#         model = Contact
#         fields = ['cardId', 'cardBalance']

# class bookBorrowForm(forms.Form):
#     userId = forms.CharField(label="用户ID", max_length=8, required=True)
#     bookId = forms.UUIDField(label="图书ID", required=True)
#     class Meta:
#         model = Contact
#         fields = ['userId', 'bookId']

# class bookReturnForm(forms.Form):
#     userId = forms.CharField(label="用户ID", max_length=8, required=True)
#     bookId = forms.UUIDField(label="图书ID", required=True)
#     class Meta:
#         model = Contact
#         fields = ['userId', 'bookId']

# class bookAddForm(forms.Form):
#     bookName = forms.CharField(label="书名", max_length=50, required=True)
#     bookAuthor = forms.CharField(label="作者", max_length=50, required=True)
#     bookPrice = forms.FloatField(label="价格", required=True)
#     class Meta:
#         model = Contact
#         fields = ['bookName', 'bookAuthor', 'bookPrice']

# class bookDeleteForm(forms.Form):
#     bookId = forms.UUIDField(label="图书ID", required=True)
#     class Meta:
#         model = Contact
#         fields = ['bookId']

# class bookUpdateForm(forms.Form):
#     bookId = forms.UUIDField(label="图书ID", required=True)
#     bookName = forms.CharField(label="书名", max_length=50, required=True)
#     bookAuthor = forms.CharField(label="作者", max_length=50, required=True)
#     bookPrice = forms.FloatField(label="价格", required=True)
#     class Meta:
#         model = Contact
#         fields = ['bookId', 'bookName', 'bookAuthor', 'bookPrice']

# class goodsAddForm(forms.Form):
#     goodsName = forms.CharField(label="商品名", max_length=50, required=True)
#     goodsPrice = forms.FloatField(label="价格", required=True)
#     goodsAmount = forms.IntegerField(label="数量", required=True)
#     class Meta:
#         model = Contact
#         fields = ['goodsName', 'goodsPrice', 'goodsAmount']

# class goodsDeleteForm(forms.Form):
#     goodsId = forms.UUIDField(label="商品ID", required=True)
#     class Meta:
#         model = Contact
#         fields = ['goodsId']

# class goodsUpdateForm(forms.Form):
#     goodsId = forms.UUIDField(label="商品ID", required=True)
#     goodsName = forms.CharField(label="商品名", max_length=50, required=True)
#     goodsPrice = forms.FloatField(label="价格", required=True)
#     goodsAmount = forms.IntegerField(label="数量", required=True)
#     class Meta:
#         model = Contact
#         fields = ['goodsId', 'goodsName', 'goodsPrice', 'goodsAmount']

# class goodsBuyForm(forms.Form):
#     goodsId = forms.UUIDField(label="商品ID", required=True)
#     goodsAmount = forms.IntegerField(label="数量", required=True)
#     billAmount = forms.FloatField(label="总价", required=True)
#     class Meta:
#         model = Contact
#         fields = ['goodsId', 'goodsAmount', 'billAmount']




