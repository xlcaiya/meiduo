"""meiduo_mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),   # 管理员

    url(r'^', include('users.urls')),

    url(r'^sms_codes/', include('verifications.urls')),

    url(r'^oauth/', include('oauth.urls'), name='oauth'),

    url(r'^', include('areas.urls')),  # 用户地址

    url(r'^ckeditor/', include('ckeditor_uploader.urls')),  # 富文本编辑器

    url(r'^', include('goods.urls')),  # 商品搜索

    url(r'^', include('carts.urls')),  # 购物车

    url(r'^', include('orders.urls')),  # 订单详情

    url(r'^', include('payment.urls')),  # 第三方支付: 支付宝

]
