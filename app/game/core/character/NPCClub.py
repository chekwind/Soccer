#coding:utf8
'''
Created on 2014-2-25

@author: CC
'''
from app.game.core.character.Character import Character
from app.game.component.club.CharacterClubComponent import CharacterClubComponent
from app.share.dbopear import dbClub

class NPCClub(Character):
	'''NPC球队类'''


	def __init__(self,id=-1,name='',templateId=0,zenId=1):
		'''初始化NPC球队类'''
		data=dbClub.ALL_Clubinfo.get(templateId)
		Character.__init__(self,id,name)
		self.setCharacterType(Character.CLUBTYPE)
		self.templateId=int(data['ID'])
		self.formatInfo={}
		self.initialiseToo(data)

	def initialiseToo(self,data):
		'''初始化NPC球队信息
		@param id:int npc球队ID
		'''
		self.formatInfo['templateId']=data['ID']
		self.formatInfo['clubname']=data['ClubName']
		self.formatInfo['leagueindex']=data['LeagueIndex']
		self.formatInfo['leaguename']=data['LeagueName']
		self.formatInfo['zenid']=data['ZenID']
		self.formatInfo['clublogo']=data['ClubLogo']
		self.formatInfo['powerindex']=data['PowerIndex']
		self.formatInfo['clubpower']=data['ClubPower']
		self.formatInfo['clubcategory']=data['ClubCategory']

	def getNPCType(self):
		'''获取NPC球队类型'''
		return self.formatInfo.get('clubcategory')

	def getZenId(self):
		'''获取NPC球队的战术ID'''
		return self.formatInfo.get('zenid')

	def getClubPower(self):
		'''获取NPC球队的实力'''
		return self.formatInfo.get('clubpower')


