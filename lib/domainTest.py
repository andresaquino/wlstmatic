#!/usr/bin/env python 
# vim: set ts=3 sw=3 sts=3 si ai: 

# domainTest.py 
# =
# 
# Andres Aquino <aquino(at)hp.com>
# Hewlett-Packard Company
# 
import os
import sys

if __name__ == "main":
	try:
		connect('admin', 'nextel123', 't3://10.103.12.144:9801')
	except:
		print 'Connection failed...'
		print dumpStack()
		exit()

# 
