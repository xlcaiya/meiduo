from django.test import TestCase

# Create your tests here.
import pickle

data =  pickle.dumps('sdafasdfsda')

print(data)

str = 'DSFASDFSDAFASDFASD'

print(str.lower())

from itsdangerous import TimedJSONWebSignatureSerializer as TJS

# TimedJSONWebSignatureSerializer(JSONWebSignatureSerializer) 下的 __init__ 设置秘钥, 过期时间
tjs = TJS('sdafasdfasdf', 300)

# 使用的是 JSONWebSignatureSerializer 里的 dumps进行加密
tjs.dumps('dfsafasdf')
