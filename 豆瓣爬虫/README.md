# 豆瓣爬虫





这次进行爬取的内容是：书的图片链接   书的名称  书的作者名

使用到的模块含有：

1.os模块   用于进行创建新的目录 以及 进行保存图片的链接

2.re模块   用来实现正则表达式，来在一大坨的html模块中进行一些操作来实现我们的正则表达式的书写

3.requests模块  用来进行我们的发起网络请求

4.with open as 语句，进行将爬取得到的数据进行保存



## 1.第一步：首先先进行实现请求网页代码

这个就是使用了我们的requests模块

然后使用with open as 语句来实现我们的基本的一些方法，来实现基本的保存网页的内容

使用这个就是为了可以实现我们对同一个网页的请求次数的减少，以免ip被封



## 2.开始书写正则表达式

使用re模块来进行匹配我们的一些内容

其中re模块中的方法含有： match  search  findall



## 3.最后使用for循环来实现我们一一保存操作

通过描述我们就可以知道，进行一些保存的时候，我们使用的含有：三个部分图片链接，书名，书的作者

使用for循环中接收到的参数，来实现我们的一些将基本的内容进行保存



## 4.对于图片链接还要进行保存在一个独特的目录下面才可以

所以通过这些操作后，我们还要通过一些方法来实现对图片进行请求并转换为二进制的格式进行保存起来

然后在下载到使用os通过mkdir来创建的文件夹的下面:  os.mkdir("目录名")5.

但是这里我们还要进行一些操作来实现有一些细节的地方，就是创建目录的时候，是在目录不存在的时候，进行创建

os.path.exists("目录名")  如果存在就返回true 不存在就返回false



## 5.最后来实现将我们的测试代码整合到起始的文件

最后进行总和，就是实现我们的完整的代码格式

所以你会在我们的目录下面含有两个文件， test.py 用于进行测试的文件    另外一个就是用于进行完整的爬虫的实现效果



test.py

```python
# 开始利用爬取并且保存了的包进行接下来的操作来减少我们的请求次数
import re
import os
import requests

with open("douban.html","r",encoding="utf-8") as f:
    data_douban = f.read()

# 测试是否可以进行读取得到网页的基本内容
# print(data_douban)

# 目前我们进行获取得到的数据是：图片链接  图片标题  作者姓名
result = re.findall(r'<div\sclass="cover">.*?<img\ssrc="(.*?)"'
                    r'.*?<h4\sclass="title">.*?class="">(.*?)</a>.*?<'
                    r'.*?\sclass="author">(.*?)</.*?>.*?</li>', data_douban, re.S)

# 测试代码开始
# print(result)
# print(len(result))

# 开始进行保存数据

for i in result:
    images_data = i[0]
    title = i[1].strip()
    author = i[2].strip()
    print(images_data)
    print(title)
    print(author)

    # 开始进行填入数据
    with open("data.text","a",encoding="utf-8") as f:
        f.write(f"图片链接为：{images_data}" + "\n")
        f.write(f"书的名称为：{title}" + "\n")
        f.write(f"书的作者是：{author}" + "\n")
        f.write("\n")

    # 开始进行图片的请求并且保存
    if not os.path.exists("book_data"):
        os.mkdir("book_data")
    with open("book_data/图片{}.jpg".format(title),"wb") as f:
        # 然后进行保存图片
        image_data = requests.get(images_data).content
        f.write(image_data)
```



doupanRead.py

```python
# 首先先进行导入模块
import re
import requests
import os

# 开始进行书写路径
url = "https://book.douban.com/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64;"
                  " x64) AppleWebKit"
                  "/537.36 (KHTML, like Gecko)"
                  " Chrome/125.0.0.0 Safari/537.36"
}

# 开始请求返回数据
response = requests.get(url, headers=headers)

# 为了减少请求的次数，所以就要进行对请求了的数据进行保存
with open("douban.html", "w", encoding="utf-8") as f:
    f.write(response.text)

# 开始利用爬取并且保存了的包进行接下来的操作来减少我们的请求次数

with open("douban.html","r",encoding="utf-8") as f:
    data_douban = f.read()

# 测试是否可以进行读取得到网页的基本内容
# print(data_douban)

# 目前我们进行获取得到的数据是：图片链接  图片标题  作者姓名
result = re.findall(r'<div\sclass="cover">.*?<img\ssrc="(.*?)"'
                    r'.*?<h4\sclass="title">.*?class="">(.*?)</a>.*?<'
                    r'.*?\sclass="author">(.*?)</.*?>.*?</li>', data_douban, re.S)

# 测试代码开始
# print(result)
# print(len(result))

# 开始进行保存数据

for i in result:
    images_data = i[0]
    title = i[1].strip()
    author = i[2].strip()
    print(images_data)
    print(title)
    print(author)

    # 开始进行填入数据
    with open("data.text","a",encoding="utf-8") as f:
        f.write(f"图片链接为：{images_data}" + "\n")
        f.write(f"书的名称为：{title}" + "\n")
        f.write(f"书的作者是：{author}" + "\n")
        f.write("\n")

    # 开始进行图片的请求并且保存
    if not os.path.exists("book_data"):
        os.mkdir("book_data")
    with open("book_data/图片{}.jpg".format(title),"wb") as f:
        # 然后进行保存图片
        image_data = requests.get(images_data).content
        f.write(image_data)
```

