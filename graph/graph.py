
##### 원형 그래프 코드(matplotlib)
import matplotlib.pyplot as plt 

a = emp.groupby('job')['sal'].sum().reset_index()
a.columns = ['job','sumsal']

colors = plt.cm.Pastel1([0, 1, 2, 3, 4])  # 5개의 색상 선택

plt.figure(figsize=(4,4))
plt.pie(a['sumsal'], labels=a['job'], autopct='%.1f%%', colors=colors, explode=[0.2, 0.02, 0.02, 0.02, 0.02])
plt.show()



### 원형 그래프 함수(plotly)
#labels, values 리스트로 준비 
import plotly.graph_objects as go 
def plot_pie(labels, values) 
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])  
    fig.update_layout(
        title="원형 그래프 제목",
        template="plotly",  
        font=dict(   
            family="Arial, sans-serif",
            size=14,
            color="RebeccaPurple"
        )
    )
    fig.show()




##### 라인 그래프 코드
#x, y 리스트로 준비
import plotly.express as px
fig = px.line(x=x, y=y)
fig.show()



##### 라인 그래프 함수
#x, y 데이터 리스트로 준비 
import plotly.graph_objects as go
def plot_line(x,y):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name='Sentiment'))
    fig.update_layout(
        title="Sentiment Line Graph",
        xaxis_title="Index",
        yaxis_title="Sentiment",
        template="plotly_white")
    fig.show()



##### 막대 그래프 함수 
#x, y 데이터 리스트로 준비
import plotly.graph_objects as go 

def plot_bar(x, y):
    fig = go.Figure(data=[go.Bar(x=x, y=y)])
    fig.update_layout(
        title="막대 그래프 제목",
        xaxis_title="X 축",
        yaxis_title="Y 축",
        template="plotly",   #다른 템플릿 ~ "plotly_dark", "ggplot2"
        font = dict(
                family="Arial, sans-serif",
                size=14,
                color="RebeccaPurple" ) )
    fig.show()



