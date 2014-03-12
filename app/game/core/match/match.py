#coding:utf8
'''
Created on 2014-3-12

@author: CC
'''

from app.game.core.match.MatchSide import MatchSide

class Match:
	'''比赛类'''
	def __init__(self,activeSide,passiveSide):
		'''初始化比赛类'''
		pass

	def DoMatch():
		'''比赛计算'''
		pass











def DoMatch(challengers,deffeners):
	'''进行比赛'''
	challenger=MatchSide(challenger)
	deffener=MatchSide(deffener)
	match=Match(challenger,deffener)
	match.DoMatch()
	return match