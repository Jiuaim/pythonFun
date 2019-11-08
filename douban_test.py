import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from bs4 import BeautifulSoup
from distutils.filelist import findall 

startIndex = 25
doubanurl2 = "https://movie.douban.com/top250?start="

print('你个二货')

print("豆瓣电影TOP250" + "\n" +" 影片名              评分       评价人数     链接 ")
a = 0
while a < 10:
    if a == 0:
        url = "https://movie.douban.com/top250?format=text"
    else:
        url = doubanurl2 + str(25 * a) + "&filter="
    a += 1
    page = urllib.request.urlopen(url)
    content = page.read()

    soup = BeautifulSoup(content,"html.parser")  
    for tag in soup.find_all('div', class_='info'):    
       # print tag  
        m_name = tag.find('span', class_='title').get_text()
        m_rating_score = float(tag.find('span',class_='rating_num').get_text())          
        m_people = tag.find('div',class_="star")  
        m_span = m_people.findAll('span')  
        m_peoplecount = m_span[3].contents[0]  
        m_url=tag.find('a').get('href')  
        print( m_name+"        "  +  str(m_rating_score)   + "           " + m_peoplecount + "    " + m_url ) 
