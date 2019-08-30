import requests
from lxml import etree
import random
import xlwt
import re

def get_IP():
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

    proxyIPs = ['27.188.64.70','163.204.246.139','121.13.252.60']

    proxyIP = random.choice(proxyIPs)
    proxies = {
            'http': proxyIP,
            'https': proxyIP
        }

    url = 'https://www.kuaidaili.com/free/'
    html = requests.get(url,proxies).text
    html1 = etree.HTML(html)
    datas=[]
    ports=[]
    for i in range(17):
        data = html1.xpath('//*[@id="list"]/table/tbody/tr['+str(i)+']/td[1]/text()')
        port = html1.xpath('//*[@id="list"]/table/tbody/tr['+str(i)+']/td[2]/text()')
        datas += data
        ports += port
    write_excel(datas,ports)

def write_excel(datas,ports):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('代理池',cell_overwrite_ok=True)
    row0 = ['IP地址','端口号']
    column0 = datas
    column1 = ports
    for i in range(len(row0)):
        sheet1.write(0,i,row0[i],xlwt.XFStyle())
    for i in range(len(column0)):
        sheet1.write(i+1,0,column0[i],xlwt.XFStyle())
    for i in range(len(column1)):
        sheet1.write(i+1,1,column1[i],xlwt.XFStyle())
    f.save('D:\\IPsave.xls')
    
if __name__ == '__main__':
    get_IP()

