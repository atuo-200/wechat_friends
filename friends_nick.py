import login 
import pyecharts
import random
from pyecharts import WordCloud

#此模块制作昵称词云图

name = []
for friend in login.wc_login():
    name.append(friend["nick_name"])

myWordCloud = WordCloud("昵称词云图",width=1300, height=1000)
#随机生成词频列表
value = random.sample(range(1,1000),len(name))
print("好友昵称",name)
myWordCloud.add("",name,value,word_size_range=[40,100])
myWordCloud.render("html_file/friends_nick.html")


