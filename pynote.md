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

## BeautifulSoup

pip install beautifulsoup4

python123.io/ws/demo.html

```python
import requests
from bs4 import BeautifulSoup

url =  'https://python123.io/ws/demo.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    print(r.status_code)
    demo = r.text
    soup = BeautifulSoup(demo,'html.parser')
    print(soup.prettify())
except:
    print("spider failed")
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
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)
 # p
 # body
```

标签树的平行遍历

- .next_sibling

- .previous_sibling

- .next_siblings
- .previous_siblings

```python
for sibling in soup.a.next_siblings:
    print(sibling)
for sibling in soup.a.previous_siblings:
    print(sibling)
```

- prettify()

  格式化输出

## 信息标记

html的信息标记：<>...</>

### 1 信息标记3类：

1. XML

   <font color=blue>internet传输</font>

2. JSON

   <font color=blue>移动应用、接口处理，无注释</font>

   键值对 {"key":"value"}

   ​			{"name":["a","b']}

   ​			{'key': {'subkey':'subvalue'}}

3. YAML

   <font color=blue>配置文件</font>

   无类型键值对（不带“”）

   name: value

   name:

   ​	-v1

   ​	-v2

   name:

   ​	newname : hideonstream

   ​	oldname : hideonbush

   |表达整块数据 #表达注释

   text: | 

   ​	北京理工大学blabla……

   
### 2 信息提取方法：

   1. 完整解析信息标记形式

   2. 无视标记，搜索关键词

   3. 融合：解析+查找

      HTML提取所有URL标签

      ```python
      import requests
      url =  'https://python123.io/ws/demo.html'
      r = requests.get(url)
      demo = r.text
      
      from bs4 import BeautifulSoup
      soup = BeautifulSoup(demo,'html.parser')
      for link in soup.find_all('a'):
          print(link.get('href'))
      ```

      

### 3 基于bs4库的HTML内容查找方法

```python
import requests
url =  'https://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
```

**find_all方法**

*.find_all(name, attrs, recursive, string, **kwargs)*

**1) name: 标签名称检索**

soup.find_all('a')//查找a标签

soup.find_all(['a','b'])//查找a标签和b标签

soup.find_all(True)//所有标签

import re //引入正则表达式库

soup.find_all(re.compile('b'))//b开头的标签

**2) attrs: 属性值字符串检索**

soup.find_all('p','course')//带有course属性值的p标签

soup.find_all(id='link1')//属性中id=link1的a标签

soup.find_all(id=re.compile('link'))//id中含有link的标签

**3) recursive: 是否对子孙全部检索（默认True**

soup.find_all('a')

soup.find_all('a',recursive=False)//仅对儿子层面进行检索

**4) string:<>...</>中字符串区域检索字符串**

soup.find_all(string = re.compile("python"))//所有出现python的字符串域

**tips:**

**< tag >(..) 等价于 < tag >.find_all(...)**

**soup(..)等价于 soup.find_all(..)**

**扩展方法：**

<>.find()

<>.find_parents()//列表类型

<>.find_parent()//一个结果

<>.find_next_siblings()//后续平行节点,列表

<>.find_next_sibling()

<>.find_previous_siblings()

<>.find_previous_sibling()

## 实例 中国大学排名定向爬虫

 http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html 

输入：大学排名URL

输出：大学排名信息（排名，大学名称，总分

技术路线：requests-bs4

定向爬虫：只对给定的URL进行爬取

可行性：检查源代码是否有页面数据信息，若动态生成这种方法不行

检查robots.txt没有，可以爬。

程序设计：

1、获取排名页面内容

——getHTMLText()

2、提取信息到合适数据结构

——二维列表fillUnivList()

3、利用数据结构展示输出结果

——printUnivList()

```python
import requests
import bs4
from bs4 import BeautifulSoup

# 输入：获取的URL信息，输出：获取内容
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""

# 将HTML页面放入列表中
def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            # tr.find_all('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])

# 将列表信息打印出来
def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    # {3}，使用format的第三个变量进行填充
    print(tplt.format("排名","学校名称","分数",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[3],chr(12288)))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2019.html'
    html = getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20) # 20 univserties

main()
```

# week3

## 正则表达式

### 0 正则表达式概念

regular expression regex RE 一行胜千言。

py开头，后续存在不多于10个字符，不能是p或者y

py[ ^py ]{0,10}

作用：查找替换，匹配字符串

编译：字符串——>正则表达式

### 1 正则表达式语法

. 任何单个字符

[] 字符集，对单个字符表示取值范围

[^] 非字符集

*前一个字符>=0次	abc *:ab,abc,abccc

+前一个字符>=1

？前一个字符0/1次扩展

|左或右

{m}前一个字符扩展m次

{m,n}扩展前一个字符[m,n]次

^匹配字符串开头

$匹配字符串结尾

()分组标记(abc|def)

\d [0-9]

\w [A-Za-z0-9]

例子：

p(y|yt|yth|ytho)?n: pn pyn pytn pythn python

python+: python pythonn pythonnn...

py[th]on: pyton pyhon

py[ ^th]?on: pyon pyaon pybon ...

^[A-Za-z]+$ 26个字母组成的字符串

^[A-Za-z0-9]+$

^-?\d+$整数

[\u4e00-\u9fa5]中文字符

\d(3)-\d(8)|\d(4)-\d(7)国内电话号码

**匹配IP地址的正则表达式**

\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3} 

​		300.300.300显然X

0-99: [1-9]?\d

100-199:1\d{2}

200-249:2[0-4]\d

250-255:25[0-5]

### 2 re库

 raw string类型（不包括\） r'[1-9]\d{5}'

字符串前加个r

string类型 要用转义符\ '[1-9]\ \d{5}'

- .search() 搜索第一个位置返回

  pattern,string,flags=0

  string:待匹配

  flags: 控制标记

  ​		re.I 忽略大小写

  ​		re.M字符串每行当作匹配开始

  ​		re.S .操作符匹配所有字符（除\n以外）

  ```python
  import re
  match = re.search(r'[1-9]\d{5}','BIT 100081')
  if match:
      print(match.group(0))
  ```

- .match() 在开始位置起

- .findall() 搜索字符串返回全部

- .split() 将一个字符串按照正则表达式匹配结果分割，列表

  pattern,string,maxsplit=0,flags=0

  maxsplit:最大分割数，剩余部分作为最后一个元素输出

  ```python
  import re
  re.split(r'[1-9]\d{5}','BIT100081 TSU100084')
  re.split(r'[1-9]\d{5}','BIT100081 TSU100084',maxsplit=1)
  ```

- .finditer() 搜索字符串返回匹配结果迭代类型，match对象

  ```python
  import re
  for m in re.finditer(r'[1-9]\d{5}','BIT100081 TSU100084'):
      if m:
          print(m.group(0))
  ```

- .sub() 替换所有匹配子串

  pattern,repl, string, count=0, flags=0

  repl：替换字符串

  count:最大替换次数

  ```python
  import re
  re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 TSU100084')
  ```

  

**面向对象方式：编译后多次操作**

pat =  re.compile(r'')

rst = pat.search(目标串)