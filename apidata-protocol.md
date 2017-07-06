# <center> API-DATA 规范</center>
- author:yu
- datetime:2017-07-05
- version:0.1.0

---
   API-DATA规范定义了接口的注释格式（以便于采集接口信息返回给api-test应用进行接口测试）和api-test应用需要的数据格式。

   我们提供对于下面模型中注释进行转换到api-test应用需要的数据格式的公共方法。

- 接口模型：
``` python

def test_api(my_dict, my_int, my_str, my_list, my_datetime):
    """
    :description  测试接口
    :param my_dict: dict:字典参数
    :param my_int: int:整型
    :param my_str: str:无默认值
    :param my_list: list:可以省略[]
    :param my_datetime: datetime :时间戳
    :return: code or message
    """
  return result
```

> 在pycharm中可以利用自动补全参数的注释（pycharm没有自动补全 :description ），但还是需要你填写参数的类型和说明。

---

### JSON-RPC

   根据JSON-RPC规范整合接口数据.当服务收到method为get_all_api的请求时，应该返回一定格式的数据。

json-rpc的request：

``` python

{
    "jsonrpc":"2.0",
    "id": 1111,
    "method":"get_all_api",
    "params":{}
}

```

   不论你的应用使用flask，Django，tornado或者其他，符合json-rpc2.0规范的接口即可，当应用的get_all_api接口被调用时，返回由公共方法整合好的数据格式。

   当然你也可以不使用采集接口注释的公共方法，而自己实现了其他整合数据的方法，只要能返回下面格式的数据就可以。


#### 1.约定返回的数据格式（即api-test应用需要的数据格式）

##### - 服务端应返回的数据格式：

``` python
{
  "jsonrpc":  "2.0",
       "id":  **,
   "result":  data
}

```

##### - 其中data是整合的接口数据


``` python
{
    apiname-1:{
        "name":"",
        "description":"",
        "return":"",
        "params":{
            "param_a": type
        },
        "param_explain":{
            "param_a": explain
        }
    },
    apiname-2:{...}
}

```

##### - data中apiname-1是一个接口整合后的数据模型：
  - "name":  接口名称
  - "params":  接口参数
      - param_a： 参数名
      - type:  参数类型,可填('str','int','float','list','dict','datetime') 
  - "param_explain": 参数说明
      - param_a： 参数名
      - explain：参数的说明，字符串类型。
  - "return":  返回信息，字符串类型
  - "description": 接口描述

#### 示例:

``` python
{
    "jsonrpc":"2.0",
    "id":"2017-07-05T15:27:09+08:00",
    "result":{
        "login":{
            "name": "login",
            "description":"登录接口",
            "return":"登录信息",
            "params":{
                "pwd":"str",
                "name":"str"
            },
            "param_explain":{
                "name": "用户名",
                "pwd": "密码"
            }
        },
        "logout":{
            "name":"logout",
            "description":"退出接口",
            "return":"退出信息success or error",
            "params":{
                "name":"str"
            },
            "param_explain":{
                 "name"："用户名"
            }
        }
    }
}

```


---

### 其他规范协议中如何配合API-DATA规范  待续