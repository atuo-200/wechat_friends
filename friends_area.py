import login 
from pyecharts import Bar

#此模块统计好友省份并制作条形图

# 使用一个字典统计各省好友数量
province_dict = {'北京': 0, '上海': 0, '天津': 0, '重庆': 0,
    '河北': 0, '山西': 0, '吉林': 0, '辽宁': 0, '黑龙江': 0,
    '陕西': 0, '甘肃': 0, '青海': 0, '山东': 0, '福建': 0,
    '浙江': 0, '台湾': 0, '河南': 0, '湖北': 0, '湖南': 0,
    '江西': 0, '江苏': 0, '安徽': 0, '广东': 0, '海南': 0,
    '四川': 0, '贵州': 0, '云南': 0,
    '内蒙古': 0, '新疆': 0, '宁夏': 0, '广西': 0, '西藏': 0,
    '香港': 0, '澳门': 0}

# 统计省份
for friend in login.wc_login():
    if friend["province"] in province_dict.keys():
        province_dict[friend["province"]] += 1

#提取数据
province_label = []
province_data  = []
for key, value in province_dict.items():
    #获取好友数量不为0的省份名称和其好友数量
    if value != 0:
        province_label.append(key)
        province_data.append(value)

bar = Bar('小坨的微信好友省份分析')
kwargs = dict(
    name = '小坨的微信好友省份分析',
    x_axis = province_label,
    y_axis = province_data,
    bar_category_gap = 0,
    is_label_show = True
)
print(kwargs)
bar.add(**kwargs)
bar.render(path="html_file/friends_area.html")

