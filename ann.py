# 1. check_even_odd : 짝수와 홀수 판정 함수
# 2. analyze_sentiment : 감정 분석 함수
# 3. wrap : 문자열을 특정 문자로 감싸는 함수
# 4. plot_bar_graph : 막대 그래프 그리는 함수
# 5. plot_pie_graph : 원형 그래프 그리는 함수
# 6. hankook(키워드,페이지수) : 한국일보 데이터 수집
# 7. dongah(키워드,페이지수) : 동아일보 데이터 수집
# 8. ja(키워드,페이지수) : 중앙일보 데이터 수집
# 9. han(키워드,페이지수) : 한겨례 데이터 수집
# 10. km(키워드,페이지수) : 국민일보 데이터 수집
# 11. chosun(키워드, 페이지수) : 조선일보 데이터 수집
# 12. naver_blog2(키워드, 페이지수) : 네이버 블러그 데이터 수집
# 13. naver_shopping(키워드, 페이지수) : 네이버 쇼핑 데이터 수집
# 14. get_coupang_data(키워드, 페이지수) : 쿠팡 데이터 수집
# 15. download_image_bing(kw) : 빙 이미지 수집, c://data_image_bing에 저장됨
# 16. download_image_naver(kw) : 네이버 이미지 수집, c://data_image_naver에 저장됨
# 17. download_image_google(kw) : 구글 이미지 수집, c://data_image_google에 저장됨
# 18. download_image_daum(kw) : 구글 이미지 수집, c://data_image_daum에 저장됨
# 19. scroll_youtube(kw) : 유튜브 댓글 수집, c://data에 저장됨
# 20. relation_word_ja(kw) : 중앙일보 2024 언급량 시각화
# 21. related_wordcloud(데이터 위치, keyword) : 연관어 분석 시각화


#1. 짝수 홀수 판정 함수 
def check_even_odd(number):
    if number % 2 == 1:
        return '홀수입니다.'
    else: 
        return '짝수입니다.'


#2. 감정 분석 함수 
#df = pd.DataFrame({'conversation':elsa_lines})
def analyze_sentiment(text):
    blob = TextBlob(text)      #TextBlob 객체를 생성 
    score = blob.sentiment.polarity  #감정 점수 계산 
    return score       
# 감정 분석 점수 컬럼 추가 
#df['sentiment'] = df['conversation'].map(analyze_sentiment)


#3. 문자열을 특정 문자로 감싸는 함수
def wrap(text, char="'"):
    return char+text+char


#4. 막대 그래프 
import plotly.graph_objects as go
def plot_bar_graph(x, y):
    fig = go.Figure(data=[go.Bar(x=x, y=y, marker_color="#FC9191")])
    fig.update_layout(
        title="막대 그래프 예시",
        xaxis_title="X 축",
        yaxis_title="Y 축",
        template="plotly",  # 다른 스타일 사용 가능: "plotly_dark", "ggplot2"
        font=dict(
            family="Arial, sans-serif",
            size=14,
            color="RebeccaPurple"
    )
)
    fig.show()


#5. 원형 그래프 
import plotly.graph_objects as go   
def plot_pie_chart(labels, values):  
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)]) 
    fig.update_layout(
        title="원형 그래프 예시",
        template="plotly",  # 다른 스타일 사용 가능: "plotly_dark", "ggplot2"
        font=dict(    
            family="Arial, sans-serif",
            size=14,
            color="RebeccaPurple"
        )
    )
    fig.show()


#6. 한국일보 데이터 수집 함수 2개
import   urllib.request
from bs4  import BeautifulSoup
import  time

# 상세 기사 url 수집함수
def hankook_detail_url(keyword, num):
    text1 = urllib.parse.quote(keyword)
    params = [ ]       
    for  i  in  range(1,num+1):
        list_url = "https://search.hankookilbo.com/Search?Page=" + str(i) + "&tab=NEWS&sort=relation&searchText=" + text1 + "&searchTypeSet=TITLE,CONTENTS&selectedPeriod=%EC%A0%84%EC%B2%B4&filter=head"
        url = urllib.request.Request( list_url )
        f = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(  f ,  "html.parser")
        
        for  i   in  soup.select( "div.inn > h3.board-list.h3.pc_only > a" ):
            params.append( i.get("href")  )
        time.sleep(1)
	    
    return  params

# 기사 본문 수집 함수
def hankook(keyword, num):
    f_hankook = open("c:\\data\\hankook.txt", "w", encoding="utf8" )
    result =  hankook_detail_url(keyword, num)
    for i  in result:
        url = urllib.request.Request( i )
        f = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup( f , "html.parser") 

        # 날짜 가져오기
        date_text = ""
        for  d  in  soup.select("div.innerwrap > div > div.info > dl"):
            date_text = d.text.strip()
            f_hankook.write( date_text + '\n') 
            print( d.text ) 

        # 본문 가져오기 
        for  i  in  soup.select("div.innerwrap div.col-main p"):  # div.innterwrap 밑에 p 테그들은 다 선택해라
            article_text = i.text.strip()   
            f_hankook.write( article_text + '\n') 
            print(article_text) 

        f_hankook.write("\n" + "="*50 + "\n\n") 

    f_hankook.close()

# 7. 동아일보 데이터 수집 함수 2개 
import urllib.request
from bs4  import BeautifulSoup
import  time

## 상세 기사 url 수집함수

def da_detail_url(keyword, num):
    
    text1 = urllib.parse.quote(keyword)
    
    params = [ ]   # 비어있는 리스트를 생성합니다. 
    
    for  i  in  range(1,num+10):
        list_url = "https://www.donga.com/news/search?"+ str(i)+"&query="+text1+"&check_news=91&sorting=1&search_date=1&v1=&v2=&more=1"
        url = urllib.request.Request( list_url )
        f = urllib.request.urlopen(url).read().decode("utf-8")
    
        soup = BeautifulSoup(  f ,  "html.parser")
        
        for  i   in  soup.select( "article > div > h4 > a" ):
            params.append( i.get("href")  )
            
        time.sleep(1)
    
    return  params


