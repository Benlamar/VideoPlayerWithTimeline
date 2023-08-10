# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playlist.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject,
    QSize, Qt)
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QFrame, QGridLayout, QHBoxLayout,
    QListView, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout)

import resource_rc

class Ui_Playlist(object):
    def setupUi(self, Playlist):
        if not Playlist.objectName():
            Playlist.setObjectName(u"Playlist")
        Playlist.setWindowModality(Qt.WindowModal)
        Playlist.resize(240, 250)
        Playlist.setMinimumSize(QSize(240, 130))
        Playlist.setMaximumSize(QSize(260, 480))
        Playlist.setStyleSheet(u"#Playlist{\n"
"	background-color: rgb(26, 95, 180);\n"
"}")
        self.gridLayout = QGridLayout(Playlist)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(Playlist)
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
        self.listView.setMinimumSize(QSize(0, 0))
        self.listView.setMaximumSize(QSize(16777215, 16777215))
        self.listView.setDragEnabled(True)
        self.listView.setMovement(QListView.Static)
        self.listView.setProperty("isWrapping", False)
        self.listView.setResizeMode(QListView.Fixed)
        self.listView.setUniformItemSizes(True)
        self.listView.setWordWrap(True)

        self.verticalLayout.addWidget(self.listView)


        self.gridLayout.addWidget(self.verticalFrame, 0, 0, 1, 1)


        self.retranslateUi(Playlist)

        QMetaObject.connectSlotsByName(Playlist)
    # setupUi

    def retranslateUi(self, Playlist):
        Playlist.setWindowTitle(QCoreApplication.translate("Playlist", u"Playlist", None))
        self.closeButton.setText("")
    # retranslateUi

