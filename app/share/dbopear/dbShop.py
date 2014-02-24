#coding:utf8
'''
Created on 2014-2-24

@author: CC
'''
from firefly.dbentrust.dbpool import dbpool

def getShopInfo(shoptype):
	sql="select * from tb_shop where id =%d"%(shoptype)
	conn=dbpool.connection()
	cursor=conn.cursor(cursorclass=DictCursor)
	cursor.execute(sql)
	result=cursor.fetchone()
	cursor.close()
	conn.close()
	return result