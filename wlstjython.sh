#!/bin/sh 
# vim :set ts=2 sw=2 sts=2 et si ai:

# wlstjython.sh 
# =
# 
# Andres Aquino <aquino(at)hp.com>
# Hewlett-Packard Company
# 

# load environment
. ${HOME}/.wlstmaticrc

export CLASSPATH=
CLASSPATH="${CLASSPATH}:${MD_HOME}/patch_wls1033/profiles/default/sys_manifest_classpath/weblogic_patch.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/patch_oepe1033/profiles/default/sys_manifest_classpath/weblogic_patch.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/patch_ocp353/profiles/default/sys_manifest_classpath/weblogic_patch.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/wlserver_10.3/server/lib/weblogic_sp.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/wlserver_10.3/server/lib/weblogic.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/modules/features/weblogic.server.modules_10.3.3.0.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/wlserver_10.3/server/lib/webservices.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/modules/org.apache.ant_1.7.1/lib/ant-all.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/modules/net.sf.antcontrib_1.1.0.0_1-0b2/lib/ant-contrib.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/wlserver_10.3/server/lib/weblogic.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/utils/config/10.3/config-launch.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/wlserver_10.3/common/derby/lib/derbynet.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/wlserver_10.3/common/derby/lib/derbyclient.jar"
CLASSPATH="${CLASSPATH}:${MD_HOME}/wlserver_10.3/common/derby/lib/derbytools.jar"

echo $CLASSPATH
java -jar /opt/jython/jython.jar


# 
