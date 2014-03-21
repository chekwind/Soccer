#coding:utf8
'''
Created on 2014-3-20

@author: CC
'''

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web import vhost
from handle import OperaGamer,DayRecored,Statistics

def loadModule():
	root=vhost.NameVirtualHost()
	root.putChild('opera',OperaGamer())
	root.putChild('dayrecored',DayRecored())
	root.putChild('statistics',Statistics())
	reactor.listenTCP(2014,Site(root))