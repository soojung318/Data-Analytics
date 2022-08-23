#!/usr/bin/env python
# coding: utf-8

# # 220816 강의 INTRO
# 
# * 주식 자동매매 시스템
# * Object Detection
# 

# In[18]:


# 객체 안에 포함된 함수(메소드)
# 객체에 포함되지 않은 함수

max([1,2,3])
len('Hello')

str1 = 'Hello'
str2 = str1.lower()
tp = (str1, str2)  # Tuple 튜플
lst = [ str1,str2]   # List 리스트

tp[0]
lst[0] #인덱싱: 인덱스를 이용해서 값을 추출하는 것

lst[0] = 'World'
lst[0]

tp[0]='World'  # 에러.
tp[0]


#리스트와 튜플 공통점: 순서대로 데이터가 저장, 중복 가능.
#차이점: 튜플은 데이터 변경 불가능.


# In[22]:


"Hello".count('lo') #lo라는 문자 개수 출력
"Hello".count('l') #l라는 문자 개수 출력
str="Hello".upper()
str2 = str.lower()
tp = (str, str2)
tp 

(e1, e2) = tp #괄호 생략 가능
e1
e2


# In[24]:


#양쪽에 공백이 있는 경우
" World ".lstrip() # left strip의 약자; 왼쪽 공백 제거 후 출력
" World ".rstrip() # right strip의 약자; 오른쪽 공백 제거 후 출력
" World ".strip() # 공백 제거 후 출력


# In[26]:


"Hello World".replace(" ",",") #공백을 쉼표로 바꾸는 예제


# In[31]:


res = "Hello World".split()  #공백으로 문자열 분리 -> 리스트로 분리됨.
type(res)  #자료형 = list

s1,s2 = res
tp = (s1,s2) #리스트를 튜플로 전환
tp


# 문제 1
# uid = 'Smith'
# pwd = 'ABC111'
# 
# 키보드에서 아이디, 암호를 동시에 입력 받아서 위에 제시된 인증을 통과하면 '로그인 성공'아니면 '로그인 실패'를 표시한다. 키보드에서는 대소문자 구분없이 입력해도 정상적으로 인증될 수 있어야 한다.

# In[36]:


go = True
while go:
    login= input('아이디,패스워드 입력: ')
    (id, pw)= login.split()
    pw = pw.upper()
    id = id.upper()
    if id=='SCOTT'and pw=='ABC111':
        print('로그인 성공')
        go = False
    else:
        print('로그인 실패')


# In[38]:


#선생님 답
uid ='Smith'
pwd='ABC111'

while True:
    in_str = input('아이디 암호:')
    in_auth = in_str.split()
    if len(in_auth)<=1:
        continue
    id. ps= in_auth
    
    id = id.title().strip()
    ps = ps.upper().strip()
    
    print((id.ps))
    
    if id == uid and ps==pwd:
        print('로그인성공')
        break
    else:
        print('로그인실패')


# In[39]:


str="Hello World"
str.find('rl')  #index 8
str.find('l')


# In[40]:


str.rfind('l')


# In[41]:


print('첫번째\n두번째')


# In[42]:


print("첫번째 ' ' 두번째")


# In[55]:


lst =[3,4,5,6,7]
lst


# In[56]:


lst.append(8)  #create
lst


# In[54]:


lst[5] = 9
lst


# In[57]:


dir(list)#
ret = lst.pop(5) #ret == return준말
print(f'{ret}를 삭제했습니다')


# In[58]:


lst


# In[59]:


# 함수, 메소드
del lst[0] #인덱스 0번 데이터 delete
lst


# In[60]:


#read
lst[0]


# In[66]:


lst =[3,4,5,6,7]
lst


# In[67]:


del lst[:2]
lst


# In[68]:


del lst[:] #데이터를 모두 지운다고 해서 객체주소공간이 지워지는 것은 아님.
lst


# In[69]:


#True/False
True,False,None


# 비교/논리 연산자

# In[72]:


type(1<2)
res = 1<2 and 4>3
type(res)
res


# 모듈 실행 형태(2가지 방법)
# 1. 주 프로그램에서 import,from 을 사용한다.
#    import mymod
#    mymod.myfunc()
#    from mymod import myfunc as f # mymod.py의 myfunc를 f로 변경
#    f()
# 2. 해당 모듈이 주 프로그램이 되어 실행되도록 한다.(콘솔에서 python mymod.py 실행)
# 
# if name == '_main_':
#     myfunc()
#     
# if
# else 
#  

