from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from users import serializer
from users.models import User


class UserRegisterView(CreateAPIView):
    """
    用户注册
    传入参数:
        username, password, password2, mobile, sms_code, allow
    """
    serializer_class = serializer.CreateUserSerializer


class UsernameCountView(APIView):
    """
    用户名数量
    """

    def get(self, request, username):
        """
        获取指定用户名数量
        """
        # 查询用户数量
        count = User.objects.filter(username=username).count()

        data = {
            'username': username,
            'count': count
        }

        # 通过json返回结果
        # return JsonResponse(data)
        return Response(data)


class MobileCountView(APIView):
    """
    手机号数量
    """

    def get(self, request, mobile):
        """
        获取指定手机号数量
        """
        # 查询手机号数量
        count = User.objects.filter(mobile=mobile).count()

        # 包装成字典
        data = {
            'mobile': mobile,
            'count': count
        }

        # 返回数据
        return Response(data)
