from django.shortcuts import render,redirect
from .models import Wheel,Nav,Mustbuy,Shop,MainShow,FoodTypes,Goods,User,Cart
from django.http import JsonResponse
import os
from .forms.login import LoginForm
from django.http import HttpResponse
import time
import random
from django.conf import settings
from django.contrib.auth import logout

# Create your views here.
def home(request):
    wheelsList = Wheel.objects.all()
    navList = Nav.objects.all()
    mustbuyList = Mustbuy.objects.all()
    shopList = Shop.objects.all()
    shop1 = shopList[0]
    shop2 = shopList[1:3]
    shop3 = shopList[3:7]
    shop4 = shopList[7:11]
    mainList = MainShow.objects.all()

    return render(request, 'axf/home.html', {"title":"Homepage", "wheelsList":wheelsList,
                  "navList":navList, "mustbuyList":mustbuyList,"shop1":shop1,"shop2":shop2,
                                             "shop3":shop3,"shop4":shop4,"mainList":mainList})

def market(request, categoryid, cid, sortid):
    leftSlider = FoodTypes.objects.all()
    if cid == '0':
        productList = Goods.objects.filter(categoryid=categoryid)
    else:
        productList = Goods.objects.filter(categoryid=categoryid, childcid = cid)

    if sortid == '1':
        productList = productList.order_by("productnum")
    elif sortid == '2':
        productList = productList.order_by("price")
    elif sortid == '3':
        productList = productList.order_by("-price")

    group = leftSlider.get(typeid = categoryid)
    childList = []
    childnames = group.childtypenames
    arr1 = childnames.split("#")
    for str in arr1:
        arr2 = str.split(":")
        obj = {"childName": arr2[0], "childId": arr2[1]}
        childList.append(obj)

    return render(request, 'axf/market.html',{"title":"Delivery Super Market","leftSlider":leftSlider,
                                              "productList":productList,"childList":childList,"categoryid":categoryid,
                                              "cid":cid})

def cart(request):
    return render(request, 'axf/cart.html',{"title":"Cart"})
def changecart(request, flag):
    token = request.session.get("token")
    if token == None:
        return JsonResponse({"data":-1,"status":"error"})
    productid = request.POST.get("productid")
    user = User.objects.get(userToken = token)

    if flag == '0':
        carts = Cart.objects.filter(userAccount = user.userAccount)
        c = None
        if carts.count() == 0:
            if product.storenums == 0;
                return JsonResponse({"data":-2,"status":"error"})
            c = Cart.createcart(user.userAccount,productid,1,product.price,
                                True,product.productimg,product.productlongname,False)
            c.save()
            pass
        else:
            c = carts.get(productid = productid)
            c.productnum += 1
            c.productprice = "%.2f"%(float(product.price) * onecart.productnum)
            c.save()
            except Cart.DoesNotExist as e:
                c = Cart.createcart(user.userAccount,productid,1,product.price,
                                True,product.productimg,product.productlongname,False)

    elif flag == '1':
        carts = Cart.objects.filter(userAccount = user.userAccount)
        c = None
        if carts.count() == 0:
            return JsonResponse({"data":-2, "status":"error"})
        else:
            try:
                c = carts.get(productid = productid)
                c.productnum += 1
                c.productprice = "%.2f"%(float(product.price) * onecart.productnum)

                if c.productnum == 0:
                    c.delete()
                else:
                    c.save()
    elif flag == '2':
        pass
    elif flag == '3':
        pass


    else:
        pass

def mine(request):
    username = request.session.get("username","not login")
    return render(request, 'axf/mine.html',{"title":"Mine"})


def login(request):
    if request.method == "POST":
        f = LoginForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data["username"]
            pswd = f.cleaned_data["passwd"]
            try:
                user = User.objects.get(userAccount = nameid)
                if user.userPasswd != pswd:

            except User.DoesNotExist as e:

            token = time.time() + random.randrange(1, 1000000)
            user.userToken = str(token)
            user.save()
            request.sessions["username"] = user.userName
            request.sessions["token"] = user.userToken
            return redirect("/mine/")
        else:
            return render(request, 'axf/login.html', {"title": "login", "form":f,
                                                      "error":f.errors})
    else:
        f = LoginForm()
    return render(request, 'axf/login.html', {"title":"login","form":f})

def register(request):
    if request.method == "POST":
        userAccount = request.POST.get("userAccount")
        userPasswd = request.POST.get("userPasswd")
        userName = request.POST.get("userName")
        userPhone = request.POST.get("userPhone")
        userAddress = request.POST.get("userAddress")
        userRank = 0

        f = request.FILES["userImg"]
        userImg = os.path.join(settings.MDEIA_ROOT, userAccount + ".png")
        with open(userImg, "wb") as fp:
            for data in f.chunks():
                fp.write(data)

        user = User.createuser(userAccount,userPasswd,userName,userPhone,userAddress,
                               userRank,userImg,userToken)

        return redirect('/mine/')
    else:
        return render(request, 'axf/register.html', {"title":"register"})

def quit(request):
    logout(request)
    return redirect('/mine/')

def checkuserid(request):
    userid = request.POST.get("userid")
    try:
        user = User.objects.get(userAccount = userid)
        return JsonResponse({"data":"already registered", "status":"error"})
    except User.DoesNotExist as e:
        return JsonResponse({"data":"ok", "status":"success"})

