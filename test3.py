# encoding: utf-8

import ast
from apidata import api_data


def top_level_functions(body):
    return (f for f in body if isinstance(f, ast.FunctionDef))

@api_data
def parse_ast(filename):
    with open(filename, "rt") as file:
        return ast.parse(file.read(), filename=filename)

if __name__ == "__main__":
    files = [__file__]
    for filename in files:
        print(filename)
        tree = parse_ast(filename)
        for x in tree.body:
            if hasattr(x, 'decorator_list'):
                for i in x.decorator_list:
                    print i.id
        for func in top_level_functions(tree.body):
            print("  %s" % func.name)