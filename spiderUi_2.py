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
        MainWindow.resize(653, 395)
        self.actionHelp = QAction(MainWindow)
        self.actionHelp.setObjectName(u"actionHelp")
        font = QFont()
        font.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        self.actionHelp.setFont(font)
        self.actionGuanyu = QAction(MainWindow)
        self.actionGuanyu.setObjectName(u"actionGuanyu")
        self.actionGuanyu.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font1.setPointSize(28)
        self.title.setFont(font1)
        self.title.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.title, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(3, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font2.setPointSize(11)
        self.label_2.setFont(font2)

        self.horizontalLayout.addWidget(self.label_2)

        self.linkInputBox = QLineEdit(self.centralwidget)
        self.linkInputBox.setObjectName(u"linkInputBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.linkInputBox.sizePolicy().hasHeightForWidth())
        self.linkInputBox.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font3.setPointSize(10)
        self.linkInputBox.setFont(font3)

        self.horizontalLayout.addWidget(self.linkInputBox)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_5.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setFont(font3)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox.setMaximum(9999999)

        self.horizontalLayout_2.addWidget(self.spinBox)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.horizontalLayout_2.addWidget(self.label)

        self.spinBox_2 = QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setFont(font3)
        self.spinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(9999999)
        self.spinBox_2.setStepType(QAbstractSpinBox.DefaultStepType)
        self.spinBox_2.setValue(0)

        self.horizontalLayout_2.addWidget(self.spinBox_2)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)


        self.gridLayout.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.radioButton = QRadioButton(self.centralwidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.setExclusive(True)
        self.buttonGroup.addButton(self.radioButton)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setFont(font2)
        self.radioButton.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.buttonGroup.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font2)

        self.horizontalLayout_3.addWidget(self.radioButton_2)


        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.VLine)

        self.gridLayout_4.addWidget(self.line, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.startCrawling = QPushButton(self.centralwidget)
        self.startCrawling.setObjectName(u"startCrawling")
        self.startCrawling.setFont(font2)

        self.verticalLayout.addWidget(self.startCrawling)

        self.stopCrawling = QPushButton(self.centralwidget)
        self.stopCrawling.setObjectName(u"stopCrawling")
        self.stopCrawling.setFont(font2)

        self.verticalLayout.addWidget(self.stopCrawling)

        self.openFolder = QPushButton(self.centralwidget)
        self.openFolder.setObjectName(u"openFolder")
        self.openFolder.setFont(font2)

        self.verticalLayout.addWidget(self.openFolder)


        self.gridLayout_4.addLayout(self.verticalLayout, 0, 2, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 2, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.status = QLabel(self.centralwidget)
        self.status.setObjectName(u"status")
        font4 = QFont()
        font4.setFamily(u"\u5fae\u8f6f\u96c5\u9ed1")
        font4.setPointSize(16)
        self.status.setFont(font4)
        self.status.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.status, 2, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.progress = QLabel(self.centralwidget)
        self.progress.setObjectName(u"progress")
        self.progress.setFont(font)

        self.horizontalLayout_4.addWidget(self.progress)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.time = QLabel(self.centralwidget)
        self.time.setObjectName(u"time")
        self.time.setFont(font)

        self.horizontalLayout_4.addWidget(self.time)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 1, 0, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setFont(font3)
        self.progressBar.setValue(0)

        self.gridLayout_2.addWidget(self.progressBar, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 2, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_5, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(3, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.author = QLabel(self.centralwidget)
        self.author.setObjectName(u"author")
        self.author.setFont(font2)
        self.author.setLayoutDirection(Qt.LeftToRight)
        self.author.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.gridLayout_3.addWidget(self.author, 2, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 653, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionHelp)
        self.menu.addAction(self.actionGuanyu)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"EhSpider v0.2", None))
        self.actionHelp.setText(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.actionGuanyu.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"EhSpider v0.2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8981\u722c\u53d6\u7684\u56fe\u518c\u7684\u94fe\u63a5\uff1a", None))
        self.linkInputBox.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8981\u722c\u53d6\u7684\u56fe\u7247\u8303\u56f4\uff08\u722c\u53d6\u5168\u90e8\u7559\u7a7a\u5373\u53ef\uff09\uff1a", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"~", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u7247\u8d28\u91cf\uff1a", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u539f\u56fe", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u975e\u539f\u56fe\uff08\u63a8\u8350\uff09", None))
        self.startCrawling.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u722c\u53d6", None))
        self.stopCrawling.setText(QCoreApplication.translate("MainWindow", u"\u7ec8\u6b62\u722c\u53d6", None))
        self.openFolder.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6\u5939", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"\u722c\u53d6\u5b8c\u6210\uff01", None))
        self.progress.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.author.setText(QCoreApplication.translate("MainWindow", u"By Entity 303", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u66f4\u591a\uff08\u672a\u5b8c\u6210\uff09", None))
    # retranslateUi

