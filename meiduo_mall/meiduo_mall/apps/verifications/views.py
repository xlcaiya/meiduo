from random import randint

from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework.views import APIView
from celery_tasks.sms.tasks import send_sms_code

# Create your views here.


class SMSCodeView(APIView):
    """发送短信验证码"""

    def get(self, request, mobile):  # mobile为str类型
        # 创建连接到redis的对象
        redis_conn = get_redis_connection('verify')

        # 60秒内不允许重发短信
        send_flag = redis_conn.get('send_flag_%s' % mobile)
        if send_flag:
            return Response({'error': '短信请求过于频繁'}, status=400)

        # 随机生成一个短信验证码
        sms_code = '%06d' % randint(0, 999999)

        # 保存短信验证码
        """方式1
        conn = get_redis_connection('verify')
        conn.setex('sms_%s' % mobile, 300, sms_code)
        """
        """方式2
        ccp = CCP()
        ccp.send_template_sms(mobile, [sms_code, '1'], 1)   # 发送成功
        
        """
        """方式2.1
        send_sms_code.delay(mobile, sms_code)   # delay, 延迟
        """
        """方式3
        # CCP().send_template_sms(mobile, [sms_code, constants.SMS_CODE_REDIS_EXPIRES // 60], constants.SEND_SMS_TEMPLATE_ID)
        """
        """方式4
        # 发送短信验证码
        # sms_code_expires = str(constants.SMS_CODE_REDIS_EXPIRES // 60)
        sms_code_expires = str(60)
        sms_tasks.send_sms_code.delay(mobile, sms_code, sms_code_expires)
        """
        sms_code_expires = str(60)
        send_sms_code.delay(mobile, sms_code, sms_code_expires)

        # 以下代码演示redis管道pipeline的使用
        pl = redis_conn.pipeline()
        pl.setex("sms_%s" % mobile, 300, sms_code)
        pl.setex('send_flag_%s' % mobile, 60, 1)
        # 执行
        pl.execute()

        # 打印短信验证码

        # print(sms_code)  # 测试环境下, 验证码打印到控制台就可以

        # 返回结果
        return Response({'message': 'OK'})
