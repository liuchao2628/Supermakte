from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# 注册
def reg(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        repassword = request.POST.get('repassword')
        password = request.POST.get('password')

    return render(request, 'user/reg.html')


# 登录

def login(request):
    return render(request, 'user/login.html')


# 个人资料

def infor(request):
    return render(request, 'user/infor.html')


# 个人中心

def member(request):
    return render(request, 'user/member.html')


# 收货地址

def address(request):
    return render(request, 'user/address.html')
