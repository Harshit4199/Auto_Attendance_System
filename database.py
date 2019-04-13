import sqlite3
import sys
import detector

def add_user(data):
    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    #c.execute('DROP TABLE class')
    #c.execute('CREATE TABLE class(Id,name)')


    c.executemany('INSERT INTO class VALUES(?,?,?)',data)
    conn.commit()
    conn.close()

def update(column_name):

    conn = sqlite3.connect('attendance.db')
    c = conn.cursor()
    #
    # list = [1,2]
    list = detector.attendence()

    c.execute("alter table class add column "+ column_name)
    sql =  "UPDATE class SET "+column_name+" = 'A' WHERE Id is not NULL"
    c.execute(sql)

    for i in range(len(list)):
        sql =  "UPDATE class SET "+column_name+" = 'P' WHERE Id =?"
        d = [list[i]]
        c.execute(sql,d)


    c.execute('SELECT * FROM class')

    for row in c:
        print row
    conn.commit()
    conn.close()

