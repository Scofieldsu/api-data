# encoding: utf-8

import os
from apidata import api
from apidata.utils.api_tools import compose_api_info
from apidata.utils.file_parse import get_decorator_func_doc,get_filename_list


#  提供API-DATA规范的数据
def get_all_api_data(dir=None, file_type='py', data_api=None, decor_list=None,except_dirs=None,except_paths=None, except_files=None):
    """
    :description 获取接口信息
    :param dir: 需要解析的路径
    :param file_type: 需要解析的文件类型
    :param decor_name: 需要获取__doc__的装饰器
    :return:
    """
    # 从method_doc_map获取所有接口方法，重组数格式
    if not except_dirs:
        except_dirs = list()
    if not except_paths:
        except_paths = list()
    if not except_files:
        except_files = list()
    result = dict()
    if not data_api:
        data_api = ['get_all_api']
    if not decor_list:
        decor_list = ['api_data']
    if not dir:
        dir = os.path.abspath('.')
    file_list = get_filename_list(dir, file_type, except_dirs, except_paths, except_files)
    api.method_doc_map = get_decorator_func_doc(file_list, decor_list)
    api_name_list = api.method_doc_map.keys()
    for i in api_name_list:
        item = compose_api_info(i, api.method_doc_map)
        result[i] = item
    for x in data_api:
        if x in result:
            result.pop(x)
    return result


