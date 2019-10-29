## requests

pip install requests

##### py:

```
import requests

r=requests.get('http://www.baidu.com')

r.status_code//状态码

r.encoding = 'utf-8'

r.text
```

![1572353567253](C:\Users\666\AppData\Roaming\Typora\typora-user-images\1572353567253.png)

#### get方法：

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

