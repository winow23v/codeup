import requests
from bs4 import BeautifulSoup
url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status() # 오류시 종료
soup = BeautifulSoup(res.text , 'lxml')
ranks = soup.find('ol', {'id':'realTimeRankFavorite'}).find_all('li')
#print(ranks)
for rank in ranks :
    print(rank.a['title'])
    prefix = ''
    if rank.span.img['title'] == '순위하락':
        prefix = '-'
    elif rank.span.img['title'] =='순위상승':
        prefix='+'
    print('변동:'+prefix +rank.span.img.next_sibling.strip())