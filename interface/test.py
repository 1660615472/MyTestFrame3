from interface.inter import HTTP

#构建关键字驱动对象
http = HTTP()
#登录前奏（授权）
http.post('http://112.74.191.10/inter/HTTP/auth')
#断言是否授权
http.assertequals('status','200')
#保存token
http.savejson('token','t')
#关联token信息
http.addheader('token','{t}')
#登录
http.post('http://112.74.191.10/inter/HTTP/login',d="{'username':'tom','password':'zhang1234'}")
http.assertequals('status','200')

http.savejson('userid','userid')
#获取用户信息
http.post('http://112.74.191.10/inter/HTTP/getuserinfo',id='id={userid}')

http.post('http://112.74.191.10/inter/HTTP/logout')
http.assertequals('status','200')