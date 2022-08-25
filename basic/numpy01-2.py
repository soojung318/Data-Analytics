#!/usr/bin/env python
# coding: utf-8

# ## 함수형 프로그래밍(Functional Programming)
# * map()    : 컬렉션 원소에 대해 특정 계산을 적용함
# * filter() : 컬렉션 원소에 대해 특정 원소만 필터링하여 새 집합 생성
# * reduce() : 컬렉션 원소에 대해 계산을 수행하여 한개의 스칼라 값을 생성
# * lambda   : 위의 함수에서 사용하는 첫번째 아규먼트인 함수(익명함수)

# In[ ]:


nums = [1,2,3,4,5]

def add(x): return x+1
list(map(add, nums))


# In[ ]:


def odd(x): return x%2==1
list(filter(odd, nums))


# In[ ]:


from functools import reduce

def sub(x,y): return x+y
reduce(sub, nums)


# In[ ]:


# lambda
list(map(lambda x : x+1, nums))


# In[ ]:





# In[ ]:


get_ipython().system('pip show numpy')


# In[ ]:


import numpy as np


# In[ ]:


# ndarray (다차원 배열)
a = np.array([1,2,3,4,5])
type(a)
a.dtype.name


# In[ ]:


nums = ['a', 2, 'b', 'c', True, 3.14]
nums
b = np.array(nums)
b.dtype.name


# In[ ]:


a = np.array([1,2,3,4,5])
a.size
a.ndim
a.shape


# In[ ]:


a = np.array([
                [1,2,3], 
                [4,5,6]
             ])
a.size
a.ndim
a.shape
a.itemsize
a.data


# In[ ]:


a = np.array((
                [1,2,3], 
                (4,5,6)
             ))
a


# In[ ]:


bool_array = np.array([True,False,False])
bool_array


# In[ ]:


float_array = np.array([1.2, 3.4, 2.71828])
float_array
float_array.dtype.name


# In[ ]:


complex_array = np.array([1+2j, 3+2j, 5+2j], dtype=complex)
complex_array


# In[ ]:


za = np.zeros((3,3))
za


# In[ ]:


import random

a = np.zeros((2,3))

for row in range(2):
    for col in range(3):
        a[row][col] = random.randint(0, 20)
a


# In[ ]:


import random
import numpy as np

a = np.zeros((2,3))

for row in range(2):
    for col in range(3):
        a[row,col] = random.randint(0, 20)
a


# In[ ]:


np.ones((3,3))


# In[ ]:


rg = range(5)  # range object 리턴
for _ in rg:
    print(_, end=",")
    
lst = list(rg)
type(lst)


# In[ ]:


np.arange(5)  # ndarray 의 원소 범위


# In[ ]:


np.arange(3, 6)


# In[ ]:


a = np.arange(3,10, 2)
type(a)


# In[ ]:


np.arange(1,10, 0.8)


# In[ ]:


a = np.arange(0,12)
a


# In[ ]:


a.shape


# In[ ]:


b = a.reshape(3,4)
b


# In[ ]:


b.shape


# In[ ]:


a.shape


# In[ ]:


a.reshape(2, -1)


# In[ ]:


# 0~9 구간을 7개 수를 일정한 간격으로 추출하려면?, linearly spaced values
np.linspace(0,10, 7)


# In[ ]:


np.linspace(0,10, 5)


# In[ ]:


np.linspace(0,10, 5, endpoint=True)


# In[ ]:


np.linspace(0,10, 5, endpoint=False)


# In[ ]:


np.random.random()


# In[ ]:


np.random.random(3)


# In[ ]:


np.random.random((3,3))


# In[ ]:


a = np.random.random(16).reshape((4,4))
a


# In[ ]:


a.data


# In[ ]:


a1 = a.flatten()
a1


# In[ ]:


a1.data


# In[ ]:


a.data   # <memory at 0x00000272A3063930>


# In[ ]:


b = a.reshape(-1, 16)
b.data  # <memory at 0x00000272A30635F0>


# In[ ]:


a = np.arange(4)
a.data


# In[ ]:


a1 = a + 1
a1.data


# In[ ]:


a + [1,1,1,1]


