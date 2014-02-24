#coding:utf8
'''
Created on 2014-2-8

@author: CC
'''

from app.game.gatenodeservice import remoteserviceHandle
import json
from app.game.appinterface import packageInfo

@remoteserviceHandle
def getItemInPackage_201(dynamicId,request_proto):
	'''获取角色的包裹信息'''
	argument=json.loads(request_proto)
	characterId=argument.get('characterId')
	response=packageInfo.GetPackageInfo(dynamicId,characterId)
	return json.dumps(response)
