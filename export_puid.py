#!/usr/bin/env python3
# coding: utf-8

from wxpy import *

'''
使用 cache 来缓存登陆信息，同时使用控制台登陆
'''
bot = Bot('bot.pkl', console_qr=True)


'''
开启 PUID 用于后续的控制
'''
bot.enable_puid('wxpy_puid.pkl')

friends = bot.friends()
groups = bot.groups()

with  open('data', 'w',encoding='UTF-8') as output:
    output.write("-----Groups-------\n")
    for i in groups:
        output.write(i.name + " ---> " + i.puid + "\n")

# 启用 puid 属性，并指定 puid 所需的映射数据保存/载入路径

# 指定一个好友
my_friend = bot.friends().search('刘亚琼@青云QingCloud')[0]
#my_friend = bot.friends().search('青小云')[0]

# 查看他的 puid
print(my_friend.puid)
# 'edfe8468'

### '''=   output.write("-----Friends-------\n")
###    for i in friends:
###        output.write(i.nick_name + " ---> " + i.puid + "\n")
### '''   

