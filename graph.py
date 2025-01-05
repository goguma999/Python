
### pie1_plotly
#labels, values 리스트로 준비 
import plotly.graph_objects as go 
def plot_pie(labels, values): 
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])  
    fig.update_layout(
        #title="원형 그래프 제목",
        template="plotly",  
        font=dict(   
            family="Arial, sans-serif",
            size=14,
            color="RebeccaPurple"
        )
    )
    fig.show()



##### pie2_matplotlib
import matplotlib.pyplot as plt 
def matplotlib_pie(labels, values):
    plt.figure(figsize=(8, 5))
    colors = plt.cm.Pastel1([0,1,2,3,4])  # 5개의 색상 선택
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
    #plt.pie(explode = [0.2, 0.02, 0.02, 0.02, 0.02]로 조각 분리 가능)  
    plt.title("Matplotlib Pie Chart")
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()




##### line1_plotly
#x, y 데이터 리스트로 준비 
import plotly.graph_objects as go
def plot_line(x,y):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name='Sentiment'))
    fig.update_layout(
        #title="Sentiment Line Graph",
        xaxis_title="Index",
        yaxis_title="Sentiment",
        template="plotly_white")
    fig.show()



##### 라인 그래프 코드
#x, y 리스트로 준비
# import plotly.express as px
# fig = px.line(x=x, y=y)
# fig.show()



##### bar1_plotly
#x, y 데이터 리스트로 준비
import plotly.graph_objects as go 

def plot_bar(x, y):
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(
        #title="막대 그래프 제목",
        xaxis_title="X",
        yaxis_title="Y",
        template="plotly",   #다른 템플릿 ~ "plotly_dark", "ggplot2"
        font = dict(
                family="Arial, sans-serif",
                size=14,
                color="RebeccaPurple" ) )
    fig.show()



##### bar2_matplotlib
import matplotlib.pyplot as plt 
def matplotlib_bar(x, y):
    plt.figure(figsize=(8, 5))
    plt.bar(x, y, color='lightblue')
    #plt.title("Matplotlib Bar Graph")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.show()



##### amount_word(kw, file_path)
"""
텍스트 파일에서 키워드(kw)의 날짜별 언급량을 계산하고 시각화하는 함수
:param kw: 검색할 키워드 (
:param file_path: 분석할 텍스트 파일의 경로
"""
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib.dates as mdates
def amount_word(kw, file_path):
    # 텍스트 파일 열기
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"파일 '{file_path}'을 찾을 수 없습니다. 경로를 확인해 주세요.")
        return
    # 텍스트를 엔터로 분리합니다.
    lines = text.split('\n')

    # Counter 모듈을 객체화 합니다.
    date_counts = Counter()
    current_date = None

    # 2024년으로 시작하는 라인만 추출(기사 날짜와 제목을 추출)
    for line in lines:
        if line.startswith('2024.'):
            current_date = line[:10]
        if current_date and kw in line:  # 키워드(kw)가 포함된 경우
            date_counts[current_date] += line.count(kw)

    # DataFrame 생성
    df = pd.DataFrame(list(date_counts.items()), columns=['date', 'count'])
    if df.empty:
        print(f"'{kw}'에 대한 데이터가 없습니다.")
        return

    df['date'] = pd.to_datetime(df['date'], format='%Y.%m.%d')  
    df = df.sort_values(by='date')  

    # AppleGothic 폰트 적용
    plt.rcParams['font.family'] = 'AppleGothic'

    # 그래프 그리기
    plt.figure(figsize=(12, 6))
    plt.plot(df['date'], df['count'], marker='o', color='b', label=f"'{kw}' 언급량")
    plt.fill_between(df['date'], df['count'], color='gray', alpha=0.3)

    # x축을 월 단위로 표시
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # 월 단위 포맷
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # 월 단위 간격 설정

    # 피크값의 날짜를 가져오기
    peak_indices = df[df['count'] == df['count'].max()].index
    for i in peak_indices:
        plt.text(df['date'][i], df['count'][i] + 0.5, df['date'][i].strftime('%Y-%m-%d'),
                 color='red', fontsize=12)

    # 그래프 설정
    plt.title(f"날짜별 '{kw}' 언급량")
    plt.xlabel('날짜')
    plt.ylabel('언급량')
    plt.grid(True)
    plt.xticks(rotation=45)  
    plt.legend()
    plt.show()



##### related_wordcloud(데이터위치, keyword) : 연관어 분석 시각화
def related_wordcloud(location, keyword):
    from collections import Counter  # 단어의 건수를 체크하기 위한 모듈
    from  konlpy.tag  import  Okt    # 한글 형태소 분석 모듈
    
    # 분석할 데이터를 불러옵니다.
    with  open(location, 'r', encoding='utf8') as f:
        text = f.read()
    
    # 키워드(러닝)와 연관이 높은 단어 추출
    related_words =[]
    okt = Okt()   
    for  sentence  in  text.split('.'):  # 문장단위로 분리
         if  keyword  in  sentence:  # 키워드가 포함된 문장인 경우에만 단어 추출
             nouns = okt.nouns(sentence)  # 문장에서 명사 추출 
             for  i  in  nouns:
                 if len(i) > 1 : # 철자가 1개보다 큰 명사이면
                     related_words.append(i)
    
    #print(related_words) # 키워드 단어를 포함하는 문장에 들어간 단어들
    
    # related_words 에서 자주 나오는 단어들만 추출
    if related_words:
        top_words = Counter(related_words).most_common(100)  # 100개 이상 출현된 단어 추출
        #print(top_words)
    else:
        print(f'{keyword}과 연관된 단어가 없습니다.')
    
    # top_words 리스트를 딕셔너리로 변환
    dct = {'키워드' :[], 'cnt' :[] }
    
    for key, value  in top_words:
        #print(key, value)
        dct['키워드'].append(key)
        dct['cnt'].append(value)

    # 데이터 프레임으로 생성
    import pandas  as  pd
    df = pd.DataFrame(dct)
    df.columns =['title','count']

    # 워드 클라우드를 그리기 위해서 다시 딕셔너리 형태로 생성
    wc = df.set_index('title').to_dict()['count']

    # 키워드와 연관성이 높은 단어들중에서 빈도수 높은 단어만 빨간색, 나머지는 검정색
    from wordcloud  import WordCloud
    import  matplotlib.pyplot as plt
    
    # 사용자 정의 색상함수
    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        if  word in top_10_words:
            return  'red'  # 빈도수 상위 10개 단어를 빨간색으로
        else:
            return 'black'
    
    # 한글 안깨지게 하는 코드 
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
graph 모듈이 임폴트 되었습니다.
함수 목록
1. pie1_plotly 
2. pie2_matplotlib
3. line1_plotly
4. bar1_plotly
5. bar2_matplotlib
6. amount_word(kw, file_path)
7. related_wordcloud(데이터위치, keyword) : 연관어 분석 시각화
"""

# 한 번에 출력
print(m)

