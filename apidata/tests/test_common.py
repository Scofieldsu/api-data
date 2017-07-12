# encoding: utf-8


from apidata.common import get_all_api_data
from file_parse_source import source_path


def test_get_all_api_data():
    result = get_all_api_data(source_path)
    my_result = {
        "temcls.tem_func_2":{
            "params":{"a":"int","b":"str"},
            "return":"test",
            "name":"temcls.tem_func_2",
            "param_explain":{"a":"int_param"},
            "description":"test"
        },
        "tem_func":{
            "params":{"a":"int","b":"str"},
            "return":"test",
            "name":"tem_func",
            "param_explain":{"a":"int_param"},
            "description":"test"
        }
    }
    flag = not cmp(result,my_result)
    assert flag