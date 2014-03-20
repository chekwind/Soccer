#coding:utf8
'''
Created on 2014-1-17

@author: CC
'''

from app.gate.core.User import User
from app.gate.core.UserManager import UsersManager
from app.gate.core.virtualcharacter import VirtualCharacter
from app.gate.core.VCharacterManager import VCharacterManager
from app.share.dbopear import dbuser
from app.game.core.language.Language import Lg
from app.gate.core.scenesermanger import SceneSerManager
from firefly.server.globalobject import GlobalObject

from twisted.python import log

def registerToServer(dynamicId,username,password):
	'''注册
	@param dynamicId:int 客户端动态ID
	@param username:str 用户名
	@param password:str 用户密码
	'''
	result=False
	userinfo=dbuser.CheckUserInfo(username)
	if not userinfo and 3<len(username)<12 and 3<len(password)<12:
		result=dbuser.creatUserInfo(username,password)
	if result:
		return {'result':True}
	else:
		return {'result':False,'message':Lg().g(22)}


def loginToServer(dynamicId,username,password):
	'''登陆服务器
	@param dynamicId:int 客户端动态ID
	@param username:str 用户名
	@param password:str 用户密码
	'''

	# if password=='crotaii':
	# 	return{'result':False}
	userinfo=dbuser.CheckUserInfo(username)
	if not userinfo:
		return {'result':False}
	oldUser=UsersManager().getUserByUsername(username)
	if oldUser:
		oldUser.dynamicId=dynamicId
		UserCharacterInfo=oldUser.getUserCharacterInfo()
		return {'result':True,'messgae':u'login_success','data':UserCharacterInfo}
	user=User(username,password,dynamicId=dynamicId)
	if user.id==0:
		return {'result':False,'messgae':u'psd_error'}
	if not user.CheckEffective():
		return {'result':False,'messgae':u'fenghao'}
	UsersManager().addUser(user)
	UserCharacterInfo=user.getUserCharacterInfo()
	return{'result':True,'messgae':u'login_success','data':UserCharacterInfo}

def activeNewGamer(dynamicId,userId,nickName):
	'''创建角色
	arguments={userId,nickName}
	userId 用户ID
	nickName 角色昵称
	profession
	'''

	user=UsersManager().getUserByDynamicId(dynamicId)
	if not user:
		return {'result':False,'messgae':u'conn_error'}
	if not user.checkClient(dynamicId):
		return {'result':False,'messgae':u'conn_error'}
	if user is None:
		return {'result':False,'messgae':u'disconnect'}
	result=user.creatNewCharacter(nickName)
	return result

def deleteRole(dynamicId,userId,characterId,password):
	'''删除角色
	@param dynamicId:int 客户端的ID
	@param userId:int 用户端ID
	@param characterId:int int 角色的ID
	@param password:str 用户的密码
	'''

	user=UsersManager().getUserByDynamicId(dynamicId)
	if not user.checkClient(dynamicId):
		return {'result':False,'messgae':u'conn_error'}
	if user is None:
		return {'result':False,'messgae':u'disconnect'}
	result=user.deleteCharacter(characterId,password)
	return result

def roleLogin(dynamicId,userId,characterId):
	'''角色登陆
	@param dynamicId:int 客户端的ID
	@param userId:int 用户的ID
	@param characterId:int 角色的ID
	'''

	user=UsersManager().getUserByDynamicId(dynamicId)
	if not user:
		return {'result':False,'messgae':u'conn_error'}
	characterInfo=user.getCharacterInfo()
	if not characterInfo:
		return {'result':False,'messgae':u'norole'}
	_characterId=user.characterId
	if _characterId!=characterId:
		return {'result':False,'messgae':u'norole'}
	oldvcharacter=VCharacterManager().getVCharacterByCharacterId(characterId)
	data={'placeId':characterInfo.get('town',1000)}
	if oldvcharacter:
		oldvcharacter.setDynamicId(dynamicId)
	else:
		vcharacter=VirtualCharacter(characterId,dynamicId)
		VCharacterManager().addVCharacter(vcharacter)
	return {'result':True,'message':u'login_success','data':data}

def enterScene(dynamicId,characterId,placeId,force):
	'''进入场景
	@param dynamicId:int 客户端的ID
	@param characterId:int 角色的ID
	@param placeId:int 场景的ID
	@param force:bool
	'''

	vgamer=VCharacterManager().getVCharacterByClientId(dynamicId)
	if not vgamer:
		return None
	nownode=SceneSerManager().getBestScenNodeId()
	d=GlobalObject().root.callChild(nownode,601,dynamicId,characterId,placeId,force,None)
	vgamer.setNode(nownode)
	SceneSerManager().addClient(nownode,vgamer.dynamicId)
	return d