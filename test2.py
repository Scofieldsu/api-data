# encoding: utf-8

from flask import Flask
from apidata import api
from demo_api import *

def create_app():
    app = Flask(__name__)
    return app

app = create_app()


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    #login_test('yu','u')
    # logout_test('u')
    print api.method_doc_map
    app.run()