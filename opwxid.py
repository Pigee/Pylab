#!/usr/bin/python3

#   使用说明  ./sxopid.py wxopid.txt result.txt
#   第一个参数读入文件  第二个参数输出文件
#   ！！！  最后一行clientid会少一个字符，，所以要手动加上  !!

import sys

wfile=open(sys.argv[2],mode='a')

sfile=open(sys.argv[1],mode='r')

wfile.write("create table opid ( opid varchar(50),clientid varchar(20),tag varchar(10));\n")
#  print(file)
for line in sfile:
   #   print(len(line))
   sline = line[0:len(line)-3]
   print(sline)
   sstr = sline.split('，')
   fele = sstr[0]
   i=0
   for ele in sstr[1:len(sstr)]:

       wfile.write('insert into opid values(\''+fele+'\','+ele+','+str(i)+');\n')
       # print('\''+fele+'\'')
       # print('\''+ele+'\'')
       # print(i)
       i=i+1

wfile.write("alter table opid add kh varchar(100);\n")
wfile.write("alter table opid add curkh varchar(100);\n")
wfile.write("alter table opid add hm varchar(100);\n")
wfile.write("alter table opid add addr varchar(200);\n")
wfile.write("update t1 set t1.kh = t2.meterno from opid t1,tmeter t2 where t1.clientid = t2.clientid;\n")
wfile.write("update t1 set t1.hm = t2.clientname,t1.addr = t2.address from opid t1,tclient t2 where t1.clientid = t2.id;\n")
wfile.write("update t1 set t1.curkh = t2.kh from opid t1,(select opid,kh from opid where tag = 0) t2 where t1.opid = t2.opid;\n")

# update opid set kh = concat('32',right(concat('000000000',kh),9));
# update opid set curkh = concat('32',right(concat('000000000',curkh),9));
# insert into w_1592793652199(id,create_date,update_date,head,nickname,kh,cur_kh,hm,userbase_addr,openid) select replace(uuid(),'-',''),now(),now(),'e','e',kh,curkh,hm,addr,id from opid


sfile.close()
wfile.close()
