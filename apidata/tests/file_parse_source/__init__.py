import os
from apidata import api_data

source_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.abspath(__file__).replace('pyc','py')


@api_data
def tem_func():
    """
    :description test
    :param a:int:int_param
    :param b:str
    :return: test
    """
    return tem_func.__doc__

class temcls(object):

    @api_data
    def  tem_func_2(self):
        """
        :description test
        :param a:int:int_param
        :param b:str
        :return: test
        """
        return self.__doc__