## 기사 본문 수집 함수
def da(keyword, num):
    f_da = open("c:\\data\\da.txt", "w", encoding="utf8" )
    
    result =  da_detail_url(keyword, num)
    
    for i  in result:
        url = urllib.request.Request( i )
        f = urllib.request.urlopen(url).read().decode("utf-8")
        
        soup = BeautifulSoup( f , "html.parser") 

        # 날짜 가져오기
        date_text = ""
        for  d  in  soup.select("header > div > section > ul"):
            date_text = d.text.strip()
            f_da.write( date_text + '\n') # 날짜 저장
            print( d.text ) 

        # 본문 가져오기 
        for  i  in  soup.select("div > div.main_view > section.news_view"):  # div.innterwrap 밑에 p 테그들은 다 선택해라
            article_text = i.text.strip()   # 본문 기사 양쪽에 공백을 잘라냄
            f_da.write( article_text + '\n') # 본문기사 저장
            print(article_text) 

        f_da.write("\n" + "="*50 + "\n\n") # 기사 구분

    f_da.close()


#8. 중앙일보 함수 2개
import urllib.request
from bs4 import BeautifulSoup
import time

# 상세 기사 url 수집함수

def ja_detail_url(keyword, num):
    
    text1 = urllib.parse.quote(keyword)
    
    params = [ ]   # 비어있는 리스트를 생성합니다. 
    
    for  i  in  range(1,num+1):
        list_url = "https://www.joongang.co.kr/search/news?keyword="+text1+"&page="+str(i)
        url = urllib.request.Request( list_url )
        f = urllib.request.urlopen(url).read().decode("utf-8")
    
        soup = BeautifulSoup(  f ,  "html.parser")

        #container > section > div > section > ul > li:nth-child(1) > div > h2 > a
        for  i   in  soup.select( "div.card_body > h2.headline > a" ):
            params.append( i.get("href")  )
        if len(params) > 5:  #맨 끝에 5개의 기사를 제외시킵니다. 
            params = params[:-5]
            
        time.sleep(1)
    
    return  params



# 기사 본문 수집 함수
def ja(keyword, num):
    f_ja = open("c:\\data\\joongang.txt", "w", encoding="utf8")
    
    result = ja_detail_url(keyword, num)
    cnt = 0 
    for i in result:
        url = urllib.request.Request(i)
        f = urllib.request.urlopen(url).read().decode("utf-8")
        
        soup = BeautifulSoup(f, "html.parser")

        # 날짜 가져오기 (datetime 속성 값)
        date_text = ""
        date_element = soup.select_one("time")
        if date_element:
            date_text = date_element['datetime'].strip()  # datetime 속성 값 가져오기
            f_ja.write(date_text + '\n')  # 날짜 저장
            print(date_text)
            cnt = cnt + 1
    
        # # 본문 가져오기 
        for i in soup.select("article.article > div p"): 
            article_text = i.text.strip()   # 본문 기사 양쪽에 공백을 잘라냄
            f_ja.write(article_text + '\n') # 본문기사 저장
            print(article_text)

        f_ja.write("\n" + "="*50 + "\n\n")  # 기사 구분
        
    f_ja.close()


# 9. 한겨레 함수 2개 
import urllib.request
from bs4 import BeautifulSoup
import time 
from datetime import datetime

#상세 기사 url 수집함수
def han_detail_url(kw, num): 
    text1 = urllib.parse.quote(kw)
    params = []
    params2 = []
    today = datetime.today()
    date = str(today)[0:10].replace("-",".")

    for i in range(1, num+1):
        list_url = "https://search.hani.co.kr/h21?searchword="+text1+"&startdate=1988.01.01&enddate="+date+"&page="+str(i)+"&sort=desc"
        url = urllib.request.Request(list_url)
        f = urllib.request.urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(f, "html.parser")

        #상세 기사 url 가져오기 
        for i in soup.select("div ul article a"):
            params.append(i.get("href"))
        #상세 기사의 날짜 가져오기 
        for i in soup.select('span.article-date'):
            params2.append(i.text)
        time.sleep(1)

    return params, params2

def han(kw, num):
    f_han = open('c:\\data\\han.txt','w',encoding = 'utf-8')
    urls, dates = han_detail_url(kw, num)

    for u, d in zip(urls, dates):
        print(d)
        f_han.write(d + '\n')
    
        url = urllib.request.Request(u)
        f = urllib.request.urlopen(url).read().decode('utf-8')
        soup = BeautifulSoup(f,"html.parser")
        
        for i in soup.select("div p"):
            article_text = i.text.strip()
            f_han.write(article_text + '\n')
            print(article_text)
        f_han.write('\n' + '='*50 + '\n\n')
    f_han.close()


# 10. 국민일보 함수 2개
# 국민일보 신문사 
import   urllib.request
from bs4  import BeautifulSoup
import  time
from  datetime  import  datetime 

# 상세 기사 url 수집함수
def km_detail_url(keyword, num):
    
    text1 = urllib.parse.quote(keyword, encoding="cp949")
    params = [ ]   #  상세기사 url 을 저장하기 위한 리스트 입니다.  
    
    for  i  in  range(1,num+1):
        list_url = "https://www.kmib.co.kr/search/searchResult.asp?searchWord=" + text1 +"&pageNo=" + str(i) + "&period="
        
        # 국민일보 url 에 접속 요청 하기 위한 코드
        url = urllib.request.Request( list_url )  
        
        # 국민일보 신문사 html 코드 수집
        f = urllib.request.urlopen(url).read().decode("cp949") 
        
	# html 코드를 BF 함수를 쓸수있도록 파싱
        soup = BeautifulSoup(  f ,  "html.parser") 
    

        # 상세 기사 url 가져오기 
        for  i   in  soup.select( " div.search_nws >  dl > dt.tit > a" ):
            params.append( i.get("href")  )
            
        time.sleep(1)
    
    return  params
    
    
    
