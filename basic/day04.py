#!/usr/bin/env python
# coding: utf-8

# In[3]:


r = range(0,10)


# In[5]:


type(r)


# In[6]:


list(r)


# In[10]:


list(range(1,5))
list(range(1,5,1))
list(range(1,5,2))
list(range(5,0,-1))


# In[11]:


#함수 작성, 리스트(원소는 정수 10)를 받아서 원소들의 합산 결과를 리턴하는 함수
def list_sum(nums):  # Parameters(가인자)
    return sum(nums)

list_sum([1,2,3,4,5,6,7,8,9,10])  # Arguments(실인자)


# In[12]:


def add_num(a,b):
    c = a+b
    print(f"{a}+{b}={c}")


# In[13]:


add_num(10,5)


# In[15]:


def sub_num(a,b):
    c = a - b
    print(f"{a}-{b}={c}")


# In[17]:


sub_num(10,6)
sub_num(b=6,a=10)


# <string>Variable length arguments(가변인자)</board>
# 
# * positional argument에 적용되는 가변인자
# * keywoard argument에 적용되는 가변인자

# In[1]:


#이용자가 임의의 갯수의 정수를 어떤 함수에 전달하여 합산하고자 한다면...
#그 argument를 받아서 합산하는 함수는 파라미터 타입을 어떻게 선언해야 할까?
def sum_it(nums):
    print(sum(nums))
    
sum_it([1,2])
sum_it([1,2,3,4,5])


# In[2]:


def sum_it2(tp):
    print(sum(tp))


# In[3]:


sum_it2((1,2,3))
sum_it2((1,2,3,4,5))


# In[7]:


def sum_it3(*arg):  # *은 튜플, Variable Length Positional Arguments
    print(sum(arg))


# In[8]:


sum_it3(1,2,3)
sum_it3(1,2,3,4,5)


# In[30]:


def test(**keyargs): #keyargs의 type: dictionary
    #print(type(keyargs))
    #print(keyargs['name'])
    print(keyargs.get('sal')) #sal 이 없는 함수도 이상 없이 출력가능


# In[31]:


# keyword argument 다수개를 파라미터로 전달할 때
test(num=11, name='Smith', dept=10)
test(num=12, name='Scott',sal=3000,loc='서울')


# <h1><strong>파일 다루기</strong></h1>
# 
# * 파일 : 메모리가 아닌 디스크에 저장된 데이터의 집합
# * 텍스트 파일 : 저장된 데이터를 읽어서 텍스트로 디코딩해야 볼 수 있다
# * 이진 파일 : 텍스트 파일이 아닌 그 이외의 데이터를 저장한 파일
# * mode :r(읽기), w(쓰기), a(추가), x(생성),b(이진 데이터), t(텍스트), +
# * mode 설정의 예 : r(rt), wb(파일에 쓸 건지) ,r+

# In[34]:


# 파일 생성(w)
fstream = open('my_sample.txt','w',encoding='utf-8')
fstream.write('내가 만든 파일\n')
fstream.close()
print('파일 생성 성공')


# In[36]:


#위에서 생성된 파일 읽어오기
fstream = open('my_sample.txt',encoding='utf-8')
data = fstream.read()
print(data)
fstream.close()


# In[59]:


#절대 경로를 이용한 파일 생성
fstream = open('D:/test/my_sample.txt','w',encoding='utf-8')
fstream.write('내가 만든 파일\n')
fstream.close()

print('파일 생성 성공')

# 'w'는 기존 파일이 존재하면 파일 내용을 지우고 새로 쓴다.
# 파일의 기존 내용을 유지하면서 뒤에 내용을 추가하려면 'a'모드를 사용한다.
# 해당 이름의 파일이 없을 때만 생성하려면 'x'모드를 사용한다.


# In[60]:


#현재 경로
import os

currentpath = os.getcwd()
print(currentpath)


# In[61]:


#절대경로로 파일 읽어오기
fstream = open(r'D:\\test\\my_sample.txt',encoding='utf-8')
data = fstream.read()
print(data)
fstream.close()


# In[62]:


# 파일을 열 때 with 블럭을 사용하면 블럭이 모두 실행된 후에 자동으로 close()된다.
with open('D:\\test\\my_sample.txt',encoding='utf-8') as fstream:
    data = fstream.read()
    print(data)


# In[63]:


#현재 작업 디렉토리에 포함된 내용 목록 보기
import os
os.listdir()
os.path.isfile('day01.ipynb')


# In[66]:


import os
abspath = os.path.join("D:/test","testfile.txt")
abspath


# In[16]:


import datetime
datetime.datetime.now()


# In[17]:


from datetime import datetime
datetime.now()


# In[74]:


time_now = datetime.now()
time_now.strftime('%Y-%m-%d-%H-%M-%S-%f') # %f : 백만분의 1초(마이크로초)


# # 문제1
#  현재 시간을 구해서 시간 문자열을 생성하고 그 문자열을 파일명으로 하여 파일 생성하기.
#  파일 내용에는 연,월,일,시,분,초를 한 행에 한 항목씩 기록해보세요
#  쓰기 작업을 마친 후에는 다시 해당 파일을 읽어서 화면에 표시해보세요.

# In[31]:


from datetime import datetime
time_now = datetime.now()
date=time_now.strftime('%Y-%m-%d-%H-%M-%S')

y = time_now.strftime('%Y\n')
m = time_now.strftime('%m\n')
d = time_now.strftime('%d\n')
h = time_now.strftime('%H\n')
mm = time_now.strftime('%M\n')
s = time_now.strftime('%S\n')

# 파일 생성(w)
fstream = open('my_date.txt','w',encoding='utf-8')
fstream.write(y)
fstream.write(m)
fstream.write(d)
fstream.write(h)
fstream.write(mm)
fstream.write(s)
fstream.close()
print('파일 생성 성공')

with open('my_date.txt',encoding='utf-8') as fstream:
    data = fstream.read()
    print(data)


# In[13]:


# 지정된 파일이 없는 경우에만 파일 생성하기
try:
    with open('sample.txt','x',encoding='utf-8') as fstream:
        print('파일을 새로 생성함')
except FileExistsError as fe:   #FileExistsError 에러가 있을 때만 출력,
    #print(dir(fe))
    print('기존 파일이 있습니다'+str(fe)) #시스템상 등록된 에러도 같이 출력
finally:
    print('작업 완료')

    


# <h1><strong>문제2</strong></h1>
# 
# * 파일 복사

# In[ ]:


#파일 복사
import shutil
shutil.copy('src_file','dst_file')


# In[ ]:


#파일명 변경
import os
os.rename('old_name','new_name')


# In[ ]:


#파일 삭제
import os
os.remove('file_name')


# In[45]:


#이진 파일을 읽어 오려면...
fstream = open('sample.jpg','rb')
data = fstream.read()
fstream.close()

fstream = open('sample_copy.jpg','wb')
fstream.write(data)
fstream.close()

print('이미지 파일 복사 완료')


# In[91]:


fstream = open('D:/test/emp.txt',encoding='utf-8')
#dir(fstream)


# In[66]:


data = fstream.read()
print(data)
fstream.close()


# In[67]:


#특정 행만 읽어오려면....
with open("D:/test/emp.txt",encoding='utf-8') as fin:
    for i in data:
        line = fin.readline() #한행만 읽음
        print(line)


# In[72]:


with open("D:/test/emp.txt",encoding='utf-8') as fin:
    while True:
        line = fin.readline()
        if line:
            #ouput.write(line)
            print(line.strip())
        else:
            break
print('파일 읽기 완료')


# In[81]:


with open("D:/test/emp.txt",encoding='utf-8') as fin:
    for line in fin:
        print(line.strip())
        
print('파일 읽기 완료')


