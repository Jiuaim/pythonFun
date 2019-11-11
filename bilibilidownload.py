import sys
from you_get import common as you_get       #导入you-get库

directory = r'fun/'                         #设置下载目录
base_url = 'https://www.bilibili.com/video/av'
aid_file = open("xiaomoaid_1.txt", "r")
aid_data = aid_file.read()
all_aid = aid_data.split('\n')

for i in range(3):
# for aid in all_aid:
    aid = all_aid[i]
    print(str(aid))
    url = base_url + str(aid)
    sys.argv = ['you-get','-o',directory,url]       #sys传递参数执行下载，就像在命令行一样
    you_get.main()

aid_file.close()