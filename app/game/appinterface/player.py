#coding:utf8
'''
Created on 2014-2-7

@author: CC
'''

from app.game.core.GamersManager import GamersManager
from app.share.dbopear import dbPlayer
from app.game.component.player import PlayerInner

def playerListInfo(dynamicId,characterId):
	'''获取角色的球员列表'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'message':u""}
	playerList=gamer.player.FormatPlayerList()
	return {'result':True,'data':playerList}

def playertraining(dynamicId,characterId,Shoot,Dribbling,Speed,Pass,Tackle,Tackling,_Save,Response,playerid,Trainpoint):
	'''球员训练'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'message':u""}
	result=gamer.player.PlayerTraining(playerid,Shoot,Dribbling,Speed,Pass,Tackle,Tackling,_Save,Response,Trainpoint,gamer)
	return result

def addPlayerExp(dynamicId,characterId,playerid,exp):
	'''球员加经验'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'message':u""}
	result=gamer.player.addPlayerExp(playerid,exp)
	return result

def upgradePlayer(dynamicId,characterId,playerid,gamecoin,itemid):
	'''球员升级'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'message':u""}
	cgamecoin=gamer.finance.getGameCoin()
	if cgamecoin>=gamecoin:
		result=gamer.player.upgradePlayer(playerid)
		return result
	else:
		return {'result':False,'message':u"yinbibuzu"}

def signPlayer(dynamicId,characterId,templateId):#未添加银币与合同
	'''签约球员'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'message':u""}
	result=gamer.player.addPlayer(templateId)
	return result

def dropPlayer(dynamicId,characterId,playerid):#尚未添加返还训练点
	'''解雇球员'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'message':u""}
	result=gamer.player.DropPlayer(playerid)
	return result

def getPlayerInner(dynamicId,characterId):
	'''获取球员寻找信息'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'message':u""}
	data={}
	pi=gamer.playerInner
	data['xy']=pi.xy
	data['ctime1']=pi.ctime1
	data['ctime2']=pi.ctime2
	data['cs1']=pi.cs1
	data['cs2']=pi.cs2
	data['player1']=pi.inner[0]
	data['player2']=pi.inner[1]
	data['player3']=pi.inner[2]
	data['point']=pi.point
	return data

def PickPlayer(dynamicId,characterId,picktype,leagueindex,costpoint=0):
	'''挑选球员'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'message':u""}
	info=gamer.playerInner.pickPlayer(picktype,costpoint,leagueindex)
	if info.get('result'):
		playerid=info.get('data').get('playerid')
		gamer.player.addPlayer(playerid,1,3)
		playerlist=gamer.player.getPlayersListByCategory(3)
		info['data']['playerlist']=playerlist
	return info

def DissmissPlayer(dynamicId,characterId,playerid):
	'''遣散球员'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'message':u""}
	player=gamer.player.getPlayer(playerid)
	playerquality=player.level.getPlayerQuality()
	result=gamer.player.DropPlayer(playerid)
	if result:		
		returnpoint=PlayerInner.DISSMISSPOINT.get(playerquality)
		gamer.playerInner.updatePoint(returnpoint)
		info={'returnpoint':returnpoint}
		return {'result':True,'message':info}
	else:
		return {'result':False,'message':u"qiansanshibai"}

def RotatePlayer(dynamicId,characterId,mainPlayerid,benchPlayerid):
	'''球员轮换'''
	gamer=GamersManager().getGamerByID(characterId)
	if not gamer or not gamer.CheckClient(dynamicId):
		return {'result':False,'message':u""}
	mainplayer=gamer.player.getPlayer(mainPlayerid)
	benchplayer=gamer.player.getPlayer(benchPlayerid)
	if mainplayer and benchplayer:
		bebchtempID=benchplayer.templateInfo.get('id')
		if not gamer.player.IsOnCourt(bebchtempID):
			mainpos=mainplayer.getPlayerpos()
			benchpos=benchplayer.getPlayerpos()
			maincategory=mainplayer.getPlayerCategory()
			benchcategory=benchplayer.getPlayerCategory()
			mainplayer.savePlayerpos(benchpos,benchcategory)
			benchplayer.savePlayerpos(mainpos,maincategory)
			return {'result':True,'message':u""}
		else:
			return{'result':False,'message':u"qiuyuanchongfu"}
	else:
		return {'result':False,'message':u"qiuyuanbucunzai"}





