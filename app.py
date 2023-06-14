# from gevent import monkey
# monkey.patch_all()  # 異步 基於greenlet
# from gevent import pywsgi
from main import create_app

# if need test change controller to test
blueprints = ['main.controller:v1', ]
# if need test change development to testing
app = create_app('development', blueprints)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555)
    # server = pywsgi.WSGIServer(('0.0.0.0', 8999), app, keyfile='./SSL/server-key.pem', certfile='./SSL/server-cert.pem')  # 需使用支持 gevent 的 WSGI
    # server.serve_forever()
