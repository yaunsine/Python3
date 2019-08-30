import urllib.request as urr
response = urr.urlopen('http://www.yworld.xyz')
html = response.read()
index = html.decode('utf-8')
file  = open('E:\\index.html','w').write(index)
