from potencial_api import App
from gevent.pywsgi import WSGIServer

app = App().start()

if __name__ == '__main__':
  http_server = WSGIServer(('67.205.58.167',8082), app)
  http_server.serve_forever()
    