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

对于User-Agent想必大家都不陌生

## cookie

## Referer

# 一些实战案例

## 普通访问

一般来说，无论是什么网站，都是需要添加`User-Agent`来进行`get`的，然后就是登录才能访问的需要加上`cookie`，剩下的就需要看网站的具体形式了。

