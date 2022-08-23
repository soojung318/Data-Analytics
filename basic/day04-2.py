#!/usr/bin/env python
# coding: utf-8

# In[5]:


r = range(0,10)


# In[6]:


type(r)


# In[7]:


list(r)


# In[12]:


list(range(1,5))
list(range(1,5, 1))
list(range(1,5, 2))
list(range(5,0, -1))


# In[15]:


# 함수 작성, 리스트(원소는 정수 10)를 받아서 원소들의 합산 결과를 리턴하는 함수
def list_sum(nums, step=1):  # Parameter Variable(가인자)
    return sum(nums)

list_sum([1,2,3,4,5,6,7,8,9,10])  # Arguments(실인자)


# In[27]:


def add_num(a, b=0):
    c = a-b
    print(f"{a} - {b} = {c}")


# In[28]:


add_num(5, 3)      # Positional Arguments
add_num(b=3, a=5)  # Keyword Arguments
add_num(a=5, b=3)


# In[29]:


add_num(5)


# In[30]:


add_num(5, 3)


# ## Variable length arguments(가변인자)
# * positional argument에 적용되는 가변인자
# * keyword argument에 적용되는 가변인자

# In[32]:


# 이용자가 임의의 갯수의 정수를 어떤 함수에 전달하여 합산하고자 한다면...
# 그 아규먼트를 받아서 합산하는 함수는 파라미터 타입을 어떻게 선언해야 할까?
def sum_it(nums):
    print(sum(nums))
    
sum_it([1,2])
sum_it([1,2,3,4,5])


# In[34]:


def sum_it2(tp):
    print(sum(tp))


# In[35]:


sum_it2((1,2,3))
sum_it2((1,2,3,4,5))


# In[36]:


def sum_it3(*arg):  # Variable Length Positional Arguments
    print(sum(arg))


# In[37]:


sum_it3(1)
sum_it3(1,2,3)
sum_it3(1,2,3,4,5,6)


# In[49]:


def test(**keyargs):
    #print(type(keyargs))
    print(keyargs.get('sal'))


# In[50]:


# keyword argument 다수개를 파라미터로 전달할 때
test(num=11, name='Smith', dept=10)
test(num=12, name='Scott', sal=3000, loc='서울')


# # 파일 다루기

# In[ ]:


# 파일 : 메모리가 아닌 디스크에 저장된 데이터의 집합
# 텍스트 파일: 저장된 데이터를 읽어서 텍스트로 디코딩해야 볼 수 있다
# 이진 파일: 텍스트 파일이 아닌 그 이외의 데이터를 저장한 파일
# mode : r(읽기), w(쓰기), a(추가), x(생성), b(이진 데이터), t(텍스트), +
# mode 설정의 예 : r(rt), wb, r+


# In[52]:


# 파일 생성(w)
fstream = open('my_sample.txt', 'w', encoding='utf-8')
fstream.write('내가 만든 파일\n')
fstream.close()
print('파일 생성 성공')


# In[53]:


# 위에서 생성된 파일 읽어오기
fstream = open('my_sample.txt', encoding='utf-8')
data = fstream.read()
print(data)
fstream.close()


# In[60]:


# 절대경로를 이용한 파일 생성
fstream = open('D:/test/my_sample.txt', 'w', encoding='utf-8')
fstream.write('내가 만든 파일\n')
fstream.close()
print('파일 생성 성공')
# 'w'는 기존 파일이 존재하면 파일 내용을 지우고 새로 쓴다
# 파일의 기존 내용을 유지하면서 뒤에 내용을 추가하려면 'a' 모드를 사용한다
# 해당 이름의 파일이 없을 때만 생성하려면 'x'를 사용한다


# In[59]:


# 문자열 안의 \ 기능을 해제하려면 \\ 으로 하거나, 문자열 앞에 'r'을 추가한다
# 디렉토리 구분자를 '/' 로 해도 된다
fstream = open('D:\\test\\my_sample.txt', encoding='utf-8')
data = fstream.read()
print(data)
fstream.close()


# In[61]:


# 파일을 열 때 with 블럭을 사용하면 블럭이 모두 실행된 후에 자동으로 close()된다
with open('D:\\test\\my_sample.txt', encoding='utf-8') as fstream:
    data = fstream.read()
    print(data)


# In[63]:


# 현재 작업 디렉토리에 포함된 내용 목록 보기
import os
os.listdir()
os.path.isfile('day01.ipynb')


# In[65]:


import os
abspath = os.path.join("D:\\test", "testfile.txt")
abspath


# ## 시간 문자열을 파일명으로 사용하기

# In[66]:


import datetime
datetime.datetime.now()


# In[67]:


from datetime import datetime
datetime.now()


# In[70]:


time_now = datetime.now()
time_now.strftime('%Y-%m-%d-%H-%M-%S-%f')


# In[78]:


# 현재 시간을 구해서 시간 문자열을 생성하고 그 문자열을 파일명으로 하여 파일 생성
# 파일 내용에는 연,월,일,시,분,초를 한 행에 한 항목씩 기록해보세요.
# 쓰기 작업을 마친 후에는 다시 해당 파일을 읽어서 화면에 표시해보세요.


# In[82]:


from datetime import datetime
dt_obj = datetime.now()
now_str = dt_obj.strftime('%Y-%m-%d-%H-%M-%S-%f')

with open(now_str, 'w', encoding='utf-8') as fstream:
    fstream.write(dt_obj.strftime('%Y') + '\n')
    fstream.write(dt_obj.strftime('%m') + '\n')
    fstream.write(dt_obj.strftime('%d') + '\n')
    fstream.write(dt_obj.strftime('%H') + '\n')
    fstream.write(dt_obj.strftime('%M') + '\n')
    fstream.write(dt_obj.strftime('%S') + '\n')

print('파일 생성 및 쓰기 완료')

with open(now_str, encoding='utf-8') as fstream:
    print(fstream.read())


# In[77]:


# 지정된 파일이 없는 경우에만 파일 생성하기
try:
    with open('sample.txt', 'x', encoding='utf-8') as fstream:
        print('파일을 새로 생성함')
except FileExistsError as fe:
    print('기존 파일이 있습니다 '+ str(fe))
finally:
    print('작업 완료')


# In[ ]:


# 파일 복사
import shutil
shutil.copy('src_file', 'dst_file')


# In[ ]:


# 파일명 변경
import os
os.rename('old_name','new_name')


# In[ ]:


# 파일 삭제
import os
os.remove('file_name')


# In[ ]:


# 이진 파일을 읽어 오려면...
fstream = open('sample.jpg', 'rb')
data = fstream.read()
fstream.close()

fstream = open('sample_cpy.jpg', 'wb')
fstream.write(data)
fstream.close()

print('이미지 파일 복사 완료')


# In[95]:


fstream = open('D:/test/emp.txt', encoding='utf-8')
data = fstream.read()
print(data)
fstream.close()


# In[98]:


fin = open('sample.txt', encoding='utf-8')
dir(fin)


# In[94]:


# 텍스트 파일의 행 단위로 읽어오기
with open("D:/test/emp.txt", encoding='utf-8') as fin:
    while True:
        line = fin.readline()
        if line:   # 0, None, 빈 문자열은 False로 간주된다
            print(line.strip())
        else : 
            break
print('파일 읽기 완료')        


# In[103]:


# 파일 스트림은 루프에서 사용할 수 있나?
fin = open('D:/test/emp.txt', encoding='utf-8')
print( hasattr(fin, '__iter__') )  # True
fin.close()


# In[99]:


# 텍스트 파일의 행 단위로 읽어오기
with open("D:/test/emp.txt", encoding='utf-8') as fin:
    for line in fin:
        print(line.strip())
print('파일 읽기 완료') 


# In[105]:


# 특정 이름이 포함된 행을 검색하여 화면에 표시해보세요
with open("D:/test/emp.txt", encoding='utf-8') as fin:
    for line in fin:
        _,name,_,_ = line.split()
        if name=='suzan':
            print(line.strip())


# ## 텍스트 파일 특정 행 데이터 변경하기
# * 한행씩 읽어온다(디스크에서 메모리에 로드한다)
# * 변경 대상 행이라면 그 행 안의 전화번호만 변경하여 메모리에 로드한다
# * 텍스트 파일의 내용이 전체 로드되면 다시 디스크에 덮어쓰기한다

# In[112]:


emp_list = []
with open("D:/test/emp.txt", encoding='utf-8') as fin:
    for line in fin:
        num,name,phone,email = line.split()
        if name=='마동석':
            #print(line.strip())
            phone = "010-1111-3333"
            line = '{} {} {} {}'.format(num,name,phone,email)
        emp_list.append(line)
print('로드 완료')

with open("D:/test/emp.txt", "w", encoding="utf-8") as fout:
    fout.writelines(emp_list)
print('수정 완료')

print('수정 결과')
with open("D:/test/emp.txt", encoding="utf-8") as fin:
    print(fin.read())


# In[113]:


# 특정 행 찾아서 삭제하기
emp_list = []
with open("D:/test/emp.txt", encoding='utf-8') as fin:
    for line in fin:
        num,name,phone,email = line.split()
        if name=='blake':
            continue
        emp_list.append(line)
print('로드 완료')

with open("D:/test/emp2.txt", "w", encoding="utf-8") as fout:
    fout.writelines(emp_list)
print('수정 완료')

print('수정 결과')
with open("D:/test/emp2.txt", encoding="utf-8") as fin:
    print(fin.read())


# # 파일을 사용한 회원관리 프로그램 실습

# In[137]:


class Member:
    def __init__(self, str_line):
        num,name,phone,email = str_line.split()
        self.num = num
        self.name = name
        self.phone = phone
        self.email = email
        
    def __str__(self):
        return '{}\t{}\t{}\t{}'.format(self.num, self.name, self.phone, self.email)
    
    def to_str(self):
        return '{} {} {} {}'.format(self.num,self.name,self.phone,self.email)


# In[138]:


fpath = "D:/test/mem.txt"


# In[162]:


def add_mem():
    in_str = input('번호 이름 전화 메일:')
    num,name,phone,email = in_str.split()
    try:
        with open(fpath, 'x'):
            print('mem.txt 파일 생성됨')
    except FileExistsError:
        pass
    with open(fpath, 'a', encoding='utf-8')as fout:
        line = '{} {} {} {}'.format(num,name,phone,email)
        fout.write(line+'\n')
    print('회원정보 추가 성공')


# In[174]:


def list_mem():
    print('------------------------------------------------------')
    with open(fpath, encoding='utf-8')as fin:
        for line in fin:
            mem = Member(line)
            print(mem)


# In[164]:


def find_mem():
    print('------------------------------------------------------')
    mem_name = input('회원이름:')
    with open(fpath, encoding='utf-8')as fin:
        for line in fin:
            mem = Member(line)
            if mem.name==mem_name:
                print(mem)
                break


# In[165]:


def overwrite(mem_list):
    with open(fpath, 'w', encoding='utf-8') as fout:
        for mem in mem_list:
            fout.write(mem.to_str() + '\n')
        return True


# In[166]:


def update_mem():
    in_str = input('회원이름 새전화번호:')
    name,phone = in_str.split()
    mem_list = []
    with open(fpath, encoding='utf-8')as fin:
        for line in fin:
            mem = Member(line)
            if mem.name==name:
                mem.phone = phone
            mem_list.append(mem)
    if overwrite(mem_list):
        print('수정 성공')


# In[167]:


def delete_mem():
    name = input('삭제할 회원이름:')
    mem_list = []
    with open(fpath, encoding='utf-8')as fin:
        for line in fin:
            mem = Member(line)
            if mem.name==name:
                continue
            mem_list.append(mem)
    if overwrite(mem_list):
        print('삭제 성공')


# In[168]:


m_dic = {'a':'ADD', 's':'LIST', 'f':'FIND', 'u':'UPDATE','d':'DELETE', 'x':'EXIT'}
def menu():
    print('------------------------------------------------------')
    m = input('목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x):')
    return m_dic.get(m)


# In[176]:


go = True
while go:
    m = menu()
    if m=='ADD':
        add_mem()
    elif m=='LIST':
        list_mem()
    elif m=='FIND':
        find_mem()
    elif m=='UPDATE':
        update_mem()   
    elif m=='DELETE':
        delete_mem()     
    elif m=='EXIT':
        break
    else:
        print('메뉴입력 오류')
        
print('프로그램 종료')


# In[ ]:




