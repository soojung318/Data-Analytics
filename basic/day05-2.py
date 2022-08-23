#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pymysql


# In[2]:


conn = pymysql.connect(host='127.0.0.1', user='root', password='ezen', db='mydb', charset='utf8')


# In[3]:


curs = conn.cursor()


# In[4]:


curs.execute('SELECT * FROM emp')


# In[5]:


rows = curs.fetchall()
type(rows)


# In[6]:


rows


# In[7]:


for(empno,ename,hiredate,sal) in rows:
    print('{}\t{}\t{}\t{}'.format(empno,ename,hiredate,sal))


# In[8]:


curs.close()


# In[9]:


conn.close()


# ## SQL 문장에 파라미터 설정
# * sql = "SELECT * FROM emp WHERE ename='%s'"
# * curs.execute(sql,('smith',))

# In[32]:


def get_conn():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='ezen', db='mydb', charset='utf8')
    return conn


# In[33]:


ename = input('사원이름:')


# In[34]:


ename


# In[41]:


conn = get_conn()
curs = conn.cursor()
curs.execute("SELECT * FROM emp WHERE ename=%s",(ename,))
row = curs.fetchone()
print(row)
empno, ename, hiredate, sal = row
print('{}\t{}\t{}\t{}'.format(empno,ename,hiredate,sal))
curs.close()
conn.close()


# In[36]:


(1+2)*(3+4)


# In[37]:


[5]


# In[40]:


(5,3)


# In[48]:


def show_all():
    conn = get_conn()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute("SELECT * FROM emp")
    rows = curs.fetchall()

    for row in rows:
        print('{}\t{}\t{}\t{}'.format(row['empno'],row['ename'],row['hiredate'],row['sal']))

    curs.close()
    conn.close()


# In[ ]:


with conn.cursor() as curs:
    curs.execute(sql, ('a','b'))
    # 커서를 close() 하지 않음


# In[ ]:


# INSERT
# 한행 입력
sql = "INSERT INTO emp VAUES(%s, %s, %s, %s)"
with conn.cursor() as curs:
    n = curs.execute(sql, (13,'james', '2022-01-14', 3500) )
    print('추가성공') if n>0 else print('추가실패')
conn.commit()
# 다수개의 행 입력


# In[51]:


emp_str = input('사번 이름 입사일 급여액:')
empno, ename, hiredate, sal = emp_str.split()

sql = "INSERT INTO emp VALUES(%s,%s,%s,%s)"

with get_conn() as conn:
    with conn.cursor() as curs:
        n = curs.execute(sql,(int(empno),ename,hiredate,int(sal)))
        print('추가 성공') if n>0 else print('추가 실패')
    conn.commit()


# In[52]:


show_all()


# In[54]:


emp_str = input('변경할 사원의 사번 급여액:')
empno, sal = emp_str.split()

sql = "UPDATE emp SET sal=%s WHERE empno=%s"

with get_conn() as conn:
    with conn.cursor() as curs:
        n = curs.execute(sql,(int(sal),int(empno)))
        print('변경 성공') if n>0 else print('변경 실패')
    conn.commit()

show_all()


# In[55]:


ename = input('삭제할 사원의 이름:')

sql = "DELETE FROM emp WHERE ename=%s"

with get_conn() as conn:
    with conn.cursor() as curs:
        n = curs.execute(sql,(ename.strip(),))
        print('삭제 성공') if n>0 else print('삭제 실패')
    conn.commit()

show_all()


# In[60]:


import pandas as pd
def emp_list():
    conn = get_conn()
    curs = conn.cursor(pymysql.cursors.DictCursor)
    curs.execute("SELECT empno,ename,hiredate,sal FROM emp")
    rows = curs.fetchall()

    df = pd.DataFrame(rows)
    display(df)
    #print(df)
    
    curs.close()
    conn.close()
    
emp_list()


# In[81]:


class EmpVO:
    def __init__(self, empno=0, ename='', hiredate='', sal=0):
        self.empno = empno
        self.ename = ename
        self.hiredate = hiredate
        self.sal = sal
    
    def __str__(self):
        return '{}\t{}\t{}\t{}'.format(self.empno,self.ename.self.hiredate,self.sal)
    


