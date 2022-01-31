import requests
from bs4 import BeautifulSoup
from datetime import datetime

# get은 GET 요청을 보내는 기능
# 요청과 응답 : 요청은 손님(클라이언트)의 주문서(daum의 정보) , 응답은 요리사(서버)의 음식(홈페이지의 HTML 정보)
# print(requests.get)

url = "http://www.daum.net"
response = requests.get(url)

# print(response.text)
# print(response.url)
# print(response.content)
# print(response.encoding)
# print(response.headers)
# print(response.json)
# print(response.links)
# print(response.ok)
# print(response.status_code)


print(BeautifulSoup(response.text, 'html.parser'))

#response.text랑 어떤것이 다른지 : str, ns4.BeautifulSoup(통, 바구니) 타입
print(type(response.text))
print(type(BeautifulSoup(response.text, 'html.parser')))


# BeautifulSoup을 파싱하는법
# html.parser : 파싱을 도와주는 것(의미있는 단위로 데이터를 추출)
soup = BeautifulSoup(response.text, 'html.parser')


file = open("daum.html", "w")
file.write(response.text)
file.close()

print(soup.title) # <title>Daum</title>
print(soup.title.string) # Daum
print(soup.span) # 최상단 span태그 한개
print(soup.findAll('span')) # span 태그 전체 


# html 문서에서 모든 a태그를 가져온느 코드
print(soup.findAll("a", "link_favorsch"))




#파일로 출력하기, 이전의 파일뒤에 또 글을 추가 하고 싶으면 w를 a로 바꾸면 된다.
search_rank_file = open("rankresult.txt","a")

#이쁘게 출력하기
rank = 1
print(datetime.today())
print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

results = soup.findAll("a", "link_favorsch")
for result in results:
    #파일로 저장
    search_rank_file.write(str(rank)+"위:"+result.get_text()+ "\n")
    
    print(rank, "위 : ", result.get_text(),"\n")
    rank += 1


