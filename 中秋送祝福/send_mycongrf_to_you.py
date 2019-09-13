import itchat
import pandas as pd
import random
import re

@itchat.msg_register([itchat.content.TEXT],isFriendChat=True)
def information(msg):
    if msg['Type']=='Text':
        content = msg['Content']
        if content.find('中秋')>=0:
            content = msg['Content']
            data = pd.read_excel('F:\\congrf.xls')
            pd.set_option('display.max_colwidth',1000)
            ra = random.randint(1,31)
            strr = str(data[data.序号 == ra].祝福语)
            if strr.find('Series')==0:
                print('找不到资源')
            else:
                strr0 = re.findall(r".*\s(.+)\nName.*", strr)
                strr = ''.join(strr0)
                itchat.send(strr,msg['FromUserName'])
                print(msg['FromUserName'])
                print(strr)
        else:
            print('非祝福消息！')
            

def login():
    print('微信已登录……')
def ex():
    print('微信已退出……')

itchat.auto_login(hotReload=True,loginCallback=login,exitCallback=ex)
itchat.run()