# # 문제 2
# * 특정 이름이 포함된 행을 검색하여 화면에 표시해보세요

# In[85]:


#문제 2
#특정 이름이 포함된 행을 검색하여 화면에 표시해보세요
# 답2 : 내가 푼 답
with open("D:/test/emp.txt",encoding='utf-8') as fin:
    for line in fin:
        if 'alice' in line:
            print(line.strip())
print('파일 읽기 완료')


# In[87]:


#답2 for사용x
with open("D:/test/emp.txt",encoding='utf-8') as fin:
    for line in fin:
        _,name,_,_ = line.split()
        if name=='alice':
            print(line.strip())
print('파일 읽기 완료')


# ## 문제 3, 텍스트 파일 특정 행 데이터 변경하기
# * 한 행씩 읽어온다(디스크에서 메모리에 로드한다)
# * 변경 대상 행이라면 그 행 안의 전화번호만 변경하여 메모리에 로드한다.
# * 텍스트 파일의 내용이 전체 로드되면 다시 디스크에 덮어쓰기한다.
# 
# 

# In[99]:


#내가푼답_오답
fstream_r = open("D:/test/emp.txt",'r',encoding='utf-8')
lines = fstream_r.readlines()
fstream_r.close()

fstream_w = open("D:/test/emp.txt",'w',encoding='utf-8')
in_name = input('변경 대상 이름:')
_,name,old_phone,_ = line.split()

for line in lines:
    fstream_w.write(line.replace(old_phone,new_phone))
fstream_w.close()

if name=='마동석':
    new_phone = input('변경할 전화번호 입력:')
    old_phone = fstream.write(new_phone)
    fstream.close()
    print(line.strip())
print('파일 변경 완료')


# In[103]:


#답3
emp_list = [] #메모리공간확보
with open("D:/test/emp.txt",encoding='utf-8') as fin:
    for line in fin:
        num,name,phone,email = line.split()
        if name =='마동석':
            print(line.strip())
            phone = "010-1111-1111"
            line = '{} {} {} {}'.format(num,name,phone,email)
        emp_list.append(line)
print('로드완료')

with open("D:/test/emp.txt","w",encoding='utf-8') as fout:
    fout.writelines(emp_list)
print('수정 완료')

print('수정 결과')
with open("D:/test/emp.txt",encoding='utf-8') as fin:
    print(fin.read())


# # 문제 4, 삭제

# In[104]:


emp_list = [] #메모리공간확보
with open("D:/test/emp.txt",encoding='utf-8') as fin:
    for line in fin:
        num,name,phone,email = line.split()
        if name =='마동석':
            continue
        emp_list.append(line)
print('로드완료')

with open("D:/test/emp.txt","w",encoding='utf-8') as fout:
    fout.writelines(emp_list)
print('삭제 완료')

print('삭제 결과')
with open("D:/test/emp.txt",encoding='utf-8') as fin:
    print(fin.read())


# # 문제 5, 회원관리 프로그램 실습(mem.txt)
# * 파일에 한 행 추가
#   - mode 'a'
#   - fout.write('xxxxxx\n')  #파일에 이어쓰기
#  <br><br>
# * 파일로부터 목록 읽어오기
#   - fin.read() :파일 내용 전체 문자열
#   - fin.readline() : 한 행 문자열 -> for문 사용가능
#   - fin.readlines() : 각 문자열
#  <br><br>
# * 파일로부터 한 행 읽어오기
#   - fin.readline() -> for()문 사용가능
#    <br><br>
# * 파일의 특정 행 수정하기
#   - fin.readline()
#   - 검색/로드/덮어쓰기
#      <br><br>
# * 파일의 특정 행 삭제하기
#   - fin.readline()
#   - 대상 행만 로드하지 않음
#   - 로드된 데이터를 파일에 덮어쓰기
#    <br><br>
# * Member class
#   - num, name, phone, email 속성
#    <br><br>
# * Menu
#   - 목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x)

# In[ ]:


class


# In[ ]:




