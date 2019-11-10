from urllib.request import urlopen
import json
 
xiaomoshipinbaseurl = 'https://www.bilibili.com/video/av'
xiaomo_file = open("xiaomoaid_1.txt", "wb+")
json_url = 'https://api.bilibili.com/x/space/arc/search?mid=396860076&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'
 
response = urlopen(json_url)
#读取数据
req = response.read()
# with open('xiaomo_1.json','wb+') as f:
#     f.write(req)
#加载json格式
file_urllid = json.loads(req)
video_vlist = file_urllid['data']['list']['vlist']


for video in video_vlist:
    xiaomo_file.write((str(video['aid']) + '\n').encode())
xiaomo_file.close()

