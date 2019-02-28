from django.db import models

# Create your models here.
class Wheel(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

class Nav(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

class Mustbuy(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

class Shop(models.Model):
    img = models.CharField(max_length=150)
    name = models.CharField(max_length=20)
    trackid = models.CharField(max_length=20)

class MainShow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

# Catagory Model
class FoodTypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=20)
    typesort = models.IntegerField()
    childtypenames = models.CharField(max_length=150)
# Items Model
class Goods(models.Model):
    # Items id
    productid = models.CharField(max_length=10)
    # Items image
    productimg = models.CharField(max_length=150)
    # Items name
    productname = models.CharField(max_length=50)
    # Items long name
    productlongname = models.CharField(max_length=100)
    # recommendation
    isxf = models.NullBooleanField(default=False)
    # BOGO Free
    pmdesc = models.CharField(max_length=10)
    # Size
    specifics = models.CharField(max_length=20)
    # Price
    price = models.CharField(max_length=10)
    # Super Market Price
    marketprice = models.CharField(max_length=10)
    #  Group id
    categoryid = models.CharField(max_length=10)
    # Child catagory id
    childcid = models.CharField(max_length=10)
    # Child catagory name
    childcidname = models.CharField(max_length=10)
    # Details page id
    dealerid = models.CharField(max_length=10)
    # Stock
    storenums = models.IntegerField()
    # Sales
    productnum = models.IntegerField()



# User Model
class User(models.Model):
    # User Account(sole)
    userAccount = models.CharField(max_length=20,unique=True)
    # Password
    userPasswd  = models.CharField(max_length=20)
    # Nickname
    userName    =  models.CharField(max_length=20)
    # Phone Number
    userPhone   = models.CharField(max_length=20)
    # Address
    userAdderss = models.CharField(max_length=100)
    # Portrait Path
    userImg     = models.CharField(max_length=150)
    # Grades
    userRank    = models.IntegerField()
    # touken validation，upgrade after login
    userToken   = models.CharField(max_length=50)
    @classmethod
    def createuser(cls,account,passwd,name,phone,address,img,rank,token):
        u = cls(userAccount = account,userPasswd = passwd,userName=name,userPhone=phone,userAdderss=address,userImg=img,userRank=rank,userToken=token)
        return u

class CartManager1(models.Manager):
    def get_queryset(self):
        return super(CartManager1, self).get_queryset().filter(isDelete=False)
class CartManager2(models.Manager):
    def get_queryset(self):
        return super(CartManager2, self).get_queryset().filter(isDelete=True)
class Cart(models.Model):
    userAccount = models.CharField(max_length=20)
    productid = models.CharField(max_length=10)
    productnum = models.IntegerField()
    productprice = models.CharField(max_length=10)
    isChose = models.BooleanField(default=True)
    productimg = models.CharField(max_length=150)
    productname = models.CharField(max_length=100)
    orderid = models.CharField(max_length=20,default="0")
    isDelete = models.BooleanField(default=False)
    objects = CartManager1()
    obj2 = CartManager2()
    @classmethod
    def createcart(cls,userAccount,productid,productnum,productprice,isChose,productimg,productname,isDelete):
        c = cls(userAccount = userAccount,productid = productid,productnum=productnum,productprice=productprice,isChose=isChose,productimg=productimg,productname=productname,isDelete=isDelete)
        return c