# In[75]:


"123"+str(4)
s1 ="123"
s1.isdigit()
n = int(s1)
print(n+5)


# In[76]:


s2 ="123"
s2.isalpha()


# In[77]:


s2 = "Thanks"
s2.isalpha()


# In[79]:


s3=""
dir(s3)


# 문제2
# 키보드에서 전화번호를 입력받아서 010으로 시작되는지, 3자의 숫자인지 검사하고, 두번째, 세번째 번호 그룹이 4자인 숫자로만 되어있는지 검사해서 그 결과를 '유효한 전화번호','번호입력오류'로 표시한다

# In[1]:


#문제2
go = True
while go:
    phoneNum = input('전화번호 입력: ')
    (num1,num2,num3 )= phoneNum.split()
    
    if num1=='010'and num2.count(num2)==4 and num3.count(num3)==4:
        print('유효한 전화번호')
        go = False
    else:
        print('번호입력 오류')


# In[6]:


#답2
vaild = False

in_str = input('전화번호 입력:')
lst = in_str.split('-')

if len(lst[0])==3 and lst[0].isdigit():
    if len(lst[1]) ==4 and lst[1].isdigit():
        if len(lst[2])==4 and lst[2].isdigit():
            valid = True
print('유효한 번호') if valid else print('실패')


# In[7]:


if True:
    print('참')


# In[10]:


if 0:   #0,None은 거짓, 문자"0"은 참,문자열''은 거짓.
    print('참')  #파이썬은 0을 초과한 숫자는 모두 참.
else:
    print('거짓')


# 문제3
# 무한히 키보드 입력을 받아 들이는 기능 작성
# 키보드에서 입력 데이터를 화면에 표시하고 다시 입력을 받는다
# 만약에 이용자가 입력할 때 아무것도 입력하지 않고 엔터키만 치는 경우에는 프로그램을 종료한다.

# In[17]:


#문제3
go = True
while go:
    str1 = input('문자열입력: ')
    
    if str1 == '':
        print('프로그램종료')
        go = False
    if str1.count(str1) == 1:
        print(str1)


# In[13]:


#문제3기능테스트
str1 = input('문자열입력: ')
str1.count(str1)


# In[18]:


#답3
go = True

while go:
    in_str = input('메시지:')
    if in_str:print(in_str)
    else:break
        
print('프로그램 종료')


# ## list(순서o,중복o,값변경o), tupe(순서o,중복o,값변경x),set(중복x),dictionary(key,value)

# In[19]:


lst = [1,2,3,4,5,6,6,6]
lst


# In[20]:


tpl = (1,2,3,4,5,6,6,6)
tpl


# In[21]:


[1,2]+[3,4]


# In[22]:


(1,2)+(3,4)


# In[23]:


set1 = {1,2,3,4,5,6,6,6}
set1


# In[24]:


dic1= {'name':'Smith','num':11,'phone':'010-4544-8888'}
dic1


# In[28]:


#값 두개를 동시에 반환 가능하다. 
#정확하게는 값 두 개가 아니라, 하나의 튜플이 반환되는 것임.
def test():
    return 1,3
test()


# In[29]:


a,b = test()
a,b


# In[30]:


a


# In[31]:


b


# 문제4
# 1~9 무작위 수 5개를 중복 없이 추출하여 출력한다.
# set() 사용.

# In[36]:


#답4
import random

go = True
set1 = set()

while go:
    set1.add(random.randint(1,9))
    if len(set1)==5:
        break
print('5개 추출완료')
set1


# In[37]:


1 in [1,2,3] #1이 리스트 안에 있는가? T/F


# In[38]:


5 not in [1,2,3] #5가 리스트 안에 없으면 T


# In[39]:


'hello' in 'hello world'


# In[40]:


'hello' not in 'hello world'


# In[43]:


import radom


# 문제5
# set을 사용하지 않고 중복되지 않은 정수 7개 추출하기(1~10)

# In[45]:


#문제5
#from random import *
import random
go = True
nums = []

while go:
    n = random.radint(1,10)
    if n not in nums:
        nums.append(n)
        if len(nums)==7:
            break
sorted(nums)


# In[46]:


#답5
emps =[[11,'smith'],[12,'ward'],[13,'scott']]

for emp in emps:
    num,name = emp
    print('{}.{}'.format(num,name))


# In[51]:


