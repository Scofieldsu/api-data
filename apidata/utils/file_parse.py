# encoding: utf-8
import ast


# 获取路径下 文件名列表
def get_filename_list(dir=None, file_type = 'py', except_dirs=None,except_paths=None, except_files=None):
    #######################
    # except_dirs
    # 遍历except_dirs下所有子目录，并加入到except_path
    # 例如 .git目录下有很多子目录，只需要将 .git 的完整路径加入except_dirs，则其子目录也不会被解析


    # except_path
    # 对except_path下文件排除解析，但except_path路径下的子目录中的文件还是会被解析
    # 例如 把 apidata/tests 加入except_path，只是没有解析test_api_tools.py等测试文件，但子目录中file_parse_source 中的文件依旧会被解析
    # 如果需求是 解析test_api_tools.py等测试文件，但不解析file_parse_source中的__init__.py文件
    # 只需要把file_parse_source加入except_path

    # except_files
    # 当不需要解析的文件比较少时，可以直接加入except_files
    #######################
    import os
    file_list = list()
    if not except_dirs:
        except_dirs = list()
    if not except_paths:
        except_paths = list()
    if not except_files:
        except_files = list()
    if not dir:
        dirs = os.path.abspath('.')
    else:
        dirs = dir
    if except_dirs:
        for tem_dirs in except_dirs:
            for tem_root,tem_dirs,tem_files in os.walk(tem_dirs):
                except_paths.append(tem_root)
    for root, dirs, files in os.walk(dirs):
        if root not in except_paths:
            for filename in files:
                if os.path.join(root, filename) not in except_files:
                    if filename.endswith(file_type):
                        file_list.append(os.path.join(root, filename))
    return file_list


# 返回该文件列表中所有使用某装饰器的函数的__doc__
def  get_decorator_func_doc(file_list,decor_list=None):
    import ast
    if not decor_list:
        decor_list = ['api_data']
    doc_dict = dict()
    for filename in file_list:
        tree = parse_ast(filename)
        if isinstance(tree, ast.Module):
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