"""
1.flask中的session机制是： 把敏感数据经过加密后放入session中，然后
再把session存放到cookie中，下次请求的时候，再从浏览器发送过来的cookie
中读取session，然后从session中读取敏感数据，并进行解密，获取最终的用户数据
2.flask的这种session机制，可以节省服务器的开销，因为把所有的信息都存储
在了客户端（浏览器）

"""



