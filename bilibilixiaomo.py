from urllib.request import urlopen
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import json
import math
 
xiaomoshipinbaseurl = 'https://www.bilibili.com/video/av'
xiaomo_file = open("xiaomoaid_1.txt", "wb+")
json_baseurl = 'https://api.bilibili.com/x/space/arc/search?mid=396860076&ps='
# json_url = 'https://api.bilibili.com/x/space/arc/search?mid=396860076&ps=30&tid=0&pn=1&keyword=&order=pubdate&jsonp=jsonp'

i = 0
while i < 9:
    json_url = json_baseurl + "30" + "&tid=0&pn=" + str(i + 1) + "&keyword=&order=pubdate&jsonp=jsonp"
    print(json_url)
    response = urlopen(json_url)
    #读取数据
    req = response.read()
    # with open('xiaomo_1.json','wb+') as f:
    #     f.write(req)
    #加载json格式
    file_urllid = json.loads(req)
    video_count = file_urllid['data']['page']['count']
    video_ps = file_urllid['data']['page']['ps']
    video_pn = file_urllid['data']['page']['pn']
    video_vlist = file_urllid['data']['list']['vlist']

    print(str(math.ceil(video_count / video_ps)))
    i += 1
    for video in video_vlist:
        xiaomo_file.write((str(video['aid']) + '\n').encode())
xiaomo_file.close()