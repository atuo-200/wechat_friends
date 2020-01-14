from wxpy import *

def wc_login():
    #登录微信
    bot = Bot()
    #获取所有好友对象
    my_friends = bot.friends()
    friend_infos = []

    for friend in my_friends:
        nick_name = friend.nick_name  # 好友昵称
        sex = friend.sex # 性别
        remark_name = friend.remark_name  # 备注
        signature = friend.signature # 个性签名
        province = friend.province  # 省份


        friend_infos.append({
		'nick_name': nick_name,
		'sex': sex,
		'remark_name': remark_name,
		'signature': signature,
		'province': province,
	})
    #print(friend_infos)
    #返回好友信息
    return friend_infos
    
