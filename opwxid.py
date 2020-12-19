#!/usr/bin/python3

#   使用说明  ./sxopid.py wxopid.txt result.txt
#   第一个参数读入文件  第二个参数输出文件
#   ！！！  最后一行clientid会少一个字符，，所以要手动加上  !!

import sys

wfile=open(sys.argv[2],mode='a')

sfile=open(sys.argv[1],mode='r')
#  print(file)
for line in sfile:
   #   print(len(line))
   sline = line[0:len(line)-3]
   print(sline)
   sstr = sline.split(',')
   fele = sstr[0]
   i=0
   for ele in sstr[1:len(sstr)]:

       wfile.write('insert into opid values(\''+fele+'\','+ele+','+str(i)+');\n')
       # print('\''+fele+'\'')
       # print('\''+ele+'\'')
       # print(i)
       i=i+1

sfile.close()
wfile.close()
