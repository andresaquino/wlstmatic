#! /bin/sh


export WL_HOME="/home/danyboy/apps/wl10mp3/wlserver_10.3"
export BEA_HOME="/home/danyboy/apps/wl10mp3/user_projects/domains"
export JAVA_HOME="/home/danyboy/apps/jdk1.6.0_24/bin"
export CLASSPATH=$WL_HOME/server/lib/weblogic.jar:$CLASSPATH
export PATH=$WL_HOME/server/lib/weblogic.jar:$PATH
export PATH=$JAVA_HOME:$PATH

#java weblogic.WLST create_domain.py

java weblogic.WLST DeployApp.py
