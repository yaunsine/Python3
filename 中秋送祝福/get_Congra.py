from urllib import request
from lxml import etree
import read_IP
import random
import re
import xlwt

'''

/html/body/div[7]/div[1]/div[1]/div[2]/p[2]

/html/body/div[7]/div[1]/div[1]/div[2]/p[3]
。。。
。。。
/html/body/div[7]/div[1]/div[1]/div[2]/p[32]
'''

def getContent():
    url="http://www.hengexing.com/z/80866_8.html"
    proxyIPs = read_IP.read_excel()
    proxyIP = random.choice(proxyIPs)
    proxies = {
        'https':proxyIP,
        'http':proxyIP
        }
    html = request.urlopen(url).read().decode('gbk')
    html0 = etree.HTML(html)
    global congrf,count
    count = []
    congrf= []
    co = 0
    for i in range(1,32,1):
        data = html0.xpath('/html/body/div[7]/div[1]/div[1]/div[2]/p['+str(i)+']/text()')
        data1 = str(data).split('\\xa0 \\xa0\\xa0')[0].split('\\n\\t')[1]
        congrf.append(data1)
        co += 1
        count.append(co)
    write_excel(count,congrf)

def write_excel(datas,ports):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('中秋祝福回复',cell_overwrite_ok=True)
    row0 = ['序号','祝福语']
    column0 = datas
    column1 = ports
    for i in range(len(row0)):
        sheet1.write(0,i,row0[i],xlwt.XFStyle())
    for i in range(len(column0)):
        sheet1.write(i+1,0,column0[i],xlwt.XFStyle())
    for i in range(len(column1)):
        sheet1.write(i+1,1,column1[i],xlwt.XFStyle())
    f.save('F:\\congrf.xls')    

getContent()

