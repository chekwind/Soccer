#coding:utf8
'''
Created on 2014-3-6

@author: CC
'''

from app.game.core.GamersManager import GamersManager
from app.game.core.trainbase.TrainBase import TrainBase

def getTrainBase(dynamicId,characterId):
	'''获取训练基地信息'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'message':u""}
	trainbase=TrainBase()
	data=trainbase.getTrainBase()
	return {'result':True,'data':data}
