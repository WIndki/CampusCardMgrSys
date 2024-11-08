from django.db import models
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
import uuid


# Create your models here.

class User(models.Model):
    userId = models.CharField(primary_key=True, validators=[RegexValidator(regex='^.{10}$', message='Length has to be 10', code='nomatch')], max_length=10, null=False, blank=False)
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    password = models.CharField(max_length=50, null=False, blank=False)
    USER_TYPE_CHOICES = [ # 用户类型
        ('admin', '管理员'),
        ('student', '学生'),
        ('staff', '教师'),
    ]
    userType = models.CharField(max_length=50, choices=USER_TYPE_CHOICES)
    lastLogin = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        UserInfo = {
            "userId": self.userId,
            "username": self.username,
            "password": self.password,
            "lastLogin": self.lastLogin
        }
        return str(UserInfo)

class Card(models.Model):
    cardId = models.CharField(primary_key=True,validators=[RegexValidator(regex='^.{10}$', message='Length has to be 8', code='nomatch')], max_length=10, null=False, blank=False)
    userId = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name='ownerId')
    cardBalance = models.FloatField(default=0)
    cardStatus = models.BooleanField()
    def __str__(self):
        CardInfo = {
            "cardId": self.cardId,
            "cardBalance": self.cardBalance,
            "cardStatus": self.cardStatus
        }
        return str(CardInfo)

class book(models.Model):
    bookId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bookName = models.CharField(max_length=50, null=False, blank=False)
    bookImgUrl = models.CharField(max_length=300, null=True, blank=True)
    bookAuthor = models.CharField(max_length=50)
    bookPrice = models.FloatField(validators=[MinValueValidator(0.00)])
    bookStatus = models.BooleanField(default=True)
    def __str__(self):
        BookInfo = {
            "bookId": self.bookId,
            "bookName": self.bookName,
            "bookAuthor": self.bookAuthor,
            "bookPrice": self.bookPrice,
            "bookStock": self.bookStock
        }
        return str(BookInfo)

class borrowLog(models.Model):
    borrowId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    userId = models.ForeignKey(to=User, on_delete=models.CASCADE)
    bookId = models.ForeignKey(to=book, on_delete=models.CASCADE)
    borrowTime = models.DateTimeField()
    returnTime = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        BorrowInfo = {
            "borrowId": self.borrowId,
            "borrowTime": self.borrowTime,
            "returnTime": self.returnTime
        }
        return str(BorrowInfo)

class good(models.Model):
    goodId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    goodName = models.CharField(max_length=50, null=False, blank=False)
    goodImgUrl = models.CharField(max_length=300, null=True, blank=True)
    goodPrice = models.FloatField(validators=[MinValueValidator(0.01)])
    goodAmount = models.IntegerField()
    def __str__(self):
        GoodsInfo = {
            "goodId": self.goodsId,
            "goodName": self.goodsName,
            "goodPrice": self.goodsPrice,
            "goodStatus": self.goodsStatus
        }
        return str(GoodsInfo)

class billLog(models.Model):
    billId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cardId = models.ForeignKey(to=Card, on_delete=models.CASCADE)
    billType = models.CharField(max_length=50)
    billAmount = models.FloatField()
    billTime = models.DateTimeField()
    def __str__(self):
        BillInfo = {
            "billId": self.billId,
            "billType": self.billType,
            "billAmount": self.billAmount,
            "billTime": self.billTime
        }
        return str(BillInfo)




