from django.conf.urls import url

from user.views import reg, login, infor, member, address

urlpatterns = [
    url(r'^reg/$', reg, name='注册'),
    url(r'^login/$', login, name='登录'),
    url(r'^infor/$', infor, name='个人资料'),
    url(r'^member/$', member, name='个人中心'),
    url(r'^address/$', address, name='收货地址'),

]
