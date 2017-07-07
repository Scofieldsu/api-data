# encoding: utf-8

PARAMS_TYPE = ['dict','int','str','float','list','datetime']

# 把function的__doc__字符串转换为字典
def trans_str_to_dict(do_str):
    result = {"param_explain":{}}
    if not do_str:
        return result
    tem_list = do_str.split('\n')
    for x in tem_list:
        if ":description" in x:
            result["description"] = x.split(":description")[1].strip()
        elif ":param" in x:
            params = x.split(":param")[1]
            if params.strip():
                tem = params.split(':')
                if len(tem) >= 2 and tem[1].strip().lower() in PARAMS_TYPE:
                    result[tem[0].strip()] = tem[1].strip()
                if len(tem) >= 3 :
                    result["param_explain"][tem[0].strip()] = tem[2].strip()
        elif ":return:" in x:
            result["return"] = x.split(":return:")[1].strip()
    return result


# 字典b是字典a中的一个value，把字典b中的一个键值对移动到字典a
def dict_move_key(dict_a, dict_b, key):
    if key in dict_b:
        dict_a[key] = dict_b[key]
        dict_b.pop(key)
    return dict_a


# 重组接口信息为get_all_api_tem中的数据格式
def compose_api_info(key, api_dict):
    tem_res = {}
    tem_res["name"] = key
    doc_dict = trans_str_to_dict(api_dict[key])
    move_key = [
        "description",
        "return",
        "param_explain"
    ]
    for x in move_key:
        tem_res = dict_move_key(tem_res,doc_dict, x)
    tem_res["params"] = doc_dict
    return tem_res