# In[82]:


class EmpDAO:
    
    def get_conn(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='ezen', db='mydb', charset='utf8')
        return conn
    
    def add_emp(self, emp):
        with self.get_conn() as conn:
            n = 0
            with conn.cursor() as curs:
                sql = "INSERT INTO emp VALUES(%s,%s,%s,%s)"
                n = curs.execute(sql, (emp.empno, emp.ename, emp.hiredate, emp.sal))
            conn.commit()
            return True if n>0 else False
        
    def get_list(self):
        with self.get_conn() as conn:
            with conn.cursor(pymysql.cursors.DictCursor) as curs:
                sql = "SELECT * FROM emp"
                curs.execute(sql)
                return curs.fetchall()
            
    def find_by_empno(self, empno):
        with self.get_conn() as conn:
            with conn.cursor(pymysql.cursors.DictCursor) as curs:
                sql = "SELECT * FROM emp WHERE empno=%s"
                curs.execute(sql, (empno,))
                return curs.fetchall()
            
    def find_by_ename(self, ename):
        with self.get_conn() as conn:
            with conn.cursor(pymysql.cursors.DictCursor) as curs:
                sql = "SELECT * FROM emp WHERE ename=%s"
                curs.execute(sql, (ename,))
                return curs.fetchall()
            
    def update_sal(self, emp):
        with self.get_conn() as conn:
            n = 0
            with conn.cursor(pymysql.cursors.DictCursor) as curs:
                sql = "UPDATE emp SET sal=%s WHERE ename=%s"
                n = curs.execute(sql, (emp.sal, emp.ename))
            conn.commit()
            return True if n>0 else False
            
    def delete_by_empno(self, empno):
        with self.get_conn() as conn:
            with conn.cursor(pymysql.cursors.DictCursor) as curs:
                sql = "DELETE FROM emp WHERE empno=%s"
                n = curs.execute(sql, (empno,))
            conn.commit()
            return True if n>0 else False


# In[83]:


m_dict = {'s':'LIST', 'a':'ADD','f':'FIND','u':'UPDATE','d':'DELETE','x':'EXIT'}
def menu():
    m = input('목록(s), 추가(a), 검색(f), 수정(u), 삭제(d), 종료(x):')
    return m_dict[m]


# In[84]:


import pandas as pd
def show_list(emp_list):
    df = pd.DataFrame(emp_list)
    display(df)


# In[85]:


import pandas as pd
def show_emp(emp):
    df = pd.DataFrame(emp)
    display(df)


# In[86]:


def add():
    in_str = input('사번 이름 입사일 급여액:')
    tp = in_str.split()
    if len(tp)<4:
        print('4개 항목을 모두 입력해주세요')
        return None
    empno,ename,hiredate,sal = tp
    return EmpVO(int(empno),ename,hiredate,int(sal))


# In[95]:


def update():
    in_str = input('수정할 사원 이름 급여액:')
    ename, sal = in_str.split()
    emp = EmpVO(ename=ename, sal=int(sal))
    dao = EmpDAO()
    return dao.update_sal(emp)


# In[96]:


def delete():
    in_str = input('삭제할 사원 번호:')
    dao = EmpDAO()
    return dao.delete_by_empno(int(in_str))


# In[99]:


dao = EmpDAO()
go = True

while go:
    m = menu()
    if m == 'LIST':
        show_list(dao.get_list())
    elif m=='ADD':
        emp = add()
        if dao.add_emp(emp):
            print('추가 성공')
        else:
            print('추가 실패')
    elif m=='FIND':
        empno = input('검색할 사원 번호:')
        show_emp(dao.find_by_empno(int(empno)))

    elif m=='UPDATE':
        if update():
            print('수정 성공')
        else:
            print('수정 실패')
    elif m=='DELETE':
        if delete():
            print('삭제 성공')
        else:
            print('삭제 실패')
    elif m=='EXIT':
        break
    else:
        print('메뉴 입력 오류')
print('프로그램 종료')


# In[ ]:




