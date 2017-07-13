
# How To Use api-data in your app

 ---

## 最简实践

 1.安装api-data： pip install api-data

 2.在所有接口文件中导入api_data，装饰你的接口：

  ``` python
  from apidata import api_data

  @api_data
  def test_api():
      ...
  ```

 3.实现一个 get_all_api 的接口，调用get_all_api_data方法获取所有接口信息，并通过get_all_api返回：

  ``` python
  from apidata.common import get_all_api_data

  @ 你的接口装饰器
  def get_all_api():

      result = get_all_api_data()

    return result
  ```

  ---


## 调用参数说明
  重点在于get_all_api_data的参数使用。

  ``` python
  def get_all_api_data(dir=None, file_type='py',data_api=['get_all_api'], decor_list=['api_data'],...):

      ...

  ```
 - dir : 默认为当前项目根路径。get_all_api_data只获取这个参数路径下的文件中的api

 - file_type: 默认为'py'，表示只解析py文件，一般我们的接口也是写在py文件中，这个参数是过滤不需要解析的其他文件，加快速率。

 - data_api: 默认为['get_all_api'],默认get_all_api为返回其他接口信息的接口，不暴露；除此你也可以添加其他不想暴露的接口。

    当然你也可以实现一个 a接口，在a接口中调用get_all_api_data，那么你的data_api的值应该[a]。当你使用a接口返回其他接口的信息，在api-test的settings你应该把get_all_api改为a

 - decor_list: 默认为['api_data'],表示只解析带有@api_data 的函数注释。如果你有使用其他装饰器实现了接口的路由分发，那么你可以不需要再在接口上使用@api_data，而是将decor_list改为你使用的装饰器。
 当然，你的decor_list也可以包含多个装饰器。

 - except_dirs:
    - 遍历except_dirs下所有子目录，并except_dirs及其子目录加入到except_path
    - 例如 .git目录下有很多子目录，只需要将 .git 的完整路径加入except_dirs，则.git及其子目录也不会被解析


 - except_path:
    - 对except_path下文件不解析，但except_path路径下的子目录中的文件还是会被解析
    - 例如 把 apidata/tests 加入except_path，只是没有解析test_api_tools.py等测试文件，但子目录中file_parse_source 中的文件依旧会被解析
    - 如果需求是 解析test_api_tools.py等测试文件，但不解析file_parse_source中的__init__.py文件,只需要把file_parse_source加入except_path

 - except_files:
    - 当不需要解析的文件比较少时或者该路径下也存在需要解析的文件时，可以直接将不需要解析的文件加入except_files