# 기사 본문 수집 함수
def km(keyword, num):
    f_km = open("c:\\data\\km.txt", "w", encoding="cp949" )
    
    result =  km_detail_url(keyword, num)
    
    for i in result:
        url = urllib.request.Request( i )
        f = urllib.request.urlopen(url).read().decode("cp949")

        soup = BeautifulSoup( f , "html.parser") 

        # 날짜 가져오기
        for i in soup.select("div.nwsti > div.nwsti_btm > div.date"):
            date_text = i.text.strip()
            f_km.write(date_text + '\n')
            print(date_text)  

        # 본문 가져오기 
        for  i  in  soup.select("div.NwsCon div#articleBody.tx"):  
            article_text = i.text.strip()   
            f_km.write( article_text + '\n') 
            print(article_text) 

        f_km.write("\n" + "="*50 + "\n\n") 

    f_km.close()


#11. 조선일보 함수 2개
import urllib.request  #웹요청
from bs4 import BeautifulSoup  #HTML 파싱
from selenium import webdriver #브라우져 제어
from selenium.webdriver.chrome.service import Service #드라이버 관리
from selenium.webdriver.common.by import By  #요소 탐색
import time  #대기시간 

#1. 상세 기사 url
def js_detail_url(kw, num):
    #키워드 검색
    text1 = urllib.parse.quote(kw)
    
    #크롬 드라이버의 경로 지정
    service = Service("C:\\data\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service) 
    params = []
    
    for i in range(1, num+1):
        ##콘텐츠-뉴스로 필터링한 후의 링크 
        list_url = "https://www.chosun.com/nsearch/?query="+text1+"&page="+str(i)+"&siteid=www&sort=1&date_period=all&date_start=&date_end=&writer=&field=&emd_word=&expt_word=&opt_chk=false&app_check=0&website=www,chosun&category="
        driver.get(list_url)  #크롬이 열리면서 이 url로 접속합니다.
        time.sleep(5)   #페이지가 완전히 로드 될 떄까지 대기(필요에 따라 조정)
    
    #html 페이지에서 iframe을 찾고 전환하는 코드
    #iframe 내부에 포함된 콘텐츠는 기본 html 문서와 분리 되어 있으므로
    #html 코드에 접근을 할 수 없습니다. 접근할 수 있도록 해주는 코드 
    try:
        iframe = drive.find_element(By.CSS_SELECTOR,"iframe_selector_here")
        driver.switch_to.frame(iframe)
        time.sleep(2)
    except:
        print("iframe을 찾을 수 없습니다. 기본 페이지에서 진행합니다.") 

    soup = BeautifulSoup(driver.page_source, "html.parser")

    #기사 상세 url을 params 리스트에 중복없이 차례대로 추가
    for i in soup.select("a.text__link.story-card__headline"):
        url = i.get("href")
        if url not in params:
            params.append(url)
     
    driver.quit()  #작업이 끝나면 브라우져를 종료합니다. 
    
    return params
    

#2. 기사 본문
def josun(kw, num):
    #조선일보 본문 저장할 텍스트 파일 생성 
    f_josun = open("c:\\data\\josun.txt", "w", encoding='utf8')

    #상세 기사 url 가져오는 코드
    result = js_detail_url(kw, num)
    
    #크롬 드라이버의 경로 지정
    service = Service("C:\\data\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service) 

    for i in result:
        driver.get(i)  #상세 기사 url을 하나씩 엽니다. 
        time.sleep(5) 
        #자바 스크립트 코드가 있을지 모르므로 iframe을 찾아서 html을 본문에 추가함
        try:
            iframe = drive.find_element(By.CSS_SELECTOR,"iframe_selector_here")
            driver.switch_to.frame(iframe)
            time.sleep(2)
        except:
            print("iframe을 찾을 수 없습니다. 기본 페이지에서 진행합니다.")

        soup = BeautifulSoup(driver.page_source, "html.parser")
        
        #본문기사의 날짜 출력하기
        for i in soup.select("div > section > article > div.article-dateline"):
            f_josun.write(i.get_text() + '\n')
            print(i.get_text())
        
        #본문기사의 html 코드를 뽑아냅니다.
        for i in soup.select("section.article-body > p"):
            f_josun.write(i.get_text() + '\n')
            print(i.get_text())
        f_josun.write('\n' + '='*50 + '\n\n')
            
    driver.quit() 
    f_josun.close()


#12. 네이버 블로그 함수 2개
import urllib.request  #웹요청
from bs4 import BeautifulSoup  #HTML 파싱
from selenium import webdriver #브라우져 제어
from selenium.webdriver.chrome.service import Service #드라이버 관리
from selenium.webdriver.common.by import By  #요소 탐색
import time  #대기시간 정해주는 모듈

#1. 상세 링크
def naver_blog(kw, n):
    # 크롬 드라이버의 위치를 지정
    service = Service("C:\\data\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
    driver = webdriver.Chrome(service=service) 
    params = []  
    for i in range(1,n+1):
        time.sleep(1)  #블로그가 글과 사진이 많아서 중간중간 로딩 되는 시간 대기 
        text1 = urllib.parse.quote(kw)
        list_url = "https://section.blog.naver.com/Search/Post.naver?pageNo="+str(i)+"&rangeType=ALL&orderBy=sim&keyword="+text1+""
        
        #크롬 로봇이 웹페이지를 직접 열 수 있게 합니다. 
        driver.get(list_url)
        time.sleep(2)
        
        #크롬 로봇이 직접 연 웹페이지의 html 코드를 가져옵니다.
        html = driver.page_source
        
        #html 코드를 BS로 파싱합니다. 
        #huml.parser 또는 lxml을 사용 (좀 어려운 사이트가 lxml)
        soup = BeautifulSoup(html, "lxml") 
        
        #블로그 상세 url 찾으러 가기
        for i in soup.select("div.desc > a.desc_inner"):
            params.append(i.get("href"))
    
    return params

#2. 네이버 블로그 본문 상세
def naver_blog2(kw, n):
    result = naver_blog(kw, n)

    #크롬 드라이버의 경로 지정
    service = Service("C:\\data\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe")
    driver2 = webdriver.Chrome(service=service) 
    
    #본문을 저장할 파일을 생성
    f2 = open("c:\\data\\naver_blog.txt","w",encoding="utf8")

    #상세 url을 하나씩 가져와서 웹브라우져 열기
    for list_url in result:
        driver2.get(list_url)
        time.sleep(2)  #페이지가 로드 되는 시간을 충분히 줍니다.
        
        #자바 스크립트로 막혀있을지 모를 html 코드를 볼 수 있게 해줍니다.
        #웹페이지에서 ID가 'mainFrame'인 html 요소를 찾습니다. 
        #이 mainFrame의 html 코드가 독립적으로 작동되는 코드여서 찾아서 기존 코드와
        #통합 시키려고 찾습니다. 
        #크롬 개발자 모드 들어가서 맨위쪽에 코듣로 올라가서 
        #iframe 태그를 찾습니다. iframe태그 안에 id이름을 찾고 다음과 같이 적어줍니다. 
        try: 
            element = driver2.find_element(By.ID, 'mainFrame') 
            driver2.switch_to.frame(element)  #통합시키는 코드
            
            #현재 페이지의 html 코드를 불러옵니다.
            html = driver2.page_source
            #BS로 html 코드를 파싱합니다.
            soup = BeautifulSoup(html, "html.parser")

            #날짜검색 
            date2 = soup.select("span.se_publishDate.pcol2")

            #날짜만 추출  #date2가 리스트로 담겨있어서 요소 하나씩 뽑아야 함 
            #print(date2[0].text.strip())
            date_text = date2[0].text.strip()
            print(date_text)
            f2.write(date_text + '\n')

            #본문검색
            base2 = soup.select("div.se-module.se-module-text > p")

            #본문 추출
            for i in base2:
                con_text = i.text.strip()
                print(con_text)
                f2.write(con_text+'\n')

            print('\n\n\n')
            f2.write('\n' + '='*60 + '\n\n') 
        
        except Exception as e:
            print('iframe을 찾을 수 없습니다.',e)

    f2.close()  #텍스트를 파일에 저장
        


#13. 네이버 쇼핑 데이터 수집 함수
######### 네이버 쇼핑 다운까지 업그레이드 ##################
import urllib.request    # 웹요청 모듈 
from bs4 import BeautifulSoup    # html 파싱 모듈 
from selenium import webdriver   # 브라우저 제어 모듈 
from selenium.webdriver.chrome.service import Service   # 드라이버 관리 모듈 
from selenium.webdriver.common.by import By     # 요소 탐색 모듈 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time    # 대기 시간 정해주는 모듈 
from webdriver_manager.chrome import ChromeDriverManager

def naver_shopping(keyword, n):


    # 크롬 로봇 드라이버의 위치를 지정
    chrome_options =  Options()
    # service = Service('C:\\data\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe')
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    # 크롬 드라이버의 위치 지정 후 driver 객체 생성
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    text1 = urllib.parse.quote(keyword)

    list_name = []   #  상품명
    list_price = []  #  상품가격
    list_date = []   # 등록일 

    for i in range(1,1+n):
        list_url = f'https://search.shopping.naver.com/search/all?adQuery={text1}&origQuery={text1}&pagingIndex={i}&pagingSize=40&productSet=total&query={text1}&sort=rel&timestamp=&viewType=list'
        
        # 크롬 로봇에 웹페이지를 엽니다.
        driver.get(list_url)

        # 크롬 로봇에 마우스 스크롤을 아래로 내려서 전체 페이지가 다 보이게 합니다.
        for  i  in  range(1,6):
            driver.find_element(By.XPATH, value='//body').send_keys(Keys.END)
            time.sleep(0.5)

        # 보이는 웹페이지의 html 코드를 뷰티플 스프로 파싱합니다. 
        time.sleep(2) # 웹페이지가 다 뜰 수 있도록 기다려줌 

        # 현재 페이지를 BS 로 파싱
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # 광고 상품 정보가 있는 html 코드 부분으로 접근
        goods_list = soup.select('div.adProduct_item__1zC9h') # 상품명
        price_list = soup.select('strong.adProduct_price__9gODs > span.price > span.price_num__S2p_v > em')  # 가격
        reg_list = soup.select('div.adProduct_etc_box__UJJ90') # 등록일
        
        # 상품명, 가격, 등록일을 리스트에 각각 담아냄 
        for  g,p,r  in  zip( goods_list, price_list, reg_list):
            price_text = p.text.strip()
            reg_list = r.text.strip().lstrip('등록일,리뷰,별점,만,천,백,십,일,구매,(,),1,2,3,4,5,6,7,8,9,0,.,,,찜').rstrip('.정보,신고하기,톡톡,수정요청').rstrip('.정보 ')
            #상품명 
            #print( g.select_one('div.adProduct_title__amInq > a').get('title'), price_text,reg_list)
            #print( '-' * 80 )
            
        # 광고가 아닌 상품 정보가 있는 html 코드 부분으로 접근
        goods_list = soup.select('div.product_item__MDtDF') # 상품명
        price_list = soup.select('strong.product_price__52oO9 > span.price > span.price_num__S2p_v > em')  # 가격
        reg_list = soup.select('div.product_etc_box__ElfVA') # 등록일
        
        # 광고가 아닌 상품명, 가격, 등록일을 리스트에 각각 담아냄 
        for  g,p,r  in  zip( goods_list, price_list, reg_list):
            product_name = g.select_one('div.product_title__Mmw2K > a').get('title')            
            price_text = p.text.strip()
            reg_list = r.text.strip().lstrip('등록일,리뷰,별점,만,천,백,십,일,구매,(,),1,2,3,4,5,6,7,8,9,0,.,,,찜').rstrip('.정보,신고하기,톡톡,수정요청').rstrip('.정보 ')

            # 리스트에 추가하기 
            list_name.append(product_name)
            list_price.append(price_text)
            list_date.append(reg_list) 


    # pandas 데이터 프레임 생성
    df = pd.DataFrame({'상품명':list_name,
                       '가격':list_price,
                       '등록일':list_date}) 
                       
    # csv 파일로 저장
    df.to_csv('c:\\data\\naver_shopping.csv', encoding='utf8', index=False)
    print('성공적으로 c:\\data\\naver_shopping.csv 가 저장되었습니다.') 

            


#14. 쿠팡
import  requests    # 크롬 로봇 안쓰고 웹에 접근하는 모듈
from  bs4  import BeautifulSoup
import  pandas  as  pd

def get_coupang_data(keyword, pages):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://www.coupang.com/"
    }
    list_name = []
    list_price = [] 
    list_review = []
    list_star = [] 
    list_ad = []
    list_rank = []
    list_url = []

    for   page  in   range( 1, pages+1):
        search_url = f"https://www.coupang.com/np/search?q={keyword}&channel=user&page={page}"
        response = requests.get(search_url, headers=headers)
        #print(response)  # <Response [200]> 이렇게 나오면 정상적으로 접근이 된것임

        if  response.status_code == 200:  # 사이트 접속이 정상이면 
            soup = BeautifulSoup( response.text, 'html.parser')
            goods_list = soup.select('ul.search-product-list > li')
            #print(goods_list)

            for  item  in  goods_list:
                #상품명 가져오기
                item_name = item.select_one('div.name')
                if item_name:
                    list_name.append( item_name.text.strip() )
                else:
                    list_name.append('')
                    
                #상품가격 가져오기 
                item_price = item.select_one('strong.price-value')
                if item_price:
                    list_price.append( item_price.text.strip() )
                else:
                    list_price.append('')

                #리뷰수 가져오기 
                descriptions_inner=item.select_one('div.descriptions-inner') # 상품의 상세정보
                if descriptions_inner and descriptions_inner.select_one('div.other-info'):  # 상세정보도 있고 기타 정보도 있으면                 
                    item_review = descriptions_inner.select_one('span.rating-total-count')
                    if item_review:
                        list_review.append(item_review.text.strip('()')) 
                    else:
                        list_review.append('0')  # 리뷰수가 없으면 0 으로 넣어라 
                else:
                    list_review.append('0')   # 상품의 기타정보가 없으면 0으로 넣어라

                #별점 가져오기 
                descriptions_inner=item.select_one('div.descriptions-inner')
                if descriptions_inner and descriptions_inner.select_one('div.other-info'):
                    item_star = descriptions_inner.select_one('em.rating')
                    if item_star:
                        list_star.append(item_star.text.strip() )
                    else:
                        list_star.append('0')    # 별점이 없으면 0으로 넣어라 !
                else:
                    list_star.append('0')        # 상품의 기타정보가 없으면 0으로 넣어라 !
                        
                # 광고 상품 여부 가져오기 
                descriptions_inner=item.select_one('div.descriptions-inner')
                if descriptions_inner and descriptions_inner.select_one('div.other-info'):
                    item_ad = descriptions_inner.select_one('span.ad-badge-text')
                    if item_ad:
                        list_ad.append('O' )
                    else:
                        list_ad.append('X')    # 광고가 아니면 0으로 넣어라 !
                else:
                    list_ad.append('X')        # 상품의 기타정보가 없으면 0으로 넣어라 !

                # 순위 가져오기 
                item_rank = item.select_one('span[class^="number no-"]')  # 클래스 이름이 number no-로 시작하는 걸 찾아라
                if item_rank:
                    list_rank.append(item_rank.text.strip())
                else:
                    list_rank.append('')  # 순위가 업으면 NA로 넣어라

                # 상품의 상세 url 가져오기
                item_url = item.select_one('a.search-product-link') 
                if item_url:
                    list_url.append("https://www.coupang.com"+item_url['href'])
                else:
                    list_url.append('')         

        
        # 판다스 데이터 프레임 만들기
        df = pd.DataFrame( {  '상품명' : list_name,
                              '가격' :  list_price,
                            '리뷰수' :  list_review,
                            '별점'   :  list_star,
                            '광고여부' : list_ad,
                            '순위' : list_rank,
                           '상세url':list_url } )

    # df 데이터프레임의 결과를 csv 파일로 내립니다. 
    df.to_csv("c:\\data\\coupang_shopping.csv", encoding="utf8", index=False)
    print('성공적으로 c:\\data\\coupang_shopping.csv 가 저장되었습니다')
        

get_coupang_data('그릭 요거트', 1)




#15. 빙 이미지 수집 
def download_image_bing(kw):
    import urllib.request
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys 
    import time
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service 
    
    # 크롬 드라이버의 위치 지정 후 driver 객체 생성
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # 네이버 이미지 검색 페이지로 이동
    driver.get("https://www.bing.com/images/feed?form=Z9LH")
    
    time.sleep(5)
    
    # 검색창에 검색 키워드를 입력
    search = driver.find_element(By.XPATH, "//*[@class='b_searchbox ']")
    search.send_keys(kw)
    search.send_keys(Keys.RETURN)
    
    #이미지가 불러와질때까지 대기 하는 시간 지정
    time.sleep(2)
    
    # 페이지를 아래로 스크롤하여 더 많은 이미지를 로드
    for i in range(1, 10):
        driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
        time.sleep(5)
    
    # 이미지 더보기 버튼 클릭
    try: 
        show_more_button = driver.find_element(By.XPATH, "//a[contains(@class, 'btn_seemore')]")
        show_more_button.click()
    except Exceptions as e:
        print("결과 더보기 버튼이 없습니다. 다음 단계로 넘어갑니다.")
        print(f'오류:{e}')
    
    # 페이지를 아래로 스크롤하여 더 많은 이미지를 로드
    for i in range(1, 10):
        driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
        time.sleep(5)
    
    # 현재 페이지의 HTML 소스 코드를 가져와 파싱
    html = driver.page_source  
    soup = BeautifulSoup(html, "lxml")
    #print(soup)
    
    # 이미지 태그를 찾고 이미지 URL을 수집
    params = []
    imgList = soup.find_all('img',class_='mimg')
    for i in imgList:
        params.append(i.get('src'))
    
    # 수집한 이미지 URL을 사용하여 이미지를 다운로드
    for idx, p in enumerate(params_n, 1):
        urllib.request.urlretrieve(p, "c:\\data_image_bing\\" + str(idx) + ".jpg")
    
    # 작업 완료 후 브라우저 닫기
    driver.quit()


#16. 네이버 이미지 다운로드
def download_image_naver(kw):
    import urllib.request
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys 
    import time
    from selenium.webdriver.common.by import By
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.service import Service 
    
    # 크롬 드라이버의 위치 지정 후 driver 객체 생성
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # 네이버 이미지 검색 페이지로 이동
    driver.get("https://search.naver.com/search.naver?where=image&sm=stb_nmr&")
    
    time.sleep(5)
    
    # 검색창에 검색 키워드를 입력
    #search = driver.find_element(By.XPATH, "//*[@class='box_window']")
    search = driver.find_element(By.XPATH, '//*[@id="nx_query"]')
    search.send_keys(kw)
    search.send_keys(Keys.RETURN)
    
    # 페이지를 아래로 스크롤하여 더 많은 이미지를 로드
    for i in range(1, 20):
        driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
        time.sleep(5)
    
    # 현재 페이지의 HTML 소스 코드를 가져와 파싱
    html = driver.page_source  
    soup = BeautifulSoup(html, "lxml")
    
    # 이미지 태그를 찾고 이미지 URL을 수집
    params_n = []
    imgList = soup.find_all("div", class_=["image_tile_bx", "_fe_image_viewer_focus_target"])
    for i in imgList:
        img_tag = i.find("img")  # 'img' 태그 찾기
        if img_tag:
            img_url = img_tag.get("data-src", img_tag.get("src"))  # 이미지 URL 가져오기
            if img_url:
                params_n.append(img_url)
    
    # 수집한 이미지 URL을 사용하여 이미지를 다운로드
    for idx, p in enumerate(params_n, 1):
        urllib.request.urlretrieve(p, "c:\\data_image_naver\\" + str(idx) + ".jpg")
    
    # 작업 완료 후 브라우저 닫기
    driver.quit()



#17. 구글 이미지 다운로드 
#####구글 이미지 
def download_image_google(kw):
    import urllib.request
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys 
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service 
    from webdriver_manager.chrome import ChromeDriverManager
    
    # 크롬 드라이버의 위치 지정후 driver 객체를 생성
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # 구글 이미지 검색 페이지로 이동
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&ei=l1AdWbegOcra8QXvtr-4Cw&ved=0EKouCBUoAQ")
    
    # 검색창 객체 생성
    #search = driver.find_element(By.XPATH, "//*[@class='gLFyf']")
    search = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')  #동현's 방법
    
    # 검색어 입력
    name = kw
    search.send_keys(name)
    
    # 엔터 입력
    search.submit()
    
    # 스크롤을 아래로 내려서 이미지를 더 로드
    for i in range(1, 9):
        driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
        time.sleep(10)
    
    # 결과 더보기 클릭 (버튼이 있는 경우에만)
    try:
        driver.find_element(By.XPATH, "//*[@class='mye4qd']").click()
        # 결과 더보기를 눌렀으니 마우스를 다시 아래로 내림
        for i in range(1, 9):
            driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
            time.sleep(10)
    except Exception as e:
        print("결과 더보기 버튼이 없습니다. 다음 단계로 넘어갑니다.")
    
    # 현재 페이지의 HTML 코드를 가져옴
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    
    # 이미지 URL들을 params 리스트에 담기
    params_g = []
    imgList = soup.find_all("g-img", class_="mNsIhb")
    
    for g_img in imgList:
        img_tag = g_img.find("img")  # g-img 태그 내의 img 태그를 찾음
        if img_tag:
            img_url = img_tag.get("src", img_tag.get("data-src"))
            params_g.append(img_url)
    
    # 결과 확인
    #print(params_g)
    
    # 이미지들을 로컬 디렉토리에 저장
    for idx, p in enumerate(params_g, 1):
        if p:
            urllib.request.urlretrieve(p, "c:\\data_image_google\\" + str(idx) + ".jpg")
        else:
            print(f"이미지 {idx}는 다운로드할 수 없습니다.")



#18. 다음 이미지 다운로드 
def download_image_daum(kw):
    import urllib.request
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys 
    import time
    from selenium.webdriver.common.by import By
    from selenium.webdriver.chrome.service import Service 
    from webdriver_manager.chrome import ChromeDriverManager
    
    # 크롬 드라이버의 위치 지정후 driver 객체를 생성
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    # 다음 이미지 검색 페이지로 이동
    driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=")
    
    # 검색창 객체 생성
    #search = driver.find_element(By.XPATH, "//*[@class='gLFyf']")
    search = driver.find_element(By.XPATH, '//*[@id="q"]')  #동현유's 방법
    
    # 검색어 입력
    name = kw
    search.send_keys(name)
    
    # 엔터 입력
    search.submit()
    
    # 스크롤을 아래로 내려서 이미지를 더 로드
    for i in range(1, 9):
        driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
        time.sleep(10)
    
    # 결과 더보기 클릭 (버튼이 있는 경우에만)
    try:
        driver.find_element(By.XPATH, "//*[@class='mye4qd']").click()
        # 결과 더보기를 눌렀으니 마우스를 다시 아래로 내림
        for i in range(1, 9):
            driver.find_element(By.XPATH, "//body").send_keys(Keys.END) 
            time.sleep(10)
    except Exception as e:
        print("결과 더보기 버튼이 없습니다. 다음 단계로 넘어갑니다.")
    
    # 현재 페이지의 HTML 코드를 가져옴
    html = driver.page_source
    soup = BeautifulSoup(html, "lxml")
    
    # 이미지 URL들을 params 리스트에 담기
    params_g = []
    imgList = soup.find_all("a", class_="thumb_bf")
    #imageColl > div.cont_img > div > div.list_row > div:nth-child(4) > div.wrap_thumb > a > img
    
    for g_img in imgList:
        img_tag = g_img.find("img")  # g-img 태그 내의 img 태그를 찾음
        if img_tag:
            img_url = img_tag.get("src", img_tag.get("data-src"))
            params_g.append(img_url)
    
    # 결과 확인
    #print(params_g)
    
    # 이미지들을 로컬 디렉토리에 저장
    for idx, p in enumerate(params_g, 1):
        if p:
            urllib.request.urlretrieve(p, "c:\\data_image_daum\\" + str(idx) + ".jpg")
        else:
            print(f"이미지 {idx}는 다운로드할 수 없습니다.")



#19. 유튜브 댓글 수집
## 첫 번째 함수
#1. 필요한 패키지 임폴트
import  requests
import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
import  pandas  as  pd

#2. 키워드를 입력하면 해당 영상의 상세 url 을 가져오는 함수

def  get_url_youtube(keyword):
    titles = []  #유튜브 영상 제목을 담을 리스트
    urls = []    #키워드를 넣었을때 나오는 모든 영상들의 url 주소를 담기 위한 리스트

    # 입력한 키워드를 컴퓨터가 알아들을 수 있는 언어도 인코딩합니다.
    search_keyword_encode = requests.utils.quote(keyword)

    # 유튜브에서 해당 키워드의 영상 리스트를 찾을 수 있는 url 을 만들어서 url변수에 입력
    url = "https://www.youtube.com/results?search_query=" + search_keyword_encode

    # 크롬 로봇을 지정합니다.
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # 크롬 로봇이 url 을 직접 열게 합니다.
    driver.get(url)

    # 키워드로 받아온 영상 리스트 웹페이지의 처음부터 맨 마지막까지의 높이를 추출합니다
    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:  #   아래의 실행문이 무한히 반복될 수 있게 합니다.

        # 마우스 스크롤을 끝까지 내리게 합니다.
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

        time.sleep(3)

        # 마우스 스크롤을 내리는 데까지의 높이를 추출합니다
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

        # 지금의 높이가 웹페이지의 끝이라면
        if  new_page_height == last_page_height:
            break  # 무한 루프 종료해라 !

        # new_page_height 의 값을 last_page_height 에 할당
        last_page_height = new_page_height
    
    html_source = driver.page_source  # 페이지의 html 소소를 html_source 에 담습니다.
    driver.quit() # 브라우져를 닫습니다.

    # html 코드를 뷰티플 스프로 파싱합니다.
    soup = BeautifulSoup( html_source, 'lxml') 

    # 영상 제목과 상세 url 가져오기 
    datas = soup.select("a#video-title")
    for  i  in  datas:
        title =  i.get('title') 
        url = "https://www.youtube.com/" + i.get("href")
        if title:
            titles.append(title)
            urls.append(url)
    
    return  titles, urls

## 두 번째 함수
## 상세 url 을 넣고 html 을 받아오는 코드
def  youtube_page_html_source(urls):

    title, url = get_url_youtube(kewword)
    
    html_sources = [] # html 코드를 저장하기 위한 리스트를 생성합니다. 

    # 크롬 로봇을 지정합니다.
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    for  i  in  range(0, 20): # 전체 url 말고 2개의 url 만 가져옵니다. 
        
        # 크롬 로봇이 url 을 직접 열게 합니다.
        driver.get(url[i])
    
        # 키워드로 받아온 영상 리스트 웹페이지의 처음부터 맨 마지막까지의 높이를 추출합니다
        last_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    
        while True:  #   아래의 실행문이 무한히 반복될 수 있게 합니다.
    
            # 마우스 스크롤을 끝까지 내리게 합니다.
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
    
            time.sleep(3)
    
            # 마우스 스크롤을 내리는 데까지의 높이를 추출합니다
            new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
    
            # 지금의 높이가 웹페이지의 끝이라면
            if  new_page_height == last_page_height:
                break  # 무한 루프 종료해라 !
    
            # new_page_height 의 값을 last_page_height 에 할당
            last_page_height = new_page_height

        time.sleep(5)
        html_source = driver.page_source  # 페이지의 html 소소를 html_source 에 담습니다.
        time.sleep(5)

        html_sources.append(html_source)
        print('OK')

    driver.quit()
        
    return  html_sources 

## 세 번째 함수
## 글쓴이와 댓글 가져오는 함수

def get_comments(html_sources):
    # 상세 url 마다 담길 댓글의 데이터 프레임을 위한 리스트
    my_dataframes=[]
    cnt = 0 
    while  cnt <  len(html_sources):
        html = html_sources[cnt]
        cnt += 1
        soup = BeautifulSoup(html, 'lxml')

        # 글쓴이 가져오기 
        writer = soup.select('div#header-author > h3 > a > span')
        # 댓글 가져오기
        comments = soup.select('yt-attributed-string#content-text > span')

        # 글쓴이와 댓글의 길이가 다를 경우에 예외처리 
        min_len = min( len(writer), len(comments) )

        if  min_len == 0:
            continue

        #글쓴이 데이터를 writer2 리스트에 추가합니다. 
        writer2 = []
        for  i  in range(min_len):
            str_temp = str(writer[i].text).strip()  
            writer2.append(str_temp)

        # 댓글 데이터를 comments2 리스트에 추가합니다. 
        comments2 = []
        for  i  in range(min_len):
            str_temp2 = str(comments[i].text).strip()
            comments2.append(str_temp2)

        # 글쓴이와 댓글 데이터로 판다스 데이터 프레임을 생성
        pd_data = {"id" : writer2, "comment" : comments2 }
        pd_df = pd.DataFrame(pd_data)

        # 판다스 데이터 프레임을 my_dataframes 리스트에 append 시킴
        if not  pd_df.empty:
            my_dataframes.append(pd_df)

    # 글쓴이와 댓글을 가지고 판다스 데이터 프레임을 생성하기
    if my_dataframes:
        comments_df = pd.concat( my_dataframes, ignore_index=True)
    else:
        comments_df = pd.DataFrame(columns=['id','comment'])

    return  comments_df


## 네 번째 함수
def  scroll_youtube(keyword):
    title, url = get_url_youtube(keyword)
    kkk = youtube_page_html_source(url)
    my_data = get_comments(kkk)
    my_data.to_csv(f'c:\\data\\{keyword}_youtube.csv', index=False, encoding="utf-8")


#20. 중앙일보 2024기사 언급량 시각화
def relation_word_ja(keyword):    
    import pandas as pd
    import matplotlib.pyplot as plt
    from collections import Counter  #텍트스 데이터에서 단어를 카운트 하는 모듈
    
    # 텍스트 파일 열기 (with절을 써서 열면 파이썬이 알아서 파일을 닫아줍니다.)
    with open('c:\\data\\joongang.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    
    # 텍스트를 엔터로 분리합니다.
    lines = text.split('\n')
    #print(lines)
    
    # Counter 모듈을 객체화 합니다.
    date_counts = Counter()
    current_date = None
    
    # 2024년으로 시작하는 라인만 추출(기사 날짜와 제목을 추출)
    for line in lines:
        if line.startswith('2024-'):
            current_date=line[:10]   #날짜만 추출
        if current_date and keyword in line:   #2024년이면서 키워드를 포함한다면
            date_counts[current_date] += line.count(keyword)
    
    df = pd.DataFrame(list(date_counts.items()), columns=['date','count'])
    
    # 날짜를 datetime 형식으로 변환
    df['date'] = pd.to_datetime(df['date'])
    
    # 시각화
    import matplotlib.pyplot as plt
    from matplotlib import font_manager, rc 
    
    # 한글 폰트 설정
    plt.rcParams['font.family'] = 'Malgun Gothic'
    
    # 시각화 하기
    plt.figure(figsize=(10,6))  # 가로10, 세로6으로 그래프 사이즈 설정
    plt.plot(df['date'], df['count'], marker='o', color='b')
    plt.fill_between(df['date'],df['count'], color='gray', alpha=0.3 )
    
    # 피크값의 날짜를 가져오기
    peak_indices = df[df['count'] == df['count'].max()].index
    for i in peak_indices:
        plt.text(df['date'][i], df['count'][i] + 0.5, df['date'][i].strftime('%Y-%m-%d'),
                 color = 'red', fontsize=12)
    
    plt.title(f'날짜별 {keyword} 언급량')
    plt.xlabel('날짜')
    plt.ylabel('언급량')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.show()



# 21. related_wordcloud(데이터 위치, keyword) : 연관어 분석 시각화
def related_wordcloud(location, keyword):
    from collections import Counter  # 단어의 건수를 체크하기 위한 모듈
    from  konlpy.tag  import  Okt    # 한글 형태소 분석 모듈
    
    # 분석할 데이터를 불러옵니다.
    with  open(location, 'r', encoding='utf8') as f:
        text = f.read()
    
    # '봄옷' 과 연관이 높은 단어 추출
    related_words =[]
    okt = Okt()   
    for  sentence  in  text.split('.'):  # 문장단위로 분리
         if  keyword  in  sentence:  # '봄옷' 이 포함된 문장인 경우에만 단어 추출
             nouns = okt.nouns(sentence)  # 문장에서 명사 추출 
             for  i  in  nouns:
                 if len(i) > 1 : # 철자가 1개보다 큰 명사이면
                     related_words.append(i)
    
    #print(related_words) # 봄옷이라는 단어를 포함하는 문장에 들어간 단어들
    
    # related_words 에서 자주 나오는 단어들만 추출합니다. 
    
    if related_words:
        top_words = Counter(related_words).most_common(100)  # 100개 이상 출현된 단어 추출
        #print(top_words)
    else:
        print(f'{keyword}과 연관된 단어가 없습니다.')
    
    # top_words 리스트를 딕셔너리로 변환합니다. 
    dct = {'키워드' :[], 'cnt' :[] }
    
    for key, value  in top_words:
        #print(key, value)
        dct['키워드'].append(key)
        dct['cnt'].append(value)

    # 데이터 프레임으로 생성합니다.
    import pandas  as  pd
    df = pd.DataFrame(dct)
    df.columns =['title','count']

    # 워드 클라우드를 그리기 위해서 다시 딕셔너리 형태로 생성합니다.
    wc = df.set_index('title').to_dict()['count']
        
    # '봄옷' 과 연관성이 높은 단어들중에서 빈도수 높은 단어만 빨간색, 나머지는 검정색
    
    from wordcloud  import WordCloud
    import  matplotlib.pyplot as plt
    
    # 사용자 정의 색상함수
    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        if  word in top_10_words:
            return  'red'  # 빈도수 상위 10개 단어를 빨간색으로
        else:
            return 'black'
    
    # 2. 한글 안깨지게 하는 코드 
    from matplotlib import font_manager, rc
    font = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font)
    
    wordCloud = WordCloud(
    font_path = "c:/Windows/Fonts/malgun.ttf", # 폰트 지정
    width = 1000, # 워드 클라우드의 너비 지정
    height = 800, # 워드클라우드의 높이 지정
    max_font_size=100, # 가장 빈도수가 높은 단어의 폰트 사이즈 지정
    background_color = 'white' # 배경색 지정
    ).generate_from_frequencies(wc) # 워드 클라우드 빈도수 지정
    
    top_10_words = {word for word, count in Counter(wc).most_common(10) }
    
    plt.imshow(wordCloud.recolor(color_func=color_func), interpolation='bilinear')
    plt.axis('off')
    plt.show()






# 메시지를 하나의 변수에 담기
m = """
ann 모듈이 임폴트 되었습니다.
함수 목록
1. check_even_odd : 짝수와 홀수 판정 함수
2. analyze_sentiment : 감정 분석 함수
3. wrap : 문자열을 특정 문자로 감싸는 함수
4. plot_bar_graph : 막대 그래프 그리는 함수
5. plot_pie_graph : 원형 그래프 그리는 함수
6. hankook(키워드,페이지수) : 한국일보 데이터 수집
7. dongah(키워드,페이지수) : 동아일보 데이터 수집
8. ja(키워드,페이지수) : 중앙일보 데이터 수집
9. han(키워드,페이지수) : 한겨례 데이터 수집
10. km(키워드,페이지수) : 국민일보 데이터 수집
11. chosun(키워드, 페이지수) : 조선일보 데이터 수집
12. naver_blog2(키워드, 페이지수) : 네이버 블러그 데이터 수집
13. naver_shopping(키워드, 페이지수) : 네이버 쇼핑 데이터 수집
14. get_coupang_data(키워드, 페이지수) : 쿠팡 데이터 수집
15. download_image_bing(kw) : 빙 이미지 수집, c://data_image_bing에 저장됨
16. download_image_naver(kw) : 네이버 이미지 수집, c://data_image_naver에 저장됨
17. download_image_google(kw) : 구글 이미지 수집, c://data_image_google에 저장됨
18. download_image_daum(kw) : 구글 이미지 수집, c://data_image_daum에 저장됨
19. scroll_youtube(kw) : 유튜브 댓글 수집, c://data에 저장됨
20. relation_word_ja(kw) : 중앙일보 2024 언급량 시각화
21. related_wordcloud(데이터 위치, keyword) : 연관어 분석 시각화
"""

# 한 번에 출력
print(m)



