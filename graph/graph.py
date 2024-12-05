
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







