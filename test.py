# encoding: utf-8

from apidata import api
from apidata.common import get_all_api_data
from demo_api import *

if __name__ == '__main__':
    login_test('yu','u')
    logout_test('u')
    a = get_all_api_data()
    print api.method_map
    print a