from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    url(r'^emails/verification/$', views.VerifyEmailView.as_view()), # 邮箱验证

    url(r'^emails/$', views.EmailView.as_view()),  # 设置邮箱

    url(r'^user/$', views.UserDetailView.as_view()),    # 用户中心个人信息

    url(r'^users/$', views.UserRegisterView.as_view()), # 用户注册

    url(r'^usernames/(?P<username>\w{5,20})/count/$', views.UsernameCountView.as_view()),

    url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),

    url(r'^authorizations/$', obtain_jwt_token),

    url(r'browse_histories/$', views.UserBrowsingHistoryView.as_view()),

    # url(r'^addresses/$', views.AddressViewSet.as_view()),   # 收货地址
    #
    # url(r'^addresses/(?P<pk>\d+)/$', views.AddressViewSet.as_view()),   # 添加地址
    #
    # url(r'^addresses/(?P<pk>\d+)/status/$', views.AddressStatusView.as_view()),   # 默认地址


]

router = routers.DefaultRouter()
router.register(r'addresses', views.AddressViewSet, base_name='addresses')

urlpatterns += router.urls
