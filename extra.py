import sqlite3
import sys

def add_user():

    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    date = 'SE25_jan'
    list = [1]

    #c.execute("alter table class add column "+ date)
    sql =  "UPDATE class SET "+date+" = 'A' WHERE Id is not NULL"
    c.execute(sql)

    for i in range(len(list)):
        sql =  "UPDATE class SET SE25_jan = 'P' WHERE Id =?"
        d = [list[i]]
        c.execute(sql,d)


    c.execute('SELECT * FROM class')

    for row in c:
        print row
    conn.commit()
    conn.close()



def add():

    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    Id = input("enter id :")
    name = raw_input("enter name : ")
    data = [(Id,name)]
    #c.execute('CREATE TABLE class(Id,name)')
    c.executemany("INSERT INTO class VALUES(?,?)",data)

    c.execute('SELECT * FROM class')

    for row in c:
        print row
    conn.commit()
    conn.close()

def delete_column():

    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()

    c.execute('SELECT * FROM class')

    for row in c:
        print row
    conn.commit()
    conn.close()

