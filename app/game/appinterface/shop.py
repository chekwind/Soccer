#coding:utf8
'''
Created on 2014-2-24

@author: CC
'''

from app.game.core.GamersManager import GamersManager

def getShopInfo(dynamicId,characterId,shopCategory):
	'''获取商城信息
	@param dynamicId:int 客户端id
	@param characterId:int 角色id
	@param shopCategory:int 商店类型 1金币2银币
	'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'message':u""}
	package=gamer.shop.getShopPackage(shopCategory)
	result=package.getPackageItemInfo()
	data={'shopCategory':shopCategory,'packageIteminfo':result}
	return {'result':True,'data':data}