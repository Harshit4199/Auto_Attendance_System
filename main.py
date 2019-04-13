import database
import datasetcreator
import detector
import trainning
import datetime


print "press 1 to add student..."
print "press 2 to take attendance..."
number = input()

if number==1:
    Id = input("enter id :")
    name = raw_input("enter name : ")
    data = [(Id,name,0)]



    database.add_user(data)
    datasetcreator.create_data(name,Id)
    trainning.train()
elif number==2:
    subject = ['SE','WT','TOC','AJAVA']
    print ("select subject...")
    print "1 SOFTWARE ENGINEERING"
    print "2 WEB TECHNOLOGY"
    print "3 TOC"
    print "4 ADVANCED JAVA"
    sub = input()-1
    date = datetime.datetime.today().strftime('_%d_%b_%y')
    time = datetime.datetime.today().strftime("%H:%M")

    print subject[sub]
    print date
    print time

    column_name = subject[sub]+date
    database.update(column_name)
else:
    print "enter valid number !"
