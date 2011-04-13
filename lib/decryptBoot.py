#! /bin/false

import java.util.ResourceBundle as rsb
import os
import shutil
import weblogic.security

bootproperties=rsb.getBundle("boot")

es=weblogic.security.internal.SerializedSystemIni.getEncryptionService("/home/andresaquino/Downloads/security")
ces=weblogic.security.internal.encryption.ClearOrEncryptedService(es)

print '\tUser: ' +  ces.decrypt(bootproperties.getString("username"))
print '\tPassword: ' +  ces.decrypt(bootproperties.getString("password"))
