# encoding: utf-8

from apidata import api
from demo_api import *
from apidata.common import get_all_api_data

if __name__ == '__main__':
    logout_test("yu")
    login_test("y", "u")
    a = get_all_api_data()
    print api.method_map
    print a