from django.contrib import admin
from django.conf.urls import url
from . import views

# Register your models here.

urlpatterns = [

    url(r'^orders/settlement/$', views.OrderSettlementView.as_view()),  # 订单结算

    url(r'^orders/$', views.SaveOrderView.as_view()),  # 保存订单

]
