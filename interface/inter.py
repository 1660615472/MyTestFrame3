import json

import requests
"""
http接口自动化的关键字库
"""
class HTTP:
    #构造函数初始变量
    def __init__(self):
        self.session = requests.session()
        self.result =''
        self.jsonres={}
        #用来保存关联数据的字典
        self.params={}


    #发包
    def post(self,url,d=None,j=None,encode='utf8'):
        if d is None:
            pass
        else:
            d =self.__get_param(d)
            d =self.__get_data(d)
        res =self.session.post(url,d,j)
        self.result =res.content.decode(encode)
        #解析返回结果
        self.jsonres = json.loads(self.result)


    #添加头信息（session）
    def addheader(self,key,value):
        value = self.__get_param(value)
        self.session.headers[key] = value


    #断言
    def assertequals(self,key,value):
        if str(self.jsonres[key]) == str(value):
            print('PASS')
        else:
            print('FAIL')

    #保存关联数据的方法
    def savejson(self,key,p):
        #将传入的关联数据保存到参数P的值
        self.params[p]= self.jsonres[key]

    #获取关联数据的方法
    def __get_param(self,s):
        #按规则获取关联参数
        #遍历已经保存的参数，将传入字符串里面，满足｛key｝所有字符串用key的值替换
        for key in self.params :
           s = s.replace('{'+key+'}',self.params[key])
           return s

    #将字符串变成字典
    def __get_data(self,s):
        s = eval(s)
        return s