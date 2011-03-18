#Created by Danyboy 
#Daniel Gonzalez Valdivia <dagonzalv@gmail.com> 02-03-2011
#Crea un dominio nuevo en el weblogic instalado 

import os
import sys

WLHOME=os.environ['WL_HOME']
BEAHOME=os.environ['BEA_HOME']

domainTemplatePath = WLHOME + '/common/templates/domains/wls.jar'
domainDirectory = BEAHOME + 'user_projects/domains/d_wlstnew'

print ('Reading the template: ')
readTemplate(domainTemplatePath)
#readTemplate(WLHOME+'/common/templates/domains/wls.jar')
print ('Template was read turururururur')


#======================================================================
# creamos el dominio a partir de que leimos anteriormente con template
#======================================================================

cd('Servers/AdminServer')
AdminName=raw_input('Please Ente AdminServerName: ')
set('Name',AdminName)

#======================================================================
# Configuramos el super servidor
#======================================================================

AdminListenAdr=raw_input('Please Enter Admin Listen Address: ')
AdminListenPort=input('Please enter Admin listen Port: ')


set('ListenAddress',AdminListenAdr)
set('ListenPort', AdminListenPort)

#======================================================================
# definimos el pwd
#======================================================================


cd('/')
cd('Security/base_domain/User/weblogic')
usr=raw_input('Please Enter AdminUser Name: ')
set('Name',usr)
AdminPassword=raw_input('Please enter Admin password:')
cmo.setPassword(AdminPassword)


#==============================================
# Escribe el dominio nuevo, cierra el template  y sale de la consola  WLST
#==============================================

domainPath=raw_input('Enter the domain path: ')
domainName=raw_input('Enter domain name: ')
print 'Given domain path, name : ', domainPath, domainName
writeDomain(domainPath+"/"+domainName)


#==============================================
# Arranca la consola de weblogic
#==============================================

command = "nohup sh "+domainPath+"/"+domainName+"/bin/startWebLogic.sh &"
os.system(command)


closeTemplate()
exit()

#----------------------------------------------------------------------
