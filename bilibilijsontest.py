from urllib.request import urlopen
import json
 
json_url = 'https://api.bilibili.com/x/space/arc/search?mid=396860076&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
 
response = urlopen(json_url)
#读取数据
req = response.read()
with open('xiaomo_1.json','wb+') as f:
    f.write(req)
#加载json格式
file_urllid = json.loads(req)
print(file_urllid)