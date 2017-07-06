# encoding: utf-8

from apidata import api,api_data
from apidata.utils.api_tools import compose_api_info

@api_data
def get_all_api_data(*args, **kwargs):
    """
    :description 获取接口信息
    :param args:str
    :param kwargs:str
    :return: 所有接口信息
    """
    # 从method_map获取所有接口方法，重组数格式
    api_dict = api.method_map
    api_name_list = api_dict.keys()
    result = {}
    for i in api_name_list:
        item = dict()
        item = compose_api_info(i, api_dict)
        result[i] = item
    result.pop("get_all_api_data")
    return result