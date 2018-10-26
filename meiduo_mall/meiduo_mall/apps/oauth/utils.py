from django.conf import settings
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadData


def generate_save_user_token(openid):   # openid: FEE0C7619E1C33BF621CAFC57038A51A
    """
    生成保存用户数据的token
    :param openid: 用户的openid
    :return: token
    """
    serializer = Serializer(settings.SECRET_KEY, 300)   # 秘钥, 有效期秒
    data = {'openid': openid}   # data: {'openid': 'FEE0C7619E1C33BF621CAFC57038A51A'}
    token = serializer.dumps(data)  # 返回bytes类型
    token = token.decode()  # token: eyJpYXQiOjE1NDA1MjExNDEsImFsZyI6IkhTNTEyIiwiZXhwIjoxNTQwNTIxNDQxfQ.eyJvcGVuaWQiOiJGRUUwQzc2MTlFMUMzM0JGNjIxQ0FGQzU3MDM4QTUxQSJ9.61gv8fsFEU6mdCIJ4KVxfJ5tXnO5jSmYfU_vJmQQlfuJzDuRb1Ug9_KLrbf6zi5YUXL3geq_IusMkJ3yR2cNrA

    # 检验token
    # 验证失败，会抛出itsdangerous.BadData异常
    serializer = Serializer(settings.SECRET_KEY, 300)
    try:
        data = serializer.loads(token)  # data {'openid': 'FEE0C7619E1C33BF621CAFC57038A51A'}
    except BadData:
        return None

    return token


def check_save_user_token(access_token):
    """
    检验保存用户数据的token
    :param token: token
    :return: openid or None
    """
    serializer = Serializer(settings.SECRET_KEY, 300)
    try:
        data = serializer.loads(access_token)
    except BadData:
        return None
    else:
        return data.get('openid')