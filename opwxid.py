#!/usr/bin/python3

import sys

file=open(sys.argv[1],mode='r')
#  print(file)
for line in file:
   print(len(line))
   sline=line[0:len(line)-2]
   sstr =sline.split('，')
   fele = sstr[0]
   i=0
   for ele in sstr[1:len(sstr)]:
       print('insert into opid values('+'\''+fele+'\','+'\''+ele+'\','+str(i)+');')
       # print('\''+fele+'\'')
       # print('\''+ele+'\'')
       # print(i)
       i=i+1
