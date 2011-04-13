#!/usr/bin/env python 
# vim: set ts=3 sw=3 sts=3 si ai syntax=python: 

# test.py 
# =-=
#
# 2011, Hewlett-Packard Company
# Andres Aquino <aquino@hp.com>
# All rights reserved.
# 

warlist='list.txt'

warfiles=open(warlist)
wars=[]
try:
	for war in warfiles:
		wars.append(war.strip('\n'))
finally:
	warfiles.close()

print "Content's wars hash"
print wars
