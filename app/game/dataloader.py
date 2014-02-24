#coding:utf8
'''
Created on 2014-1-17

@author: CC
'''

from app.share.dbopear import dbShieldWord,dbPlayer,dbItems
import memmode
from firefly.dbentrust.madminanager import MAdminManager

def load_config_data():
	"""从数据库中读取配置信息
	"""
	dbShieldWord.getAll_ShieldWord()
	dbPlayer.getPlayerExp()
	dbPlayer.getAllPlayerTemplate()
	for i in range(1,6):
		dbPlayer.getFindPlayerTemplateByLeague(i)
	dbItems.getAll_ItemTemplate()

def registe_madmin():
	"""注册数据库与memcached对应
	"""
	MAdminManager().registe(memmode.tb_character_admin)
	MAdminManager().registe(memmode.tb_player_admin)
	MAdminManager().registe(memmode.tb_item_admin)
	MAdminManager().registe(memmode.tb_zen_admin)