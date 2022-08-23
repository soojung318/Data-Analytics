#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Sample:
    
    def __init__(self, x, y): # Initializer(초기자), 인스턴스 변수 초기화
        self.x = x
        self.y = y
        print(f'x:{x}, y:{y}')
        
    def __hash__(self):
        print('__hash__()')
        return self.hash(self.x,self.y)
    
    def __eq__(self, other):
        print('__eq__()')
        return self.x==other.x and self.y==other.y
    
    def __str__(self):
        return 'x:{}, y:{}'.format(self.x, self.y)


# In[ ]:


s1 = Sample(1,2)  # 객체생성, 인스턴스 생성
s2 = Sample(3,4)


# In[ ]:


s1==s2


# In[ ]:


print(s1)
print(s2)


# In[ ]:


s1.__eq__(s2)


# In[ ]:


class Product:
    
    def __init__(self, num,name,price,year):
        self.num = num
        self.name = name
        self.price = price
        self.year = year

    def __str__(self):
        return '{}\t{}\t{}\t{}'.format(self.num, self.name, self.price, self.year)
        
    def printRow(self):
        print(self)


# In[ ]:


product11 = Product(11,'Galaxy Watch', 200000, 2021)
product12 = Product(12,'Sense Book', 1200000, 2022)
product13 = Product(13,'Shaomi Band', 50000, 2021)
product14 = Product(14,'DDR Memory', 10000, 2020)
product15 = Product(15,'IPTime 공유기', 70000, 2022)


# In[ ]:


products = [product11, product12,product13,product14,product15]


# In[ ]:


for p in products:
    p.printRow()


# In[ ]:


2**3
4/2
5/2
5//2
5%2


# In[ ]:


nums = [2,5,4,3,6,8]
nums[2]  # indexing

nums[len(nums)-1]

nums[-1]  # 8
nums[-2]  # 6


# In[ ]:


import random

nums = [random.randint(0,100) for _ in range(10)]
print(nums)

nums2 = [nums[-i] for i in range(1, 11)]
print(nums2)


# In[ ]:


nums =  [i for i in range(10)]
nums


# In[ ]:


nums[2:5]  # Slicing


# In[ ]:


nums[2:5] = [0]


# In[ ]:


nums


# In[ ]:


p1 = nums[2:5]
p1


# In[ ]:


p1[0] = [2,3,4]


# In[ ]:


p1


# In[ ]:


p1[0:0] = [2, 3, 4]
p1


# In[ ]:


nums =  [i for i in range(10)]
nums


# In[ ]:


nums[:10]


# In[ ]:


nums[5:10]


# In[ ]:


nums[5:]


# In[ ]:


nums =  [i for i in range(10)]
nums


# In[ ]:


nums[:] = [0]
nums


# In[ ]:


nums =  [i for i in range(10)]
nums


# In[ ]:


nums[:] = []
nums


# In[ ]:


nums =  [i for i in range(10)]
nums


# In[ ]:


nums[0:10:2]  #start : stop : step


# In[ ]:


a = [1,'a', 3.14, [0,2]]
a


# In[ ]:


[2,3] + [4,5]   # 두 리스트의 결합


# In[ ]:


str = "ab" + "c"
str


# In[ ]:


[1,2] * 3


# In[ ]:


"ab" * 3


# In[ ]:


num = [1,2,3,4,5]
num[2]


# In[ ]:


str = "Hello World"
str[6]


# In[ ]:


str[6:]


# In[ ]:


num


# In[ ]:


str


# In[ ]:


num[2] = 10  # 리스트의 원소 변경
num


# In[ ]:


str[6] = 'w'
str


# In[ ]:


reverse = [str[-i] for i in range(1, len(str)+1)]
reverse


# In[ ]:


# 리스트 원소를 문자열로 변환하기
num = ['a','4','5','6','7']
''.join(num)


# In[ ]:


alpha = chr(97)
alpha


# In[ ]:


chr(122)


# In[ ]:


ord('0')  # 48
ord('9')  # 57


# In[ ]:


import random

chr_list = [chr(97+i) for i in range(26)]        # 소문자 리스트
num_list = [str(i) for i in range(10)]           # 숫자를 문자열로 변환한 리스트
chrs = chr_list + num_list                       # 리스트 합치기
len(chrs)  # 36

