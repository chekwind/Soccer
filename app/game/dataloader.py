#coding:utf8
'''
Created on 2014-1-17

@author: CC
'''

from app.share.dbopear import dbShieldWord,dbPlayer,dbItems,dbTask,dbExperience
import memmode
from firefly.dbentrust.madminanager import MAdminManager

def load_config_data():
	"""从数据库中读取配置信息
	"""
	dbShieldWord.getAll_ShieldWord()#载入关键字
	dbPlayer.getPlayerExp()#载入球员升级经验配置
	dbPlayer.getAllPlayerTemplate()#载入球员搜索模板
	for i in range(1,6):
		dbPlayer.getFindPlayerTemplateByLeague(i)
	dbItems.getAll_ItemTemplate()#载入道具模板
	dbTask.getALLTask()#载入任务
	dbExperience.getExperience_Config()#载入角色升级经验表


def registe_madmin():
	"""注册数据库与memcached对应
	"""
	MAdminManager().registe(memmode.tb_character_admin)
	MAdminManager().registe(memmode.tb_player_admin)
	MAdminManager().registe(memmode.tb_item_admin)
	MAdminManager().registe(memmode.tb_zen_admin)