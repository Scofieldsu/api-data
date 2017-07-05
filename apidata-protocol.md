##    api-data-protocol
- author:yu
- datetime:2017-07-05
- version:0.1.0

---
### JSON-RPC
   根据JSON-RPC规范整合接口数据.

#### 1.约定数据格式定义

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