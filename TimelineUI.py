# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timeline.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject,QSize)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout)

import resource_rc

class Ui_TimelineNavigator(object):
    def setupUi(self, TimelineNavigator):
        if not TimelineNavigator.objectName():
            TimelineNavigator.setObjectName(u"TimelineNavigator")
        TimelineNavigator.resize(240, 250)
        TimelineNavigator.setMinimumSize(QSize(240, 140))
        TimelineNavigator.setMaximumSize(QSize(260, 480))
        TimelineNavigator.setStyleSheet(u"#TimelineNavigator{\n"
"	background-color: rgb(26, 95, 180);\n"
"}")
        self.gridLayout = QGridLayout(TimelineNavigator)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(TimelineNavigator)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.handleFrame = QFrame(self.verticalFrame)
        self.handleFrame.setObjectName(u"handleFrame")
        self.handleFrame.setStyleSheet(u"#closeButton{\n"
"	padding:0px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.handleFrame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 4)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.closeButton = QPushButton(self.handleFrame)
        self.closeButton.setObjectName(u"closeButton")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u":/images/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QSize(18, 18))
        self.closeButton.setFlat(True)

        self.horizontalLayout.addWidget(self.closeButton)


        self.verticalLayout.addWidget(self.handleFrame)

        self.listView = QListView(self.verticalFrame)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)


        self.gridLayout.addWidget(self.verticalFrame, 0, 0, 1, 1)


        self.retranslateUi(TimelineNavigator)

        QMetaObject.connectSlotsByName(TimelineNavigator)
    # setupUi

    def retranslateUi(self, TimelineNavigator):
        TimelineNavigator.setWindowTitle(QCoreApplication.translate("TimelineNavigator", u"TimelineNavigator", None))
        self.closeButton.setText("")
    # retranslateUi

