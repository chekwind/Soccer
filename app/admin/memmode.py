#coding:utf8
'''
Created on 2014-3-20

@author: CC
'''

from firefly.dbentrust.mmode import MAdmin

register_admin=MAdmin('tb_register','username')
register_admin.insert()