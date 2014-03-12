#coding:utf8
'''
Created on 2014-3-11

@author: CC
'''

from app.game.component.Component import Component
from app.share.dbopear import dbclub

class TrainMatchComponent(Component):
	'''训练赛组件'''

	def __init__(self,owner):
		''''''
		Component.__init__(self,owner)
		self.npc=[]
		self.initData()

	def initData(self):
		''''''
		pass

	def getNpcByLeague(self,leagueindex):
		'''根据级别获取npc球队'''
		for npc in dbclub.TRAINMATCHNPC.values():
			if npc['LeagueIndex']==leagueindex:
				self.npc.append(npc)
		return self.npc

	def getNpc(self):
		''''''
		return self.npc

	def doMacth(self,npcid):
		''''''
		from app.game.core.character.NPCClub import NPCClub
		from app.game.core.match.match import DoMatch
		npc=NPCClub(templateId=npcid)
		fig=DoMatch([self._owner],[npc])


