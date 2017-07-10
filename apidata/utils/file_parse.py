# encoding: utf-8
import ast


# 获取路径下 文件名列表
def get_filename_list(dir=None,file_type = 'py'):
    import os
    file_list = list()
    if not dir:
        dirs = os.path.abspath('.')
    else:
        dirs = dir
    for root, dirs, files in os.walk(dirs):
        for filename in files:
            if filename.endswith(file_type):
                file_list.append(os.path.join(root, filename))
    return file_list


# 返回该文件列表中所有使用某装饰器的函数的__doc__
def  get_decorator_func_doc(file_list,decor_list=['api_data']):
    import ast
    doc_dict = dict()
    for filename in file_list:
        tree = parse_ast(filename)
        doc_dict = funcdef_dict(tree, doc_dict, decor_list)
        doc_dict = cls_dict(tree, doc_dict, decor_list)
    return doc_dict



# 从ast抽象语法树中的对象 返回FunctionDef的注释字典
def funcdef_dict(tree, doc_dict, decor_list):
    for func in get_ast_functions(tree.body):
        if hasattr(func, 'decorator_list'):
            for i in func.decorator_list:
                if hasattr(i, 'id'):
                    if i.id in decor_list:
                        doc_dict[func.name] = ast.get_docstring(func)
    return doc_dict


# 从ast抽象语法树中的对象 返回ClassDef中FunctionDef的注释字典
def cls_dict(tree, doc_dict, decor_list):
    for clas in get_ast_class(tree.body):
        name_prefix = clas.name.lower()
        for func in get_ast_functions(clas.body):
            if hasattr(func, 'decorator_list'):
                for i in func.decorator_list:
                    if hasattr(i, 'id'):
                        if i.id in decor_list:
                            doc_dict[name_prefix + '.' + func.name] = ast.get_docstring(func)
    return doc_dict

# 返回解析后类型为ast.FunctionDef的函数
def get_ast_functions(body):
    """
    :param body:
    :return:
    """
    return (f for f in body if isinstance(f, ast.FunctionDef))


# 返回解析后类型为ast.ClassDef的类
def get_ast_class(body):
    """
    :param body:
    :return:
    """
    return (f for f in body if isinstance(f, ast.ClassDef))


# 解析文件，返回ast抽象语法树
def parse_ast(filename):
    """
    :param filename:
    :return:
    """
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)