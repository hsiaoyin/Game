import sqlite3
import datetime
#import os
conn=sqlite3.connect('tempdb.sqlite')
cur=conn.cursor() #handle

try:
    cur.execute('''CREATE TABLE Users2 (ID Text, ResultMoney numeric, Insurance, text )''')
except:
    a=0
cur.execute('''insert into Users2 (ID,ResultMoney) values ("check",123)''')


conn.commit()



#with open("result.csv","rb") as f:
#    data=list(csv.reader(f))
#import collections
#counter=collections.defaultdict(int)
#for row in data:
    #counter[row[0]] +=1


#write
#f.writerow(list())
#check=str(list())
#f.write(check)
#f.close
#with open('result.csv','w',newline="",) as csvfile:


#    spamwriter=csv.writer(csvfile,delimiter=",")
#    spamwriter.writerow(['name','InitialSetup',check])
#    spamreader=csv.reader(csvfile,delimiter=",")
#    print(type(spamreader))
#    print(dir(type(spamreader)))
#    for row in spamreader:
#        print(",".join(row))
