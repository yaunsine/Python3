import urllib.request as urr
import json
import urllib.parse as urp
import time
data={}
def getmovies(data):
    print("dssd")
    
    
    data['cover']="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2518852413.jpg"
    data['cover_x']='960'
    data['cover_y']='1500'
    data['id']="26997663"
    data['is_new']=False
    data['playable']=True
    data['rate']="6.3"
    data['title']="寂静之地"
    data['url']="https://movie.douban.com/subject/26997663/"
    print(data)
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E6%81%90%E6%80%96&sort=recommend&page_limit=20&page_start=0'
    data = urp.urlencode(data).encode('utf-8')
    response = urr.urlopen(url,data)
    html = response.read().decode('utf-8')
    target = json.loads(html)


if __name__ == '__main__':
    getmovies(data)
