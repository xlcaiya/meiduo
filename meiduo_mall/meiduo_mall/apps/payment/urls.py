from django.contrib import admin
from django.conf.urls import url

# Register your models here.
from . import views

urlpatterns = [
    url(r'^orders/(?P<order_id>\d+)/payment/$', views.PaymentView.as_view()),   # 发起支付

    url(r'^payment/status/$', views.PaymentStatusView.as_view()),   # 保存支付结果

]