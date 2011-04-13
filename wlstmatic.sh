#!/bin/sh 
# vim: set ts=2 sw=2 sts=2 et si ai:
 
# wlstmatic.sh - WLSTMatic
# =-=
#
# Developer
# Andres Aquino <aquino at hp.com>
#

# load environment
. ${HOME}/.wlstmaticrc

# set up common environment
. ${WL_HOME}/server/bin/setWLSEnv.sh > /dev/null 2>&1

CLASSPATH="${CLASSPATH}${CLASSPATHSEP}${FMWLAUNCH_CLASSPATH}"
CLASSPATH="${CLASSPATH}${CLASSPATHSEP}${DERBY_CLASSPATH}"
CLASSPATH="${CLASSPATH}${CLASSPATHSEP}${DERBY_TOOLS}"
CLASSPATH="${CLASSPATH}${CLASSPATHSEP}${POINTBASE_CLASSPATH}"
CLASSPATH="${CLASSPATH}${CLASSPATHSEP}${POINTBASE_TOOLS}"

if [ "${WLST_HOME}" != "" ] ; then
  WLST_PROPERTIES="-Dweblogic.wlstHome='${WLST_HOME}' ${WLST_PROPERTIES}"
  export WLST_PROPERTIES
fi

#JVM_ARGS="-Dprod.props.file='${WL_HOME}'/.product.properties ${WLST_PROPERTIES} ${JVM_D64} ${MEM_ARGS} ${CONFIG_JVM_ARGS}"
JVM_ARGS="${WLST_PROPERTIES} ${JVM_D64} ${MEM_ARGS} ${CONFIG_JVM_ARGS}"

echo "${CLASSPATH}"
#echo "${JAVA_HOME}/bin/java ${JVM_ARGS} weblogic.WLST $@"
/usr/lib/jvm/java-6-sun/bin/java ${JVM_ARGS} weblogic.WLST "$@"

