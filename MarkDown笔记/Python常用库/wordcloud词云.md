# wordcloud介绍

```python
import jieba
import wordcloud
import imageio
import numpy as np
f = open(r'C:\Users\LENOVO\Desktop\Python文件\第三方库学习\词频、词云\20大报告.txt', 'r', encoding='utf-8')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
bg_pic = imageio.v2.imread(r'C:\Users\LENOVO\Desktop\Python文件\第三方库学习\词频、词云\中国地图.jpeg').astype(np.uint8)
mask = np.array(bg_pic)
stopwords = {'和','的','是','在','以','大','了','从','好','把','对'}
w = wordcloud.WordCloud(font_path='msyh.ttc', width=1000, height=700,
                        background_color='white',stopwords=stopwords,mask=mask)
w.generate(txt)
w.to_file('grwprdcloud.png')
```

![](https://bangwu.oss-cn-shanghai.aliyuncs.com/img/202305101212625.png)