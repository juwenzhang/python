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