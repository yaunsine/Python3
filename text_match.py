import itchat
import re


def match_url(a):
    url = '.*https?:\/\/m\.tb\.cn\/.*'
    f = re.search(url,a)
    if not f:
        return False
    else:
        return True


@itchat.msg_register([itchat.content.TEXT], isFriendChat=True,isMpChat=True)
def information(msg):
    info = itchat.search_friends(name='比淘惠')
    if msg['Type'] == 'Text' and match_url(msg['Content']):
        global name2,name3
        a = msg['Content']
        
        name1 = info[0]['UserName']
        name2 = msg['FromUserName']
        name3 = msg['ToUserName']
        itchat.send("正在为您查询……",name2)
        
        itchat.send(a,name1)
        

@itchat.msg_register([itchat.content.SHARING], isFriendChat=True,isMpChat=True)
def url_info(msg):
    name = itchat.search_friends(name='比淘惠')[0]['UserName']
    if msg['Type']=='Sharing':
        nm = msg['FromUserName']
        if name==nm:
            l=msg['Content']

            begin=l.find('<des>')

            end=l.rfind('</des>')

            ss=l[begin+5:end]
            goods = '*****商品*****\n标题：'+str(ss)+'\n*****优惠信息*****\n'+str(msg['Text'])+'\n优惠链接：'+str(msg['Url'])+'\n*****优惠券查询结果*****'
            itchat.send(goods,name2)
            
            print(goods)
        else:
            print('非商品链接')
    else:
        print('非链接')
        

itchat.auto_login()
itchat.run()

