#!/usr/bin/env python
# coding: utf-8

# # 파이썬 프로그래밍
# ## Interactive Interpreter

#      * 첫번째
#      * 두번째
#      * 세번째
# 

# In[1]:


print('Hello World')


# In[2]:


print(5)


# In[3]:


print("5")


# In[4]:


print(5+3)


# In[5]:


print()


# In[6]:


print("3+5")


# In[7]:


print("3+5=",8)


# In[8]:


print(1,2,3,"Hello","World!")


# In[9]:


print("3+5=",3+5)


# In[10]:


print("홍길동")


# In[11]:


print(1+2+3+4+5+6+7+8+9+10)


# In[12]:


print(2^5)


# In[13]:


2*2*2*2*2


# In[14]:


print(2*2*2*2*2)


# In[15]:


print(5-(3-1))


# In[16]:


print(10/2,10*2)


# In[17]:


val=30


# In[18]:


v1=25
v2=39
print(v1+v2)


# In[19]:


v1=25
v2=30
print(v1+v2)


# In[20]:


x=3*50
y=x+120
z=y/3
print(z)


# In[21]:


2*2*2


# In[22]:


x=2*2*2


# In[23]:


print(x)


# In[24]:


y=x/4
print(y)


# In[25]:


z=y*y


# In[26]:


print(z)


# In[27]:


x=100


# In[28]:


print(x)


# In[29]:


x=3.14
print(x)


# In[30]:


x="hi~"
print(x)


# In[31]:


x=3*50
x=x+120
x=x/3
print(x)


# In[32]:


x=2*2*2
print(x)


# In[33]:


x=x/4
print(x)


# In[34]:


x=x*x
print(x)


# In[35]:


x,y=121,797
print(x,y)


# In[36]:


x=y
print(x)


# In[37]:


print(x,y)


# In[38]:


x,y=y,x


# In[39]:


print(x,y)


# In[40]:


x,y=121,797
x,y=y,x
print(x,y)


# In[41]:


print()


# In[42]:


print("반갑습니다.")


# In[43]:


print("파이썬의 세계로 오신 것을 환영합니다.")


# In[44]:


def greet():
    print("반갑습니다.")
    print("파이썬의 세계로 오신것을 환영합니다")
    


# In[45]:


greet()


# In[46]:


greet()


# In[47]:


def greet():
print("방가방가")


# In[48]:


greet()


# In[49]:


def MH():
    print("1+2+3+4+5=",1+2+3+4+5)
    print("Simple is the best!")
    print("행복한 파이썬~")
    


# In[50]:


print MH()


# In[51]:


print MH()


# In[52]:


def MH():
    print("1+2+3+4+5=",1+2+3+4+5)
    print("Simple is the best!")
    print("행복한 파이썬~")


# In[53]:


def MH()


# In[54]:


MH()


# In[55]:


def greet2(name):
    print("반갑습니다.",name)
    print(name,"님은 파이썬 세계로 오셨습니다.")
    


# In[56]:


greet2("John")


# In[57]:


greet2("min kyung")


# In[58]:


greet2("Everyone")


# In[59]:


def adder(num1,num2):


# In[60]:


def adder(num1, num2):
    print("덧셈 결과:", num1 + nuum2)


# In[61]:


adder(10,5)


# In[62]:


def adder(num1, num2):
    print("덧셈 결과:", num1 + num2)


# In[63]:


adder(10,5)


# In[64]:


def test(str1):
    print("연습문제02-2")


# In[65]:


test()


# In[66]:


def test(str1):
    print("str1")
    print("str1")
    print("str1")


# In[67]:


test("연습문제02-2")


# In[68]:


def test(str1):
    print(str1)
    print(str1)
    print(str1)


# In[69]:


test


# In[70]:


test("연습문제02-2")


# In[71]:


def(num):
    if(num<0) print(num)
    if(num>0) print(-num)


# In[72]:


def calc(num):
    if(num<0) print(num)
    if(num>0) print(-num)
    


