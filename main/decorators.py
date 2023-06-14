###############################
# reference:https://medium.com/citycoddee/python%E9%80%B2%E9%9A%8E%E6%8A%80%E5%B7%A7-3-%E7%A5%9E%E5%A5%87%E5%8F%88%E7%BE%8E%E5%A5%BD%E7%9A%84-decorator-%E5%97%B7%E5%97%9A-6559edc87bc0
#           https://blog.csdn.net/weixin_42817311/article/details/107875619
###############################

from functools import wraps
from flask import Response, session
import json


def session_required(func):
    @wraps(func)
    def wrapper():
        access_id = session.get('key', 'not set')
        if access_id == 'not set':
            data = {"code": 401, "success": "false", "data": "token expired"}
            return Response(json.dumps(data), mimetype='application/json')
        else:
            return func()
    return wrapper
