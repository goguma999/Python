##### pie graph
import matplotlib.pyplot as plt 

a = emp.groupby('job')['sal'].sum().reset_index()
a.columns = ['job','sumsal']

colors = plt.cm.Pastel1([0, 1, 2, 3, 4])  # 5개의 색상 선택

plt.figure(figsize=(4,4))
plt.pie(a['sumsal'], labels=a['job'], autopct='%.1f%%', colors=colors, explode=[0.2, 0.02, 0.02, 0.02, 0.02])
plt.show()

