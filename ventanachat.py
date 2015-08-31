# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanachat.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import time
import json
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(359, 471)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.LineTexURL = QtGui.QLineEdit(self.centralwidget)
        self.LineTexURL.setGeometry(QtCore.QRect(0, 0, 271, 31))
        self.LineTexURL.setObjectName(_fromUtf8("LineTexURL"))
        self.QWNavegadorWeb = QtWebKit.QWebView(self.centralwidget)
        self.QWNavegadorWeb.setGeometry(QtCore.QRect(0, 30, 359, 421))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica LT Std"))
        self.QWNavegadorWeb.setFont(font)
        self.QWNavegadorWeb.setUrl(QtCore.QUrl(_fromUtf8("https://www.livecoding.tv/accounts/login/?next=/chat/crearmijuego/")))
        self.QWNavegadorWeb.setObjectName(_fromUtf8("QWNavegadorWeb"))
        self.PushButtonEntrar = QtGui.QPushButton(self.centralwidget)
        self.PushButtonEntrar.setGeometry(QtCore.QRect(270, 0, 91, 31))
        self.PushButtonEntrar.setObjectName(_fromUtf8("PushButtonEntrar"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(0, 450, 361, 23))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Helvetica LT Std"))
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.mensajenuevo = 0

        def escribirjson(tipomsg,cantidadmsg,nick,msg):
            fh = open("nodejs/mensajes.json","w");
            fh.write("{\n  \"tipomsg\": \""+tipomsg+"\",\n  \"cantidadmsg\": \""+cantidadmsg+"\",\n  \"nick\": \""+nick+"\",\n  \"msg\": \""+msg+"\"\n}")
            fh.close()

        def mensajeschat():
            elementos = self.QWNavegadorWeb.page().mainFrame().documentElement()
            mensajescantidad = elementos.findAll(".message").count()
            mensajechatultimo = (elementos.findAll(".message")).last()
            mensajechattemp =  (mensajechatultimo).toPlainText()
            mensajechattemp2 = mensajechattemp.replace('\\','\\\\').replace('"','\\"').replace('\n',' ')

            nickname = (mensajechatultimo.findFirst(".nickname")).toInnerXml()

            mensajechat = mensajechattemp2[len(nickname):len(mensajechattemp2)]


            if self.mensajenuevo!=mensajescantidad:
                self.mensajenuevo = mensajescantidad
                if nickname!="":
                    escribirjson("msg",str(mensajescantidad),nickname,mensajechat)
                else:
                    nicknuevo = mensajechat[ 0 : (len(mensajechat))-17]
                    escribirjson("conectado",str(mensajescantidad),nicknuevo,"Bienvenido al Streaming")

        def tiempotimer():
            global timer
            timer = QtCore.QTimer()
            timer.start(100)
            timer.timeout.connect(mensajeschat)

        tiempotimer()

        def entrarcanal():
            self.QWNavegadorWeb.setUrl(QtCore.QUrl(_fromUtf8("https://www.livecoding.tv/chat/"+self.LineTexURL.text()+"/")))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.QWNavegadorWeb, QtCore.SIGNAL(_fromUtf8("loadProgress(int)")), self.progressBar.setValue)
       # QtCore.QObject.connect(self.LineTexURL, QtCore.SIGNAL(_fromUtf8("textChanged(QString)")), self.QWNavegadorWeb.reload)
        QtCore.QObject.connect(self.PushButtonEntrar, QtCore.SIGNAL(_fromUtf8("clicked()")), entrarcanal)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MiniChatiLivecoding", None))
        self.PushButtonEntrar.setText(_translate("MainWindow", "Entrar", None))

from PyQt4 import QtWebKit

if __name__=="__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())