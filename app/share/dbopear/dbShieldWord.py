#coding:utf8
'''
Created on 2014-1-17

@author: CC
'''
from firefly.dbentrust.dbpool import dbpool

SHIELDWORD=[]

def getAll_ShieldWord():
	global SHIELDWORD
	sql="SELECT sword FROM tb_shieldword;"
	conn=dbpool.connection()
	cursor=conn.cursor()
	cursor.execute(sql)
	result=cursor.fetchall()
	cursor.close()
	conn.close()
	SHIELDWORD=result

def checkIllegalChar(chars):
	'''检查是否包含非法字符
	@param chars: str 源字符
	'''
	for word in SHIELDWORD:
		if chars.find(word[0])!=-1:
			return False
	return True

def replaceIllegalChar(chars):
	'''替换非法字符
	@param chars: str 源字符
	'''
	for word in SHIELDWORD:
		chars=chars.replace(word[0],'*'*len(word[0]))
	return chars