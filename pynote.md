# week1

## requests入门

### 0 Requests下载

pip install requests

```python
import requests
r=requests.get('http://www.baidu.com')
r.status_code	//状态码
r.encoding = 'utf-8'
r.text
```

### 1 Requests库的get方法

requests.get(url,params=NONE,**kwargs)

r.status_code 	200 ok 

r.text	页面内容

r.encoding	http猜测的网页编码方式

r.apparent_encoding	编码方式

r.content	http内容二进制形式

```
import requests
r = requests.
```

### 2 request异常（基本框架）

requests.Connection	网络连接错误异常

requests.HTTPError	http错误

requests.URLRequired	URL缺失异常

requests.TooManyRedirects	超过最大重定向次数，产生重定向异常

requests.ConnectTimeout	连接远程服务器超时异常

requests.Timeout	请求URL超时，产生超时异常

```python
import requests
def getHTMLText(url):
	try:
		r = requests.get(url, timeout=30)
		r.raise_for_status() 
        # 如果状态不是200，引发httperror异常
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return "产生异常"

if __name__=="__main__":
	url = "http://www.baidu.com"
	print(getHTMLText(url))
```

### 3 http协议及Requests库方法

URL格式	http://host[:port][path]

host	合法Internet主机域名/IP地址

port	端口号

path	请求资源路径

http://www.bit.edu.cn

http://220.181.111.181/duty

1. GET——全部资源
2. HEAD——获得头部信息
3. POST
4. PUT——存储资源
5. PATCH——局部更新
6. DELETE——删除资源

###### patch和put区别

patch局部更新只需提交更新字段，put必须提交所有字段

```python
# head
r = requests.head('http://httpbin.org/get')
print(r.headers)
# post
payload = {'key1':'value1','key2':'value2'}
r = requests.post('http://httpbin.org/post', data = payload)# 在form字段
r = requests.post('http://httpbin.org/post', data = 'ABC') # ABC在data段
print(r.text)
```

### 4 Requests库主要方法解析

requests.request(method,url,**kwargs)

**kwargs：控制访问参数

params:字典或字节序列

```python
# params
kv = {'key1':'value1','key2':'value2'}
r = requests.request('GET','http://httpbin.org/get',params=kv)
print(r.url)
# **data
r = requests.request('POST','http://httpbin.org/get',data=kv)
print(r.url)
# **json
# **headers
hd={'user-agent':'Chrome/10'}
r = requests.request('POST','http://python123.io/ws',headers=hd)
# cookies：字典
# auth：元组
# files：字典类型，文件
fs = {'file':open('.xls','rb')}
requests.request('POST','http://python123.io/ws',files=fs)
# timeout
# proxies 设定访问代理服务器，增加登陆认证
# allow_redirects:重定向
# stream 立即下载
# verify SSL证书
# cerf 本地SSL证书
```

## robots协议

### 0 网络爬虫引发的问题

​	小规模：Requests库	>90%

​	中规模：Scrapy库

​	限制的审查：

​			User-Agent限制：只响应浏览器

​			Robots协议

### 1 Robots协议

网络爬虫排除标准：哪些页面可以抓取，哪些不行

robots.txt

 https://www.jd.com/robots.txt 

### 2 Robots协议的使用

自动/人工识别robots.txt

## 5个实例

### 0京东商品链接

 https://item.jd.com/100004404944.html 

r = requests.get(' https://item.jd.com/100004404944.html ')

r.status_code

r.encoding

r.text[:1000]

```python
import requests
url = 'https://item.jd.com/100004404944.html'
try:
	r = requests.get(url, timeout=30)
	r.raise_for_status()
    #如果状态不是200，引发httperror异常
	r.encoding = r.apparent_encoding
	print(r.text[:1000])
except:
	print("产生异常")
```

1 亚马逊商品信息（修改头部）

 https://www.amazon.cn/dp/B07TYR42LV

```python
import requests
r = requests.get('https://www.amazon.cn/dp/B07TYR42LV')
print(r.status_code) # 网络没错，浏览器判断不同。
print(r.encoding)
print(r.request.headers) # 头部信息

kv = {'user-agent':'Chrome/5.0'}
url = 'https://www.amazon.cn/dp/B07TYR42LV'
r = requests.get(url, headers = kv)
print(r.status_code)
print(r.request.headers)
page = r.text
print(page)
```

### 2 baidu 360 搜索关键词提交

http://www.baidu.com/s?wd=<font color=blue>keyword</font>

http://www.so.com/s?q=<font color=blue>keyword</font>

```python
import requests
arg='wd'
keyword='Python'
try:
    kv={arg:keyword}
    r = requests.get('http://www.baidu.com/s',params = kv)
    r.raise_for_status()
    print(r.status_code)
    print(r.request.url)
    print(len(r.text))
except:
    print("spider failed")
```

### 3 网络图片的爬取（下载图片）

格式：http://www.exp.com/pic.jpg

国家地理：<http://www.ngchina.com.cn/>

http://image.ngchina.com.cn/2019/1026/20191026093445665.jpg

```python
import requests
import os
url = "http://image.ngchina.com.cn/2019/1026/20191026093445665.jpg"
root = "E://kaifa//pics//"
path = root + url.split('/')[-1]
try:
    # 当前根目录是否存在
    if not os.path.exists(root):
        os.mkdir(root)
    print(path)
    # 当前文件是否存在
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        print(r.status_code)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
    else:
        print("file exists!")
except:
    print("spider failed")
    
```

### 4 IP地址归属地自动查询

```python
import requests
url = "http://m.ip138.com/ip.asp?ip="
try:
    r = requests.get(url + '202.204.80.112')
    r.raise_for_status()
    print(r.status_code)
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("spider failed")
```

# week2

## 1 beautifulsoup安装

pip install beautifulsoup4

python123.io/ws/demo.html

```python
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo,'html.parser')
print(soup.prettify())
```

字符串标签树 ——> beautifulsoup类

- tag标签 <></>
- name 标签名
- attributes 标签属性
- navigableString标签内非属性字符串
- Comment 标签内字符串注释

标签书的下行遍历

- .contents 子节点列表 < tag >所有儿子节点存入列表
- .children 子节点迭代类型
- .descendants 子孙节点迭代类型

```python
# 遍历儿子节点
for child in soup.body.children:
    print(child)
    
# 遍历子孙节点
for child in soup.body.descendants:
    print(child)
```

标签树的上行遍历

```python
soup = BeautifulSoup(demo, 'html.parser')
for parent in soup.a.
```