# In[ ]:


a, a1


# In[ ]:


b = a*2
b


# In[ ]:


# Element-wise 
a * np.sin(1.2)


# In[ ]:


np.sin(a)


# In[ ]:


np.sqrt(a)  # universal function


# In[ ]:


np.array([1,2,3]) * np.array([3,4,5])


# In[ ]:


a = np.arange(6).reshape(2,-1)
a


# In[ ]:


b = np.arange(6).reshape(3,-1)
b


# In[ ]:


np.dot(a,b)   # dot product(내적, Inner Product)


# In[ ]:


#dir(a)
a.dot(b)  # a.b


# In[ ]:


a = np.arange(5)
a


# In[ ]:


a + 1


# In[ ]:


a


# In[ ]:


a += 1
a


# In[ ]:


a -= 1
a


# In[ ]:


dir(a)


# In[ ]:


a = np.arange(5)
a


# In[ ]:


a.sum()


# In[ ]:


a.max(), a.min(), a.mean(), a.std(ddof=0)


# In[ ]:


np.std(a)


# In[ ]:


#``std = sqrt(mean(x))``, where
#``x = abs(a - a.mean())**2``


# In[ ]:


# 평균(mean)
# 분산(Variance) : 각원소와 평균의 차이의 제곱, 이들을 모두 합산, 그 값을 원소의 갯수로 나눔
# 표준편차(std)  : 분산의 제곱근


# In[ ]:


a


# In[ ]:


np.sqrt(np.mean((a-a.mean())**2)), np.std(a)


# In[ ]:


a = np.arange(10,16)
a


# In[ ]:


a[2], a[-1], a[0], a[-6]


# In[ ]:


a[a.size-1]


# In[ ]:


a[[1,2,3]]


# In[ ]:


a = np.arange(1, 17).reshape(4,-1)
a


# In[ ]:


for e in a:
    for i in e:
        print(i, end=' ')


# In[ ]:


a[1][2], a[1,2], a[[1,2]]


# In[ ]:


# fancy indexing : 인덱서 안에 정수나 불리언 배열을 사용하여 배열의 값을 추출해내는 방법
ba = np.array([True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False])
ba = ba.reshape(4,-1)
ba


# In[ ]:


a[ba]


# In[ ]:


a<2


# In[ ]:


a[a<2]


# In[ ]:


a[1,2]


# In[ ]:


a[[1,2]]


# In[ ]:


nums = [1,2,3,4,5]
nums[0:5]


# In[ ]:


nums[0:]


# In[ ]:


nums[:]


# In[ ]:


nums[::2]


# In[ ]:


nums[2]


# In[ ]:


a = np.arange(10, 16)
a


# In[ ]:


a[1:5]


# In[ ]:


a[1:5:2]


# In[ ]:


a.data  # <memory at 0x00000272A3082A00>
b = a[::]
b.data  # <memory at 0x00000272A3177340>


# In[ ]:


nums = list(range(5))
nums


# In[ ]:


nums2 = nums[:]
nums2


# In[ ]:


nums2[0] = 5
nums2


# In[ ]:


nums


# In[ ]:


a = np.arange(5)
a


# In[ ]:


b = a[:]   # 리스트에서는 슬라이싱 결과와 원본이 서로 다른 리스트가 된다. ndarray는 슬라이싱 결과도 원본참조
b


# In[ ]:


b[0] = 5
b


# In[ ]:


a


# In[ ]:


A = np.arange(10, 19).reshape(3,-1)
A


# In[ ]:


A[0, 1:]


# In[ ]:


A[0:2, 1:]


# In[ ]:


A[:,0]


# In[ ]:


A[::2, 1:]


# In[ ]:


A[[0,2], 1:]


# In[ ]:


for row in A:
    print(row)


# In[ ]:


for n in A.flat:
    print(n, end=' ')


# In[ ]:


for n in A.flatten():
    print(n, end=' ')


# In[ ]:


for n in A.ravel():
    print(n, end=' ')


# In[ ]:


np.apply_along_axis(np.max, axis=1, arr=A)


# In[ ]:


odd_sum = 0

for e in A.flat:
    if e%2==1: odd_sum += e
        
