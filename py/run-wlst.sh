#!/bin/sh 
# vim: set ts=2 sw=2 sts=2 et si ai: 

# run-wlst.sh 
# =-=
# 2011, Hewlett-Packard Company
# Andres Aquino <aquino@hp.com>
# All rights reserved.
# 

export WL_HOME="${HOME}/apps/wl10mp3/wlserver_10.3"
export BEA_HOME="${HOME}/apps/wl10mp3/user_projects/domains"
export JAVA_HOME="${HOME}/apps/jdk1.6.0_24/bin"
export CLASSPATH=${WL_HOME}/server/lib/weblogic.jar:$CLASSPATH
export PATH=${WL_HOME}/server/lib/weblogic.jar:${JAVA_HOME}:${PATH}

java weblogic.WLST ${1}

