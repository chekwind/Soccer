#coding:utf8
'''
Created on 2014-3-20

@author: CC
'''

from twisted.web import resource
from twisted.web.resource import ErrorPage
from memmode import register_admin
from firefly.server.globalobject import GlobalObject
from urls import getDayRecordList,getStatistics
import json

class OperaGamer(resource.Resource):

	def render(self,request):
		username=request.args['username'][0]
		opear_str=request.args['opear_str'][0]
		usermodedata=register_admin.getObjData(username)
		if not usermodedata:
			return "Account dose not exist!!!"
		pid=usermodedata.get('characterId')
		if not pid:
			return "Role does not exist!!!"
		gate_node=GlobalObject().remote.get('gate')
		gate_node.callRemote("opera_gamer",pid,opear_str)
		return "Success"

class DayRecored(resource.Resource):
	'''获取每日的纪录'''
	def render(self,request):
		index=int(request.args['index'][0])
		data=getDayRecordList(index)
		response=json.dumps(data)
		return response

class Statistics(resource.Resource):
	'''单服总数据统计'''
	def render(self,request):
		data=getStatistics()
		response=json.dumps(data)
		return response