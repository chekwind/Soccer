#coding:utf8
'''
Created on 2014-3-20

@author: CC
'''

from MySQLdb.cursors import DictCursor
from gfirefly.dbentrust.dbpool import dbpool

def getIncomByData(onedata):
	'''获取每天的缴费情况'''
	sql="SELECT SUM(rmb) AS goal,COUNT(DISTINCT uid) AS cnt FROM tb_recharge WHERE DATE(rtime)=DATE('%s') and boo=1;"%onedata
	conn=dbpool.connection()
	cursor=conn.cursor(cursorclass=DictCursor)
	cursor.execute(sql)
	result=cursor.fetchone()
	cursor.close()
	conn.close()
	result['goal']=float(result.get('goal')) if result.get('goal') else 0
	return result

def getDayConsume(onedata):
	'''获取某天的消费情况'''
	sql="SELECT * FROM tb_bill WHERE DATE(recordDate)=DATE('%s');"%onedata
	conn=dbpool.connection()
	cursor=conn.cursor(cursorclass=DictCursor)
	cursor.execute(sql)
	result=cursor.fetchall()
	cursor.close()
	conn.close()
	info={}
	info['cons_goal']=sum([record['spendGold'] for record in result])
	info['user_cnt']=len(set([record['characterId'] for record in result]))
	return info

def getDayRecordList(index,limit=10):
	'''获取每日的纪录'''
	sql="SELECT * FROM tb_statistics ORDER BY recorddate DESC LIMIT %s,%s;"%((index-1)*limit,index*limit)
	conn=dbpool.connection()
	cursor=conn.cursor(cursorclass=DictCursor)
	cursor.execute(sql)
	result=cursor.fetchall()
	cursor.close()
	conn.close()
	recordlist=[]
	for daterecord in result:
		recorddate=daterecord['recorddate']
		IncomeInfo=getIncomByData(recorddate)
		info=daterecord
		info['f_arpu']=0 if not IncomeInfo['cnt'] else IncomeInfo['goal']/IncomeInfo['cnt']
		info['z_arpu']=0 if not info['createrole'] else IncomeInfo['goal']/info['createrole']
		info['pay_rate']=0 if not info['loginuser'] else IncomeInfo['cnt']*100/info['loginuser']
		info['r_rate']=0 if not info['createrole'] else info['loginuser']*100/info['createrole']
		info['recorddate']=str(info['recorddate'])
		info['pay_cnt']=IncomeInfo['cnt']
		info['pay_goal']=IncomeInfo['goal']
		info.update(getDayConsume(recorddate))
		recordlist.append(info)
	return recordlist

def getStatistics():
	'''获取单服总数据'''
	sql1="SELECT COUNT(id) FROM tb_register;"
	sql2="SELECT COUNT(id) FROM tb_character;"
	sql3="SELECT COUNT(DISTINCT uid) FROM tb_recharge WHERE boo=1;"
	sql4="SELECT SUM(rmb) FROM tb_recharge WHERE boo=1;"
	conn=dbpool.connection()
	cursor=conn.cursor()
	cursor.execute(sql1)
	result1=cursor.fetchone()[0]
	cursor.execute(sql2)
	result2=cursor.fetchone()[0]
	cursor.execute(sql3)
	result3=cursor.fetchone()[0]
	cursor.execute(sql4)
	result4=cursor.fetchone()[0]
	cursor.close()
	conn.close()
	return {'reg_cnt':0 if not result1 else result1,'role_cnt':0 if not result2 else result2,'fu_cnt':0 if not result3 else result3,'income':0.0 if not result4 else float(result4)}