# In[73]:


def calc(num):
    if(num<0) 
        print(num)
    if(num>0) 
        print(-num)


# In[74]:


def opp_num(num):
    print(num*-1)+


# In[75]:


opp_num(-3)


# In[76]:


opp_num(3)


# In[77]:


def avr(n1,n2):
    print((n1+n2)/2)


# In[80]:


#d 두번 누르면 셀 하나씩 사라짐
#위쪽에 셀을 만들고 싶다면 원하는 셀 위치를 선택한 후 a키를 눌러.
#루프 돌리면  [ ]안에 *이 있다.


# In[81]:


a,b = 5,8
c=a+b
c


# In[82]:


import mymath as m
m.multiply(3,4)


# In[83]:


import mymath


# In[84]:


import mymath


# In[85]:


import mymath


# In[86]:


in_str = input('두 수(공백으로 구분) 입력:')
in_str


# In[90]:


in_str = input('두 수(공백으로 구분) 입력:')
res = in_str.split()
type(res)
res[0], res[1]
a, b = int(res[0]), int(res[1])
print('a+b=',a+b)
#list는 배열과 같은 개념


# In[91]:


#가감승제, 입력받은 두수로... 
str1 = input('두 수(공백으로 구분) 입력:')
res = str1.split()
type(res)
res[0], res[1]
a,b =int(res[0]),int(res[1])
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)


# In[99]:


#틀린코드
login= input('아이디,패스워드 입력: ')
(id, pw)= idPw.split()
if id=='scott'and pw=='1111':
    print('로그인 성공')
else :
    print('로그인 실패')


# In[111]:


go = True


# In[103]:


while go:
    pass
    login= input('아이디,패스워드 입력: ')
    (id, pw)= idPw.split()
    
    if id=='scott'and pw=='1111':
        print('로그인 성공')
        break;


# In[112]:


while go:
    login= input('아이디,패스워드 입력: ')
    (id, pw)= login.split()
    
    if id=='scott'and pw=='1111':
        print('로그인 성공')
        go = False
    else:
        print('로그인 실패')


# In[ ]:




range(0,5)
# In[114]:


range(0,5)


# In[113]:


# shift + tab : 문법 설명
for n in [1,3,5]:
    print(n,end=',')
    


# In[119]:


res = 0
for n in [1,2,3,4,5,6,7,8,9,10]:
    res = res + n # n += 1(n+1
print(res)


# In[120]:


import random
random.randint(0,5)


# In[121]:


res = 0
random_list =[]
random_list.append(5)
random_list


# In[122]:


#무작위 정수 10개를 가진 리스트 생성
#그 값들을 한 행으로 표시
num_list =[]
for n in range(10):
    num_list.append(random.randint(0,5))

for n in num_list:
    print(n, end=' ')


# In[123]:


str1 = '5.3'
str2 = '6.7'

n1 = float(str1)
n2 = float(str2)
print(n1 +n2)


# In[125]:


#실수나 정수 그 어떤 값도 문자열에서 숫자로 변환해야 한다면?
str1 = '3.14'
print(type(str1))

num = eval(str1)
print(type(num))


# In[126]:


eval('3+4')


# In[127]:


2++3


# In[128]:


2**3


# In[129]:


2**8 # 제곱


# In[130]:


1+2*3-7 #연산자 우선순위


# In[135]:


#리스트에 무작위 정수 10개(0~9)를 저장하고 그 중에서 가장 큰 수와 가장 작은 수를 표시해보세요.

num_list =[]
for n in range(10):
    num_list.append(random.randint(0,9))

for n in num_list:
        print(n, end=' ')
print(format(max(num_list),min(num_list)))
        


# In[138]:


import random

nums = [random.radint(0.9) for _ in range(10)] #List Comprehension

min = 10
max = 0

for n in nums:
    if n<min:
        min = n
    if n>max:
        max = n
print('min={}, max={}'.format(min,max))


# In[ ]:




