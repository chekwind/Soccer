#coding:utf8
'''
Created on 2014-2-26

@author: CC
'''

from firefly.dbentrust.dbpool import dbpool
from MySQLdb.cursors import DictCursor

ALL_NPCClubInfo={}

def getAllNPCClubInfo():
	'''获取所有NPC球队信息
	'''
	global ALL_NPCClubInfo
	sql="SELECT * FROM tb_npcclub"
	conn=dbpool.connection()
	cursor=conn.cursor(cursorclass=DictCursor)
	cursor.execute(sql)
	result=cursor.fetchall()
	cursor.close()
	conn.close()
	for npcclub in result:
		ALL_NPCClubInfo[npcclub['ID']]=npcclub

