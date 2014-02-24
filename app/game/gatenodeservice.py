#coding:utf8
'''
Created on 2014-1-17

@author: CC
'''

from firefly.server.globalobject import GlobalObject
from firefly.utils.services import CommandService

remoteservice=CommandService("gateremote")
GlobalObject().remote['gate']._reference.addService(remoteservice)

def remoteserviceHandle(target):
	"""
	"""
	remoteservice.mapTarget(target)