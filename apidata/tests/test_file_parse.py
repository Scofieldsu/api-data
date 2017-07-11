# encoding: utf-8


import pytest
from file_parse_source import source_path,file_path
from apidata.utils.file_parse import *


@pytest.fixture
def tem_func():
    """
    :description test
    :param a:int:int_param
    :param b:str
    :return: test
    """
    return tem_func.__doc__


@pytest.fixture
def tem_func_2():
    """
    :description test
    :param a:int:int_param
    :param b:str
    :return: test
    """
    return tem_func_2.__doc__

@pytest.fixture()
def get_tree(file_name):
     return parse_ast(file_name)


def test_get_filename_list():
    result = get_filename_list(source_path)
    my_result = list()
    my_result.append(file_path)
    flag = not cmp(result.sort(),my_result.sort())
    assert flag


def test_get_decorator_func_doc():
    result = get_decorator_func_doc(get_filename_list(source_path))
    my_result = dict()
    my_result["tem_func"] = tem_func()
    my_result["tem_func_2"] = tem_func_2()
    flag = cmp(result, my_result)
    assert flag


def test_funcdef_dict():
    tree = get_tree(file_path)
    result = funcdef_dict(tree, dict(), decor_list=['api_data'])
    my_result = dict()
    my_result["tem_func"] = tem_func()
    flag = cmp(result, my_result)
    assert flag


def test_cls_dict():
    tree = get_tree(file_path)
    result = cls_dict(tree, dict(), decor_list=['api_data'])
    my_result = dict()
    my_result["tem_func_2"] = tem_func_2()
    flag = cmp(result, my_result)
    assert flag