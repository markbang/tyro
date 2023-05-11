# headers的参数

在`requests.get()`方法中，后面有关反爬的参数，其中就有headers，使用方法也很简单，`headers=一个字典`这个字典用来储存一些参数，伪造请求头来让网站认为是真人访问，而不是机器人。

```python
headers = {
  			'Referer': '具体的Referer',
            'User-Agent': '具体的user-agent',
    		'cookie':'具体的cookie'
    }
requests.get(url,headers=headers)
```

## User-Agent

对于User-Agent想必大家都不陌生，这是爬虫的第一步，大部分网站都有检查User-Agent，设置它很简单，就是打开开发者工具，在网络请求中找到复制粘贴即可。因为User-Agent一般都是固定的，里面包含的只是一些浏览器型号之类的，目的是确保你这个请求是真人，所以`my_fake_useragent`库也应运而生。

```python
from my_fake_useragent import UserAgent
headers = {'User-Agent': UserAgent(family='chrome').random()}
```

按照这个方式就可以随机User-Agent，更加方便而且会解决一些User-Agent反爬机制。

## cookie

## Referer

Referer与防盗链有关(防盗链：溯源，当前本次请求的上一级是谁  A ->B ->C )添加Referer就是确定是不是根据它所要的网站跳转到请求网站的，如果不是，则拒绝访问。例如一些视频网站的视频网址，如果不是从视频网站跳转过去，大部分可能就是拒绝。

这里我会拿豆瓣做一个实例解析，感兴趣的可以去看看，链接。

# 直接全部添加

在浏览器开发者模式中，我们不光只看到前面所提到的那几个参数，还有很多很多其它的参数，那具体的一个网站

