#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[6]:


import random

a = np.zeros((2,3))

for row in range(2):
    for col in range(3):
        a[row,col] = random.randint(0,20)
a


# In[5]:


np.ones((3,3))


# In[7]:


np.ones((4,4))


# In[8]:


range(5)


# In[9]:


np.arange(5) #ndarray의 원소 범위


# In[10]:


np.arange(3,6)


# In[12]:


a = np.arange(3,10,2)
type(a)


# In[13]:


np.arange(1,10,0.8)


# In[14]:


a = np.arange(0,12)
a


# In[15]:


a.shape


# In[16]:


a.reshape(3,4) #3행 4열


# In[17]:


a.shape #원본은 그대로 냅두고 reshape은 새로 메몸리공간에 저장함.


# In[18]:


a.reshape(2,-1)


# In[19]:


# 0~9 구간을 7개 수를 일정한 간격으로 추출하려면?, linearly spaced values
np.linspace(0,10,7)


# In[20]:


np.linspace(0,10,5)


# In[21]:


np.random.random()


# In[22]:


np.random.random(3)


# In[23]:


np.random.random((3,3))  


# # 문제1,
# ndarray원소가 16개인 1차원 배열 생성<br>
# 4 * 4 변환

# In[24]:


#1답
np.random.random(16).reshape((4,4))


# In[25]:


a.data  #a라는 배열이 저장된 메모리 주소 출력


# In[29]:


b = a.reshape(-1,12)
b.data  #b의 메모리 주소 출력


# In[32]:


a1 = a.flatten()
a1


# In[33]:


a1.data


# In[36]:


a = np.arange(4)
a.data


# In[41]:


a +[1,1,1,1]


# In[37]:


a1 = a + 1
a1.data


# In[40]:


a, a1


# In[42]:


a


# In[43]:


a*2


# In[44]:


#Element-wise
a * np.sin(1.2)


# In[45]:


np.sin(a)


# In[46]:


np.sqrt(a) # universal function


# In[47]:


np.array([1,2,3]) * np.array([3,4,5])


# In[50]:


a = np.arange(6).reshape(2,-1) #reshape으로 2행으로 다시 정렬하여 새로운 메모리공간에 저장
a


# In[53]:


b = np.arange(6).reshape(3,-1)  #reshape으로 3행으로 다시 정렬하여 새로운 메모리공간에 저장
b


# In[54]:


np.dot(a,b) #dot product(내적, Innger Product)


# In[55]:


#dir(a)
a.dot(b)   # a, b


# In[56]:


a = np.arange(5)
a


# In[57]:


a + 1


# In[58]:


a


# In[60]:


a += 1
a


# In[61]:


a = np.arange(5)
a


# In[62]:


a.sum()


# In[66]:


a.max(), a.min(), a.mean(), a.std()  #mean:평균, std:표준편차


# In[67]:


#평균(m)
#분산(Variance): 각 원소와 평균의 차이의 제곱, 이들을 모두 합산, 그 값을 원소의 갯수로 나눔
#표준편차(std) :분산의 제곱근

m = np.arange(5)
m.mean(),m.var(),m.std()


# In[69]:


a


# In[71]:


np.sqrt(np.mean(abs(a-a.mean())**2)),np.std(a)


# In[72]:


a = np.arange(10,16)
a


# In[73]:


a[2],a[-1],a[0],a[-6]


# In[74]:


a[a.size-1]  #[a-1]과 같은 결과


# In[75]:


a[[1,2,3]]


# In[76]:


a = np.arange(1,17).reshape(4,-1)
a


# In[79]:


for e in a:
    for i in e:
        print(i,end=' ')


# In[ ]:


a[1][2], a[1,2],a[[1,2]]  #이 셋은 완전히 다른 결과


# In[84]:


#fancy indexing: 인덱서 안에 정수나 불리언 배열을 사용하여 배열의 값을 추출해내는 방법
ba = np.array([True,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False])
ba = ba.reshape(4,-1)
ba


# In[85]:


a[ba]


# In[87]:


a<2  #정수형 배열


# In[88]:


a[a<2]  #boolean 배열


# In[89]:


nums = [1,2,3,4,5]
nums[0:5]


# In[90]:


nums[::2]


# In[91]:


a[::]


# In[92]:


nums=list(range(5))
nums


# In[93]:


nums2= nums[:]
nums2


# In[94]:


nums2[0] = 5


# In[95]:


nums


# In[96]:


nums2


# In[97]:


a


# In[102]:


A = np.arange(10,19).reshape(3,-1)
A


# In[103]:


np.apply_along_axis(np.max, axis=1,arr=A)


# In[104]:


odd_sum = 0

for e in A.flat:
    if e%2==1: odd_sum += e
print(f'홀수의 합={odd_sum}')


# In[105]:


A[A%2==1]


# In[106]:


A[A%2==1].sum()


# In[108]:


A.data


# A1 = A.reshape(1,-1)
# A1.data

# In[112]:


A1.shape= (3,-1)
A1


# In[113]:


A1.data


# # View, Copies

# In[114]:


a = np.arange(1,5)
a


# In[115]:


b = a


# In[116]:


a[2] = 0


# In[117]:


b


# In[118]:


c = a[0:2]
c


# In[120]:


a[0] = 5
c


# In[2]:


#csv(Comma Separated Values)
#sample.csv
'''
id,value1,value2,value3
1,123,1.4,23
2,110,0.5,18
3,164,2.1,19
'''


# In[1]:


np.genfromtxt('sample.csv',delimiter=',',names=True)


# In[ ]:




