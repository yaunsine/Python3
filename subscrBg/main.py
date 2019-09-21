import requests
from lxml import etree
import random
import smtplib
import requests
from email.mime.text import MIMEText
import re
import schedule
import time

#请求连接获取文章内容
def deal_url(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    proxyIPs = ['27.188.64.70','163.204.246.139','121.13.252.60','180.118.247.69','111.75.223.9','1.193.244.92']
    proxyIP = random.choice(proxyIPs)
    proxies = {
            'http': proxyIP,
            'https': proxyIP
        }
    html = requests.get(url,proxies).text
    return html

#获取更新的链接
def geturls():
    url = 'https://language.chinadaily.com.cn/news_bilingual/'
    html = deal_url(url)
    alist = [i.start() for i in re.finditer('gy_box_txt2',html)]    #查找到首页中包含文章的链接起始位置
    da = []
    urllist = []
    for i in range(len(alist)):
        dd = html[alist[i]+68:alist[i]+150]     #截取链接字段
        if dd.count('"')>=2:
            da = [i.start() for i in re.finditer('"',dd)]   #定位到超链接引号数组位置
            dd = dd[da[0]+1:da[1]]      #提取两个引号中的字段
            urllist.append(dd)      #取到的链接存入列表
    return urllist

#获取到正文和标题
def getContent():
    #随机获取一篇文章
    ran = random.randint(0,len(geturls())-1)
    url = 'https:'+geturls()[0]
    html = deal_url(url)
    html0 = etree.HTML(html)
    #分割出标题
    title0 = ''
    title = [i.start() for i in re.finditer('main_title1',html)]
    tit = html[title[0]+12:title[0]+100]
    a = tit.index('>')
    b = tit.index('<')
    title0 = tit[a+1:b]
    #分割出正文部分
    datas = ''
    for i in range(1,100,1):
        data = str(html0.xpath('//*[@id="Content"]/p['+str(i)+']/text()'))
        ss = '\xa0|\[\]|\"]|\[\"|\[\'|\'\]'     #正则匹配去除[''],[""]
        data = re.sub(ss,'',data)
        data = re.sub(r'\\xa0','',data)     #正则匹配去除\xa0
        data += '\n'*2
        if data.find('来源：')<=0:
            datas+=data
        else:
            break
    return title0,datas

#邮箱发送
def sendtoEmail():  

    msg = MIMEText(getContent()[1]) #发送正文部分
    msg["Subject"] = '【原视界文章推送】'+getContent()[0]    #发送标题部分
    msg["From"]    = user
    msg["To"]      = to
    try:
        s = smtplib.SMTP_SSL("smtp.qq.com", 465)
        s.login(user, pwd)
        s.sendmail(user, to, msg.as_string())
        s.quit()
        print("发送成功!",time.ctime(time.time()))
    except smtplib.SMTPException as e: 
        print ("发送出错,%s" %e)

#设置定时发送
def send_mail_by_schedule():
    schedule.every().day.at("12:00").do(sendtoEmail)
    schedule.every().day.at("18:00").do(sendtoEmail)
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__=="__main__":
    print('=======订阅系统=======')
    global user,pwd,to
    user = input('请输入QQ号:')+'@qq.com'
    pwd = input('请输入邮箱授权码:')
    to = input('请输入订阅号:')+'@qq.com'
    print('虫子管家已为您开启订阅，请勿退出此程序并保持网络通畅，订阅文章于每天12:00和18:00准时发送至您的邮箱！')
    send_mail_by_schedule()
