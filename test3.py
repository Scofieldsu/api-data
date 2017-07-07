# encoding: utf-8

import ast
from apidata import api_data,api
import os

dir = os.path.abspath('.')
file_list = list()
for root, dirs, files in os.walk(dir):
    for filename in files:
        if filename.endswith('py'):
           file_list.append(os.path.join(root,filename))
           # print os.path.join(root,filename)

@api_data
def top_level_functions(body):
    """
    :param body:
    :return:
    """
    return (f for f in body if isinstance(f, ast.FunctionDef))


@api_data
def parse_ast(filename):
    """
    :param filename:
    :return:
    """
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)

if __name__ == "__main__":
    files = file_list
    for filename in files:
        # print(filename)
        tree = parse_ast(filename)
        for func in top_level_functions(tree.body):
            if hasattr(func, 'decorator_list'):
                for i in func.decorator_list:
                    if hasattr(i, 'id'):
                        # print i.id
                        if i.id == 'api_data':
                            api.method_doc_map[func.name] = ast.get_docstring(func)
                            # print ast.get_docstring(func)
                            print("  %s" % func.name)
    print api.method_doc_map