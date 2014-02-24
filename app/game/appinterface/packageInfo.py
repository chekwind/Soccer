#coding:utf8
'''
Created on 2014-2-12

@author: CC
'''
from app.game.core.GamersManager import GamersManager

def GetPackageInfo(dynamicId,characterId):
	'''获取包裹的信息'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'messgae':""}
	data=gamer.pack.getPackageItemList()
	return data
