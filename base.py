# random
import random
dice = [1,2,3,4,5,6]
print(random.choice(dice))


# random 2개 추출
product = [ '정상품', '불량품', '정상품', '정상품', '정상품', '불량품' ]
import numpy as np 
a = np.random.choice(product, size=2, replace=False)  #비복원 추출
print(a)


# 가로로 출력
for i in range(1,11):
    print(i, end = ' ')


# for loop ~ continue
for i in range(1,11): 
    if i == 5:
        continue # 뒤 남은 코드 하지마라 ! 바로 올라가라 ! 
    print(i)


# for loop ~ break 
for i in range(1,11):
    if i == 5:
        print('5를 만났습니다. 종료')
        break 
    print(i)


# float 계산
from decimal import Decimal
result = Decimal('43.2')-Decimal('43.1')
print(result)


##문자열(Immutable)
# count
# find, index 
a = '기상 후 1시간을 얼마나 의미 있게 보내느냐에 따라 그날 하루가 결정됩니다'
a.find('의미')   #없으면 -1
a.index('의미')  #없으면 에러


# split, join
b = '아무 것도 하지 않으면, 아무 일도 일어나지 않는다.'
c = b.split()     
d = ' '.join(c)   #c리스트의 요소들을 다시 문자열로 출력하는데 문자와 문자의 연결을 공백으로 하겠다. 


# strip
e = '보험 실효 개시일은, 보험 계약 이후 한달, 이후입니다. 한달! 입니다.'
e2 = e.split()
cnt = 0

for i in e2:     
    if i.strip(' 1234567890`''-=~!@#$%^&*()_+";:,.<>/?') in['한달', '효과']:
        cnt += 1
print(cnt)        


# f문자열 포매팅
f'{"hi":=^10}'    # '====hi====' : 가운데 정렬 & 공백채우기
f'{"hi":!<10}'    # 'hi!!!!!!!!' : 왼쪽 정렬 & 공백채우기
f'{y:0.4f}'       # '3.4213' : 소수점 4자리까지
f'{y:10.4f}'      # '    3.4213' : 소수점 4자리까지 표현하고 총 자릿수를 10으로 맞춤


# replace(x, y)
a = "Life is too short"
a.replace("Life", "Your leg")


##리스트 관련 함수
# sort
a = [1,4,3,2]
a.sort() 
a  #[1,2,3,4]

# reverse
a = ['a', 'c', 'b']
a.reverse()
a  #['b', 'c', 'a']

# index(x) 
a = [1,2,3]
a.index(3)   #2 

# insert(a,b) #리스트 a번째 위치에 b를 삽입 
a = [1,2,3]
a.insert(2,5)
a  #[1,2,5,3]  

# remove(x) #첫 번째로 나오는 x 삭제
a = [1,2,3,1,2,3]
a.remove(3)  
a  #[1,2,1,2,3] 

# pop(), pop(x) #맨 마지막 요소/x번째 요소를 리턴하고 삭제
a = [1,2,3]
a.pop(1)  #2
a  #[1,3]

# extend(x)  #x에는 리스트만 올 수 있음. 원래의 리스트에 x리스트의 요소소 추가 
a = [1,2,3]
a.extend([4,5])
a  #[1,2,3,4,5]


##딕셔너리 관련 함수
a = {'name':'pey', 'phone':'010-9999-1234', 'birth':'1118'}
a.keys()
a.values()
a.items()
a.clear()  #key:value 쌍 모두 삭제

a.get('name')  #'pey'
a.get('nokey') #None 
a['nokey']     #에러
a.get('nokey','foo') #'foo'  #찾으려는 Key가 없을 때 가져올 디폴트 값 설정

#in  #해당 Key가 딕셔너리 안에 있는지 조사하기
'name' in a  #True 


##집합 관련 함수
s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])

#교집합 
s1 & s2  #{4,5,6}
s1.intersection(s2)   #{4,5,6} 

#합집합
s1|s2
s1.union(s2)

#차집합
s1 - s2
s1.difference(s2) 

s1.add(4)  #값 1개 추가 
s1.update([리스트])   #값 여러개 추가 
s1.remove(x)  #특정 값 제거 


# while loop
x = 1
while x < 11:
    print(x, end=" ")
    x = x + 1 


# kwargs 
def print_kwargs(**kwargs):  #딕셔너리로 저장
    print(kwargs)

print_kwargs(name='foo', age=3)   #{'name':'foo','age':3} 


# 파일 열고 자동으로 닫기 with 
with open('c:\\data\\new.txt','w') as f:
    f.write('Life is too short to worry about stupid things.') 


