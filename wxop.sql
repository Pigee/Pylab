
create table (wxid varchar(100) ,clid int,sn int);
alter table opid add kh varchar(30);
alter table opid add cur_kh varchar(30);

alter table opid add name varchar(200);
alter table opid add addr varchar(200);

update t1 set t1.kh = t2.meterno,t1.name = t2.paymentpeople,t1.addr = t2.Meteraddress
from opid t1,tmeter t2
 where t1.clid = t2.clientid;

update t1 set t1.cur_kh = t2.kh from opid t1,(select kh,wxid from opid where sn = 0) t2 where t1.wxid = t2.wxid;

############

update opid set kh = concat('32',right(concat('00000000',kh),9));
update opid set cur_kh = concat('32',right(concat('00000000',cur_kh),9));

insert into w_1592793652199(id,create_date,update_date,head,nickname,kh,cur_kh,hm,userbase_addr,openid)
select replace(uuid(),'-',''),now(),now(),'e','e',kh,cur_kh,name,addr,wxid from opid;
