##### pie 
import matplotlib.pyplot as plt 

a = emp.groupby('job')['sal'].sum().reset_index()
a.columns = ['job','sumsal']

colors = plt.cm.Pastel1([0, 1, 2, 3, 4])  # 5개의 색상 선택

plt.figure(figsize=(4,4))
plt.pie(a['sumsal'], labels=a['job'], autopct='%.1f%%', colors=colors, explode=[0.2, 0.02, 0.02, 0.02, 0.02])
plt.show()


##### line_express
#x_data, y_data 리스트로 준비
import plotly.express as px
fig = px.line(x=x_data, y=y_data)
fig.show()


##### line_graph_objects
#x_data, y_data 리스트로 준비
import plotly.graph_objects as go
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines+markers', name='Sentiment'))
fig.update_layout(
    title="Sentiment Line Graph",
    xaxis_title="Index",
    yaxis_title="Sentiment",
    template="plotly_white")
fig.show()



