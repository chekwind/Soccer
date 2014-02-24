#coding:utf8
'''
Created on 2014-2-24

@author: CC
'''
from app.game.component.Component import Component
from app.share.dbopear import dbShop

class CharacterShopComponent(Component):
	'''
	商店类
	'''

	def __init__(self,owner):
		Component.__init__(self,owner)
		self.shopPackage=ShopPackage()

	def initShopItems(self):
		'''初始化商店物品
		'''
		self.shopPackage.clearAllShopPackage()
		for shopType in range(1,2):
			items=self.updateShopItems(shopType)
			for item in items:
				self.shopPackage.putItemInShopPackage(shopType,item)

	def getShopPackage(self,shopType):
		'''获取商店物品信息
		@param shopType:int 商店类型 1金币 2银币
		'''
		if shopType==1:
			shopPackage=self.shopPackage.coinShopPackage
		elif shopType==2:
			shopPackage=self.shopPackage.gamecoinShopPackage

		if not shopPackage.getItems():
			self.initShopItems()
		return shopPackage

	def updateShopItems(self,shopType):
		'''获取商店物品
		@param shopType:int 商店类型
		'''
		list=[]
		shopInfo=dbShop.getShopInfo(shopType)
		if not shopInfo:
			return list
		shopInfo=shopInfo[0]
		count=shopInfo['count']
		for i in range(0,count):
			item=Item(27)
			list.append(item)
		return list