print(f'홀수의 합={odd_sum}')


# In[ ]:


A[A%2==1].sum()


# In[ ]:


A[A%2==1].sum()


# In[ ]:


A


# In[ ]:


A.data   # <memory at 0x00000272A31AF040>


# In[ ]:


A1 = A.reshape(1,-1)
A1.data  # <memory at 0x00000272A31AF110>


# In[ ]:


A1.shape = (3,-1)
A1


# In[ ]:


A1.data


# In[ ]:


A1.shape = (9,)
A1


# In[ ]:


A1.shape = (3,-1)
A1


# In[ ]:


A


# In[ ]:


A.transpose()


# In[ ]:


A


# In[ ]:


A = np.ones((3,3))
B = np.zeros((3,3))


# In[ ]:


np.vstack([A,B])


# In[ ]:


np.hstack([A,B])


# In[ ]:


np.column_stack([[1,2,3], [4,5,6], [7,8,9]])


# In[ ]:


np.row_stack([[1,2,3], [4,5,6], [7,8,9]])


# In[ ]:


A = np.arange(16).reshape(4,-1)
A


# In[ ]:


np.hsplit(A, 2)


# In[ ]:


(a1,a2) = np.hsplit(A, 2)


# In[ ]:


a1


# In[ ]:


np.vsplit(A, 2)


# In[ ]:


A


# In[ ]:


np.split(A, [1,3], axis=1)


# In[ ]:


np.split(A, [2,3], axis=0)


# In[ ]:


a = np.array([1,2,3,4])
a


# In[ ]:


b = a
b


# In[ ]:


b[2] = 0
b


# In[ ]:


a


# ## Views, Copies

# In[ ]:


a = np.arange(1,5)
a


# In[ ]:


b = a


# In[ ]:


a[2] = 0


# In[ ]:


b


# In[ ]:


c = a[0:2]
c


# In[ ]:


a[0] = 5
c


# In[ ]:


a, c


# In[ ]:


c[1] = 7
c


# In[ ]:


a


# In[ ]:


a = np.arange(1,5)
a


# In[ ]:


b = a.copy()


# In[ ]:


b[0] = 5
b


# In[ ]:


a


# In[ ]:


v2 = np.array([1,2]) * np.array([3,4])
v2


# In[ ]:


a


# In[ ]:


a * 2


# In[ ]:


a * [2,2,2,2]


# In[ ]:


a


# In[ ]:


np.save('saved_ndarray', a)    # .npy
print('파일에 저장성공')


# In[ ]:


fa = np.load('saved_ndarray.npy')
fa


# In[ ]:


# csv ( Comma Separated Values)
# sample.csv
'''
id,value1,value2,value3
1,123,1.4,23
2,110,0.5,18
3,164,2.1,19
'''


# In[ ]:


ta = np.genfromtxt('sample.csv', delimiter=',', names=True)


# In[ ]:


ta[0][1]


# In[ ]:


ta[0]


# In[ ]:


type(ta), ta.ndim, ta.shape


# In[ ]:


ta['id']


# In[ ]:


ta = np.genfromtxt('sample.csv', delimiter=',', names=True, dtype=float)
ta


# In[ ]:


ta.ndim, ta.shape, ta.size


# ## numpy 데이터 삭제

# In[ ]:


import numpy as np

arr = np.array([1, 2, 3, 4, 5])
arr = np.delete(arr, 2)
arr


# In[ ]:


arr = np.array(["Alice", "Bob", "Charlie", "David", "Eric"])
arr = np.delete(arr, [0, 1, 2])
print(arr)


# In[ ]:


arr = np.array([[1 ,2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
arr = np.delete(arr, 1, axis=1)
print(arr)


# In[ ]:


arr = np.array([[1 ,2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
arr = np.delete(arr, [0,3], axis=1)
print(arr)


# In[ ]:


arr = np.array([[1 ,2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
arr = np.delete(arr, 0, axis=0)
print(arr)


# In[ ]:


arr = np.array([[1 ,2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])
arr = np.delete(arr, [0, 2], axis=0)
print(arr)


# In[ ]:


arr = np.array([1, 1, 1, 1, 2, 3, 4])
arr = np.delete(arr, np.where(arr == 1))
print(arr)


# In[11]:


# 검색
import numpy as np
a = np.arange(10)
a


# In[12]:


idx = np.where(a==5)
print('{}의 위치={}'.format(5, idx))


# ## numpy CRUD 실습

# In[1]:


import numpy as np


# In[2]:


names = np.array(['scott','jone','lora','blake','andy'])
subjects = np.array(['Java','Spring','Python'])
stid = np.array([11,12,13,14,15])
scores = np.zeros((5,3))


# In[3]:


m_dic= {'s':'LIST', 'a':'ADD','f':'FIND','u':'UPDATE','d':'DELETE', 'x':'EXIT'}
def menu():
    print('================================================================')
    m = input('목록(s), 추가(a), 검색(번호로 검색, f), 수정(u), 삭제(d), 종료(x):')
    return m_dic.get(m)


# In[4]:


def add():
    sNum, name = input('번호 이름').split()
    num = int(sNum.strip())
    idx = np.where(stid==num)
    if names[idx]!=name:
        print('일치하는 번호와 이름이 없습니다')
    else:
        s1,s2,s3 = input('S1, S2, S3 과목 성적:').split()
        score1 = int(s1.strip())
        score2 = int(s2.strip())
        score3 = int(s3.strip())
        scores[idx] = [score1,score2,score3]
        np.save('scores', scores)
        print('성적입력 성공')


# In[5]:


def list():
    print('================================================================')
    # 컬럼명
    print('번호\t이름', end='')
    for s in subjects:
        print(f'\t{s}', end='')
    print()
    print('--------------------------------------')
    
    # 데이터
    global scores
    try:
        tmp = np.load('scores.npy')
        scores = tmp
    except IOError as ioe:
        pass
    for i in range(len(names)):
        print('{}\t{}\t'.format(stid[i],names[i]), end='')
        for s in scores[i]:
            print('{}\t'.format(s), end='')
        print()


# In[6]:


def print_by_index(idx):
    print('================================================================')
    # 컬럼명
    print('번호\t이름', end='')
    for s in subjects:
        print(f'\t{s}', end='')
    print()
    print('--------------------------------------')
    
    num = stid[idx]
    name = names[idx]
    print('{}\t{}\t'.format(num[0],name[0]), end='')
    st_score = scores[idx][0]
    for s in st_score:
        print(f'{s}\t', end='')
    print()


# In[7]:


def find():
    sNum = input('학생 번호:')
    num = int(sNum)
    idx = np.where(stid==num)
    print_by_index(idx)


# In[8]:


def update():
    tmp = input('학생번호:')
    st_num = int(tmp.strip())
    idx = np.where(stid==st_num)
    
    tmp = input('과목번호(0,1,2) 새 성적:')
    subject_idx, new_score = tmp.strip().split()
    scores[idx, int(subject_idx)] = int(new_score)
    np.save('scores', scores)
    print('--------> 성적 수정 성공')


# In[9]:


def delete():
    global stid
    global names
    global scores
    global subjects
    
    tmp = input('학생정보 삭제(0) 과목삭제(1):')
    axis = int(tmp)
    if axis==0:
        tmp = input('삭제할 학생번호:')
        st_num = int(tmp.strip())
        idx = np.where(stid==st_num)
        stid = np.delete(stid, idx)
        names = np.delete(names, idx)
        scores = np.delete(scores, idx, axis=0)
        print('-------------> 학생정보 삭제 성공')
    elif axis==1:
        tmp = input('삭제할 과목번호(0,1,2):')
        idx = int(tmp.strip())
        subjects = np.delete(subjects, idx)
        scores = np.delete(scores, idx, axis=1)
        print('-------------> 과목 삭제 성공')


# In[10]:


go = True
while go:
    m = menu()
    if m == 'LIST':
        list()
    elif m=='ADD':
        add()
    elif m=='FIND':
        find()
    elif m=='UPDATE':
        update()
    elif m=='DELETE':
        delete()
    elif m=='EXIT':
        go = False
    else:
        print('--------> 메뉴입력 오류')
        
print('--------> 프로그램 종료')


# In[ ]:




