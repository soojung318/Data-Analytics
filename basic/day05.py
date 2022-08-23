#!/usr/bin/env python
# coding: utf-8

# # 220818

# In[15]:


import pymysql


# In[157]:


conn = pymysql.connect(host='127.0.0.1',user='root',password='ezen',db='mydb',charset='utf8')  #mariaDB연결


# In[158]:


curs = conn.cursor()  #커서 열기


# In[118]:


curs.execute('SELECT * FROM emp')


# In[90]:


rows = curs.fetchall()  #fetch로부터 커서를 전부 가져옴
type(rows)  #rows의 정체는?  2차원 tuple


# In[91]:


rows


# In[92]:


for(empno,ename,hiredate,sal) in rows:
    print('{}\t{}\t{}\t{}'.format(empno,ename,hiredate,sal))


# In[152]:


curs.close()  #커서 닫기


# In[153]:


conn.close()  #mariaDB연결 종료


# In[13]:


#db,커서연결 함수
def get_conn():
    conn = pymysql.connect(host='127.0.0.1',user='root',password='ezen',db='mydb',charset='utf8')  #mariaDB연결
    return conn


# In[44]:


#db, 커서 종료 함수 ,사용안됌.
def close_conn():
    curs.close()
    conn.close()
    return 


# In[97]:


conn = get_conn()
curs = conn.cursor()
sql = "SELECT * FROM emp WHERE ename=%s"
curs.execute(sql,('alice'))

print('{}\t{}\t{}\t{}'.format(empno,ename,hiredate,sal))


curs.close()
conn.close()


# In[98]:


conn = get_conn()
curs = conn.cursor(pymysql.cursors.DictCursor)
curs.execute("SELECT * FROM emp")
rows = curs.fetchall() #하나를 가져옴

for row in rows:
    print(row['empno'],row['ename'],row['hiredate'],row['sal'])
curs.close()
conn.close()


# In[ ]:


with conn.cursor() as curs:
    curs.execute(sql,('a','b'))
    #커서를 close() 하지 않음
    


# In[110]:


#INSERT
#한 행 입력
sql = "INSERT INTO emp VALUES(%s,%s,%s,%s)" #4개의 파라미터를 가진 sql문
with conn.cursor() as curs:
    n = curs.execute(sql,(13,'alex','2022-01-14',3500))
    conn.commit()
    print('추가성공') if n>0 else print('추가실패')
#다수 개의 행 입력


# # 문제1, 추가
# 키보드에서 사번, 이름, 입사일, 급여액을 입력 받아서 emp 테이블에 한 행으로 입력하고 그 성공여부를 표시하세요.

# In[138]:


conn = get_conn()
curs = conn.cursor()

sql = "INSERT INTO emp VALUES(%s,%s,%s,%s)" #4개의 파라미터를 가진 sql문
with conn.cursor() as curs:
    info = input('사번, 이름, 입사일, 급여액 순으로 입력:')
    (empno,ename,hiredate,sal) = info.split()
    n = curs.execute(sql,(empno,ename,hiredate,sal))
    conn.commit()
    print('추가성공') if n>0 else print('추가실패')
    
curs.close()
conn.close()


# In[137]:


#쌤 답1
emp_str = input('사번 이름 입사일 급여액:')
empno, ename, hiredate, sal = emp_str.split()

sql = "INSERT INTO emp VALUES(%s,%s,%s,%s)"

with get_conn() as conn:
    with conn.cursor() as curs:
        n = curs.execute(sql,(int(empno),ename,hiredate,int(sal)))
        print('추가성공') if n>0 else print('추가실패')
    conn.commit()


# # 문제2, 수정
# 키보드에서 사번, 급여액을 입력받아서 해당 사원의 급여를 갱신하고 목록을 표시해보세요.

# In[156]:


#내 답2
sql = "UPDATE emp SET sal=%s WHERE empno=%s"
with conn.cursor() as curs:
    info = input('변경할 급여액, 사번 순으로 입력:')
    (sal,empno) = info.split()
    n = curs.execute(sql,(sal,empno))
    conn.commit()
    print('변경 성공') if n>0 else print('변경 실패')
    
curs.close()
conn.close()


# In[ ]:


#쌤 답2

emp_str = input('변경할 사원의 사번 급여액:')
empno, sal = emp_str.split()

sql = "UPDATE emp SET sal=%s WHERE empno=%s"

with get_conn() as conn:
    with conn.cursor() as curs:
        n = curs.execute(sql,(int(sal),int(empno)))
        print('변경성공') if n>0 else print('변경 실패')
    conn.commit()
    
curs.close()
conn.close()


# # 문제 3, 삭제
# 키보드에서 사원의 이름을 입력받아서 해당 사원의 정보를 삭제하고 목록을 표시해보세요.

# In[159]:


sql = "DELETE FROM emp WHERE empno=%s"
with conn.cursor() as curs:
    info = input('삭제할 사번 입력:')
    (empno) = info.split()
    n = curs.execute(sql,(empno))
    conn.commit()
    print('삭제 성공') if n>0 else print('삭제 실패')
    
curs.close()
conn.close()


# In[ ]:


#썜답3

ename = input('삭제할 사원의 이름:')
sql = "DELETE FROM emp WHERE ename=%s"

with get_conn() as conn:
    with conn.cursor() as curs:
        n = curs.execute(sql,(ename.strip(),))
        print('삭제성공') if n>0 else print('삭제실패')
    conn.commit()


# # 판다스, 빅데이터
# 파이썬, 표계산에 사용ㅇ like 엑셀

# In[160]:


#예제

import pandas as pd
def emp_list():
    conn = get_conn()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute("SELECT empno,ename,hiredate,sal FROM emp")
    rows = curs.fetchall()
    
    df = pd.DataFrame(rows)
    display(df)  #print(df)
    
    curs.close()
    conn.close()
emp_list()


# # 문제 4,
# class EmpDAO 클래스 선언: CRUD 작업용 메소드 정의 ,데이터 베이스 입출력<br>
# class EmpVO 클래스, 데이터베이스 정보<br>
# 기능: 목록(s),추가(a), 검색(f),수정(u), 삭제(d), 종료(x)<br>
# 수정: 이름을 이용하여 급여액 변경<br>
# <br>
# <strong>함수 목록</strong>
#   - find_by_empno()
#   - find_by_ename()
# <br>
# 

# In[21]:


class EmpVO:
    def __init__(self,str_line):
        empno,ename,hiredate,sal = str_line.split()
        self.empno = empno
        self.ename = ename
        self.hiredate = hiredate
        self.sal = sal
    
    def __str__(self):
        return '{}\t{}\t{}\t{}'.format(self.empno,self.ename,self.hiredate,self.sal)
    
    def to_str(self):
        return '{} {} {} {}'.format(self.empno, self.ename,self.hiredate.self.sal)


# In[28]:



import pandas as pd
class EmpDAO:
    
    
    
    def add_emp():
        conn = get_conn()
        sql = "INSERT INTO emp VALUES(%s,%s,%s,%s)" #4개의 파라미터를 가진 sql문
        with conn.cursor() as curs:
            info = input('사번, 이름, 입사일, 급여액 순으로 입력:')
            (empno,ename,hiredate,sal) = info.split()
            n = curs.execute(sql,(empno,ename,hiredate,sal))
            conn.commit()
            print('추가성공') if n>0 else print('추가실패')

    def list_emp():
        conn = get_conn()
        curs = conn.cursor(pymysql.cursors.DictCursor)
        curs.execute("SELECT empno,ename,hiredate,sal FROM emp")
        rows = curs.fetchall()

        df = pd.DataFrame(rows)
        display(df)  #print(df)
        
    def find_emp():
        conn = get_conn()
        curs = conn.cursor()
        
        sql = "SELECT * FROM emp WHERE ename=%s"
        with conn.cursor() as curs:
            info = input('검색할 이름 입력:')
            (ename) = info.split()
            n = curs.execute(sql,(ename))
            conn.commit()
            print('검색 성공') if n>0 else print('검색 실패')
        
        print('{}\t{}\t{}\t{}'.format(EmpVO.empno,EmpVO.ename,EmpVO.hiredate,EmpVO.sal))

    def update_emp():
        conn = get_conn()
        curs = conn.cursor()
        sql = "UPDATE emp SET sal=%s WHERE empno=%s"
        with conn.cursor() as curs:
            info = input('변경할 급여액, 사번 순으로 입력:')
            (sal,empno) = info.split()
            n = curs.execute(sql,(sal,empno))
            conn.commit()
            print('변경 성공') if n>0 else print('변경 실패')

    def delete_emp():
        conn = get_conn()
        curs = conn.cursor()
        sql = "DELETE FROM emp WHERE empno=%s"
        with conn.cursor() as curs:
            info = input('삭제할 사번 입력:')
            (empno) = info.split()
            n = curs.execute(sql,(empno))
            conn.commit()
            print('삭제 성공') if n>0 else print('삭제 실패')


# In[29]:


m_dic = {'a':'ADD','s':'LIST','f':'FIND','u':'UPDATE','d':'DELETE','x':'EXIT'}
def menu():
    print('--------------------------------------------------------------------')
    m = input('추가(a),목록(s),검색(f),수정(u),삭제(d),종료(x):')
    return m_dic.get(m)


# In[30]:


go = True
while go:
    m = menu()
    if m == 'ADD':
        EmpDAO.add_emp()
    elif m =='LIST':
        EmpDAO.list_emp()
    elif m =='FIND':
        EmpDAO.find_emp()
    elif m =='UPDATE':
        EmpDAO.update_emp()
    elif m == 'DELETE':
        EmpDAO.delete_emp()
    elif m=='EXIT':
        break
    else:
        print('메뉴입력 오류')
print('프로그램 종료')


# # Thread
# 한 프로세스 안에서 동시에 실행되는 코드(로직,함수)

# In[41]:


import time
from datetime import datetime

num = 0
cnt = 0
while True:
    num += 1
    print(f'num={num}')
    time.sleep(0.30)
    if num==10:
        break

while True:
    print(datetime.now())
    time.sleep(0.30)
    cnt += 1
    if cnt==10:
        break
print('루프종료')


# 
