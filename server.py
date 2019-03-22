from gevent import monkey
from matrix import Matrix
from flask import Flask
from flask import render_template
from gevent.pywsgi import WSGIServer

monkey.patch_all()
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


if __name__ == "__main__":
    http_server = WSGIServer(('127.0.0.1', 5000), app)
    http_server.serve_forever()
