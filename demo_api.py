# encoding: utf-8

from apidata import api_data


@api_data
def login_test(name, pwd):
    """
    :description test登录接口
    :param name: str
    :param pwd: str
    :return: test登录信息
    """
    result = {"msg": "login success", "code": 200}
    return result


@api_data
def logout_test(name):
    """
    :description test退出接口
    :param name: str
    :return: test退出信息success or error
    """
    return "logout success"
