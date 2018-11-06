from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^cart/$', views.CartView.as_view()),  # 购物车增、删、改、查

    url(r'^cart/selection/$', views.CartView.as_view()),    # 购物车全选
]