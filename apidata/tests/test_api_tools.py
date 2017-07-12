# encoding: utf-8

import pytest
from apidata.utils.api_tools import trans_str_to_dict,dict_move_key,compose_api_info


@pytest.fixture
def tem_func():
    """
    :description test
    :param a:int:int_param
    :param b:str
    :return: test
    """
    return tem_func.__doc__

def test_trans_str_to_dict():
    trans_dict = {
        "description": "test",
        "return": "test",
        "param_explain": {"a":"int_param"},
        "a": "int",
        "b": "str"
    }
    flag = not cmp(trans_str_to_dict(tem_func()), trans_dict)
    assert  flag


def test_dict_move_key():
    b_dict = {
        "b_one": "one",
        "b_two": "two",
    }
    a_dict = {
        "a": "aa",
        "b": b_dict
    }
    c = {
        "a": "aa",
        "b_one": "one",
        "b": {
            "b_two": "two"
        }
    }
    d = dict_move_key(a_dict,b_dict,"b_one")
    flag = not cmp(d, c)
    assert flag


def test_compose_api_info():
    method_doc_dict = dict()
    method_doc_dict[tem_func.__name__] = tem_func.__doc__
    result = compose_api_info("tem_func", method_doc_dict)
    my_result = {
        "name": "tem_func",
        "description": "test",
        "return": "test",
        "param_explain": {"a": "int_param"},
        "params": {
            "a": "int",
            "b": "str"
        }
    }
    flag = not cmp(result, my_result)
    assert flag