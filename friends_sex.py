import login 
from pyecharts import Pie

#此模块统计好友性别比例
sex_dict = {'boys': 0, 'girls': 0, "no_sex": 0}
for friend in login.wc_login():
    #print(friend)
    if friend["sex"] == 1:
        sex_dict['boys'] += 1
    elif friend["sex"]  == 2:
        sex_dict['girls'] += 1
    elif friend["sex"] == 0:
        sex_dict['no_sex'] += 1
print(sex_dict)


attr = ["boys","girls","no_sex"]
v1 = [sex_dict["boys"],sex_dict["girls"],sex_dict["no_sex"]]

pie = Pie("小坨的微信好友性别比例分析")
pie.add(
    "",
    attr,
    v1,
    is_label_show=True,
    is_more_utils=True
)
pie.render(path="html_file/friends_sex.html")