''.join([chrs[random.randint(0, 36)] for _ in range(32)])


# In[ ]:


str(5)


# In[ ]:


len('Hello')
len([3,4,5,6])


# ## 6교시 시작

# In[ ]:


def get_list(cnt, start, end):
    return [random.randint(start, end+1) for _ in range(cnt)]


# In[ ]:


get_list(10, 2, 13)


# In[ ]:


list1 = [1,2,3,4,5]
list1[4] = 10
list1


# In[ ]:


list1.remove(10)
list1


# In[ ]:


min(list1)  # 1
max(list1)  # 4


# In[ ]:


list1 = []
list1.append('a')
list1.append(5)
list1


# In[ ]:


list1.extend(['c', 7])
list1


# In[ ]:


list1.clear()
list1


# In[ ]:


list1 = [3,4,5,6,7]
list1.insert(2, 100)
list1


# In[ ]:


list1
deleted = list1.pop(2)
print( '삭제된 값:{}, 삭제 후:{}'.format(deleted, list1))


# In[ ]:


len(list1)       # 총갯수
list1.count(5)   # 5의 총갯수


# In[ ]:


list1.index(6)


# * list.append()
# * list.extend(other list)
# * list.clear()
# * list.insert(위치, 값)
# * list.pop(위치)
# * list.remove(값) 
# * list.count(값)
# * list.index(값)

# list, Member 클래스를 이용한 CRUD
# * 프로그램 시작, 메뉴 표시 : 목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x)
# * 추가: Member속성(번호, 이름, 전화)
# * 검색 : 번호로 검색, 이름으로 검색 택일
# * 수정: 전화번호 수정

# In[14]:


class Member:
    
    def __init__(self, num, name, phone):
        self.num = num
        self.name = name
        self.phone = phone
        
    def __str__(self):
        return '{}\t{}\t{}'.format(self.num, self.name, self.phone)
    
    def __eq__(self, other):
        return self.num==other.num
    
    def __hash__(self):
        return hash(self.num)


# In[15]:


m_dic = {'s':'LIST', 'a':'ADD', 'f':'FIND', 'u':'UPDATE', 'd':'DELETE', 'x':'EXIT'}


# In[16]:


def menu():
    print('------------------------------------------------------------')
    m_input = input(' 메뉴 => 목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x):')
    return m_dic.get(m_input)


# In[17]:


def print_list():
    print('------------------------------------------------------------')
    for m in mem_list:
        print(m)


# In[18]:


def add_member():
    strMem = input('번호 이름 전화:')
    sNum,name,phone = strMem.split()
    mem_list.append( Member(sNum,name,phone))
    print('추가 성공')


# In[19]:


def find_by_num(sNum):
    for m in mem_list:
        if m.num==sNum:
            return m
    return None


# In[20]:


def find_by_name(name):
    for m in mem_list:
        if m.name==name:
            return m
    return None


# In[21]:


def find():
    print('------------------------------------------------------------')
    find_key = input('번호로 검색(i), 이름으로 검색(n):')
    mem = None
    if find_key=='i':
        sNum = input('번호:')
        mem = find_by_num(sNum)
    elif find_key=='n':
        name = input('이름:')
        mem = find_by_name(name)
    else:
        print('입력오류')
    return mem


# In[22]:


def update():
    sNum = input('수정할 회원번호:')
    mem = find_by_num(sNum)
    if mem is None:
        print('검색된 회원정보가 없음')
        return False
    else:
        phone = input('새 전화번호:')
        mem.phone = phone
        return True


# In[23]:


def delete():
    sNum = input('삭제할 회원번호:')
    mem = find_by_num(sNum)
    idx = mem_list.index(mem)
    deleted = mem_list.pop(idx)
    if deleted:
        print('삭제 성공')
    else:
        print('삭제 실패')


# In[24]:


mem_list = []
go = True
while go:
    m = menu()
    if m=='LIST':
        print_list()
    elif m=='ADD':
        add_member()
    elif m=='FIND':
        print(find())
    elif m=='UPDATE':
        update()
    elif m=='DELETE':
        delete()
    elif m=='EXIT':
        go = False
    else:
        print('메뉴 입력 오류')
print('프로그램 종료...')


# In[ ]:




