#! /bin/false

import weblogic
import javax.xml
import java.io.FileInputStream as fis
import java.io.FileOutputStream as fos

import os
import shutil

import java.io.BufferedReader as BR
import java.lang.System.in as Sin
import java.io.InputStreamReader as isr
import java.lang.System.out.print as jprint

import weblogic.security

#Standards are defined here

class ConfigStore:
  def __init__(self, fileLocation):
    factory=javax.xml.parsers.DocumentBuilderFactory.newInstance()
    builder=factory.newDocumentBuilder()
    input=fis(fileLocation)
    self.document=builder.parse(input)
    self.DOM=self.document.getDocumentElement()
  def write(self, newFileLocation):
    xmlFrom=javax.xml.transform.dom.DOMSource(self.document)
    xmlTo=javax.xml.transform.stream.StreamResult(fos(newFileLocation))
    Transformer=javax.xml.transform.TransformerFactory.newInstance().newTransformer()
    Transformer.transform(xmlFrom, xmlTo)

configxml=ConfigStore("/home/andresaquino/Downloads/config/config.xml")

es=weblogic.security.internal.SerializedSystemIni.getEncryptionService("/home/andresaquino/Downloads/security")
ces=weblogic.security.internal.encryption.ClearOrEncryptedService(es)

numServers=configxml.DOM.getElementsByTagName("server").getLength()
domainName=configxml.DOM.getAttribute("name")

print "The domain found: %s has %s servers." % (domainName, numServers)

print '## Servers'
for i in range(configxml.DOM.getElementsByTagName("server").getLength()):
  serverNode=configxml.DOM.getElementsByTagName("server").item(i)
  name=serverNode.getAttribute("name")
  print 'Server: ' + name

print '## Decrypt the JDBC passwords'
for j in range(configxml.DOM.getElementsByTagName("JDBCConnectionPool").getLength()):
  poolNode=configxml.DOM.getElementsByTagName("JDBCConnectionPool").item(j)
  print 'Name: ' +  poolNode.getAttribute("Name")
  print '\tURL: ' +  poolNode.getAttribute("URL")
  print '\tDriverName: ' +  poolNode.getAttribute("DriverName")
  print '\tUser: ' +  poolNode.getAttribute("Properties")
  print '\tPassword: ' +  ces.decrypt(poolNode.getAttribute("PasswordEncrypted"))
  print '\tTargets: ' +  poolNode.getAttribute("Targets")

print '## Decrypt the EmbeddedLDAP'
for j in range(configxml.DOM.getElementsByTagName("EmbeddedLDAP").getLength()):
  poolNode=configxml.DOM.getElementsByTagName("EmbeddedLDAP").item(j)
  print 'Name: ' + poolNode.getAttribute("Name")
  print '\tCredential: ' + ces.decrypt(poolNode.getAttribute("CredentialEncrypted"))

print '## Decrypt the Security Configuration'
for j in range(configxml.DOM.getElementsByTagName("SecurityConfiguration").getLength()):
  poolNode=configxml.DOM.getElementsByTagName("SecurityConfiguration").item(j)
  print 'Name: ' + poolNode.getAttribute("Name")
  print '\tCredential: ' + ces.decrypt(poolNode.getAttribute("CredentialEncrypted"))

print '## Decrypt the ServerStart'
for j in range(configxml.DOM.getElementsByTagName("ServerStart").getLength()):
  poolNode=configxml.DOM.getElementsByTagName("ServerStart").item(j)
  print 'Name: ' + poolNode.getAttribute("Name")
  print '\tUserName: ' + poolNode.getAttribute("Username")
  print '\tPassword: ' + ces.decrypt(poolNode.getAttribute("PasswordEncrypted"))

