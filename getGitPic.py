from urllib import request
import os
from lxml import etree
import re
import time

#创建文件夹，开始主程序
def create_dir(folder='F:\\gitpic',url='https://octodex.github.com'):
    if os.path.exists(folder)==False:
        #创建指定文件夹
        os.mkdir(folder)
        os.chdir(folder)
    else:
        print('%s文件夹已存在'%folder)
    get_img(folder,url)

#保存下载图片
def get_img(folder,url):
    picAdrs = getURL(url)
    count = 0
    for i in picAdrs:
        count += 1
        print("第%d张图片正在下载……"%count)
        #得到图片名称
        filename = i.split('/')[-1]
        #图片地址
        urleach= url+i
        #图片写入F:/gitpic目录下
        with open(folder+'/'+filename,'wb') as f:
            img = request.urlopen(urleach).read()
            f.write(img)
            #time.sleep(2)
    print('已完成下载')

#处理链接，得到图片地址
def getURL(url):
    html = request.urlopen(url).read().decode('utf-8')#解析网页元素
    #d-block width-fit height-auto rounded-1
    listimg = [i.start() for i in re.finditer('d-block width-fit height-auto rounded-1',html)]#查找存放图片链接的位置
    #148张图片
    lis = []#建立列表，存放所有图片链接
    da = [] #处理中间字符串数据
    for i in range(len(listimg)):
        dd = html[listimg[i]+84:listimg[i]+140]
        #找到src双引号的内容
        if dd.count('"')>=2:
            da = [i.start() for i in re.finditer('"',dd)]
            dd = dd[da[0]+1:da[1]]
            lis.append(dd)
    #传递链接供保存图片
    return lis

#程序入口
create_dir()
