import re

from django.conf import settings
from django.core.mail import send_mail
from django_redis import get_redis_connection
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from users.models import User
from celery_tasks.email_dir.tasks import send_verify_email


class CreateUserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(label='确认密码', write_only=True)
    sms_code = serializers.CharField(label='短信验证码', write_only=True)
    allow = serializers.CharField(label='同意协议', write_only=True)
    token = serializers.CharField(label='登录状态token', read_only=True)  # 增加token字段

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'password2', 'mobile', 'sms_code', 'allow', 'token')
        extra_kwargs = {
            'username': {
                'min_length': 5,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许5-20个字符的用户名',
                    'max_length': '仅允许5-20个字符的用户名'
                }
            },
            'password': {
                'min_length': 8,
                'max_length': 20,
                'error_messages': {
                    'min_length': '仅允许5-20个字符的密码',
                    'max_length': '仅允许5-20个字符的密码'
                }
            }
        }

    def validate_mobile(self, value):
        """
        手机号格式
        """
        if not re.match(r'1[3-9]\d{9}$', value):
            raise serializers.ValidationError('手机号格式错误')
        return value

    def validate_allow(self, value):
        """
        用户协议
        """
        if value != 'true':
            raise serializers.ValidationError('请勾选用户协议')
        return value

    def validate(self, data):
        """
        校验密码, 短信验证码
        """

        # 校验密码
        if data['password'] != data['password2']:
            raise serializers.ValidationError('两次密码输入不一致')

        # 短信验证码
        redis_con = get_redis_connection('verify')  # 连接到redis数据库
        # 获取用户验证码
        sms_code = redis_con.get('sms_%s' % data['mobile'])  # type: bytes
        if sms_code is None:
            raise serializers.ValidationError('无效的短信验证码')

        if data['sms_code'] != sms_code.decode():
            raise serializers.ValidationError('短信验证码错误')

        return data

    def create(self, validated_date):
        """
        保存注册信息
        """
        # 删除数据库没有的键
        del validated_date['password2']
        del validated_date['sms_code']
        del validated_date['allow']
        user = super().create(validated_date)  # 继承父类方法

        # 调用Django的认证系统加密密码
        user.set_password(validated_date['password'])
        user.save()

        # 补充生成记录登录状态的token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        user.token = token

        return user


class UserDetailSerializer(serializers.ModelSerializer):
    """
    from 用户中心个人信息
    用户详细信息序列化器
    """

    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email', 'email_active')


class EmailSerializer(serializers.ModelSerializer):
    """
    from 保存邮箱并发送验证邮件
    邮箱序列化器
    """

    class Meta:
        model = User
        fields = ('id', 'email')
        extra_kwargs = {
            'email': {
                'required': True
            }
        }

    def update(self, instance, validated_data):

        email = validated_data['email']

        instance.email = email
        instance.save()

        # 生成验证链接
        verify_url = instance.generate_verify_email_url()
        # 发送验证邮件
        send_verify_email.delay(email, verify_url)
        # send_mail('天天科技', '注册验证', settings.EMAIL_FROM, [validated_data['email']])
        # send_mail('天天科技', '注册验证', settings.EMAIL_FROM, [email])





        return instance
