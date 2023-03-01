# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spiderUi.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(861, 491)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font.setPointSize(26)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.title, 1, 1, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 105, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(278, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(268, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(9)
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)

        self.linkInputBox = QLineEdit(self.centralwidget)
        self.linkInputBox.setObjectName(u"linkInputBox")

        self.gridLayout.addWidget(self.linkInputBox, 0, 2, 1, 1)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font2.setPointSize(11)
        self.pushButton.setFont(font2)

        self.gridLayout.addWidget(self.pushButton, 0, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_5, 1, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 1, 1, 1, 3)

        self.horizontalSpacer_4 = QSpacerItem(148, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 4, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font3.setPointSize(14)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 112, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 861, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Exhentai Spider v0.2", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"Exhentai Spider v0.2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u8981\u722c\u53d6\u7684\u56fe\u518c\u7684\u94fe\u63a5\uff1a", None))
        self.linkInputBox.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u722c\u53d6", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u722c\u53d6\u5b8c\u6210\uff01", None))
    # retranslateUi

