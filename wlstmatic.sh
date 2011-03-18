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

# wlst execution
java weblogic.WLST ${1}