dic1 = {'smith':[11,'smith',20],
        'ward':[12,'ward',10],
        'scoot':[13,'scott',30]
       } #dictionary
#dir(dic1)
dic1


# 문제6
# 딕셔너리에 저장된 목록 표시하기.
# 

# In[54]:


dic1 = {'smith':[11,'smith',20],
        'ward':[12,'ward',10],
        'scoot':[13,'scott',30]
       } #dictionary

for dic2 in dic1:
    num,name= dic2
    print('{}.{}'.format(num,name))


# In[56]:


#답6
klist = dic1.keys()
print(type(klist))
for name in klist:
    emp = dic1.get(name)
    num,name,dept = emp
    print('{}\t{}\t{}'.format(num,name,dept))


# In[63]:


#문제 7 (6번 변형.)
for item in dic1.items():
    k, v = item
    num,name,dept = v
    print('{}\t{}\t{}'.format(num,name,dept))


# In[64]:


dic2 = {'a':'smith','b':'scott'}
dic2['a']
dic2.get('a')


# In[66]:


dic2.get('c') #해당 키가 없더라도 오류는 발생하지 않음


# In[67]:


dic2['c'] = 'ward'
dic2


# In[68]:


dic2.get('c')


# In[69]:


dic2['c'] = 'king'  #update
dic2.get('c')
dic2['c']


# In[72]:


dir(dic2)
dic2.pop('a')


# In[73]:


dic2


# In[74]:


del dic2['b']
dic2


# 문제8
# 딕셔너리 crud 실습
# 프로그램 시작 시 다음 과 같은 목록(s)을 보여준다.
# 검색(f), 추가(a), 수정(u),삭제(d), 종료(x) 목록
# 키보드에서 아이디, 번호, 이름 항목을 입력 받아서 Emp 객체를 초기화 한다. 아이디를 키로 하고 Emp 객체를 value 로 하는 딕셔너리에 저장한다.

# In[80]:


#답8
class Emp:
    def __init__(self,uid,num,name):
        self.uid = uid
        self.num = num
        self.name = name
        
    def __str__(self):
        return '{}\t{}\t{}'.format(self.uid,self.num,self.name)


# In[81]:


emp_dic={}
m_dic ={'s':'LIST','f':'FIND','a':'ADD','u':'UPDATE','d':'DELETE','x':'EXIT'}

def menu():
    print('-------------------------------------------------')
    m = input('목록(s). 검색(f).추가(a).수정(u).삭제(d).종료(x):')
    return m_dic.get(m) #list 반환


# In[88]:


def add():
    in_str = input('아이디 번호 이름:')
    token = in_str.split()
    if len(token) != 3:
        print('입력오류')
        return
    uid,num,name = token #튜플
    emp_dic[uid] = Emp(uid,num,name) #uid라는 키에 Emp라는 객체를 넣음
    print('저장성공')


# In[83]:


def list():
    print('-------------------------------------------------')
    for key in emp_dic.keys():
        emp = emp_dic[key]
        print('{}\t{}\t{}'.format(emp.uid, emp.num,emp.name))


# In[84]:


def find():
    print('-------------------------------------------------')
    uid = input('검색할 사원 아이디:')
    found = emp_dic.get(uid)  #emp객체가 found 변수에 대입
    if found: #값이 있다면 true, false는 0,None일 경우에만.
        print(found)
    else:
        print('검색된 정보가 없습니다.')


# In[85]:


def update():
    print('-------------------------------------------------')
    in_str = input('수정할 아이디 번호 이름:')
    uid, num, name = in_str.split()
    found = emp_dic.get(uid)
    if found: # 수정사항이 발견되면 새로 입력된 번호와 이름을 변경
        found.num = num
        found.name = name
        print('수정 성공')
    else:
        print('수정 실패')
        


# In[86]:


def delete():
    print('-------------------------------------------------')
    uid = input('삭제할 아이디:')
    if emp_dic.pop(uid): #삭제 성공했다면,, pop()안에 반환기능 내제됨. null이면 삭제 실패
        print('삭제 성공')
    else:
        print('삭제 실패')


# In[ ]:


go = True
while go:
    m = menu()
    if m == 'LIST':
        list()
    elif m == 'FIND':
        find()
    elif m == 'ADD':
        add()
    elif m == 'UPDATE':
        update()
    elif m == 'DELETE':
        delete()
    elif m == 'EXIT':
        break
    else:
        print('메뉴 입력 오류')
print('프로그램 종료')


# In[ ]:




