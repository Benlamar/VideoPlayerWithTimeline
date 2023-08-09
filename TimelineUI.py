# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timeline.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TimelineNavigator(object):
    def setupUi(self, TimelineNavigator):
        TimelineNavigator.setObjectName("TimelineNavigator")
        TimelineNavigator.resize(240, 250)
        TimelineNavigator.setMinimumSize(QtCore.QSize(240, 140))
        TimelineNavigator.setMaximumSize(QtCore.QSize(260, 480))
        TimelineNavigator.setStyleSheet("#TimelineNavigator{\n"
"    background-color: rgb(26, 95, 180);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(TimelineNavigator)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalFrame = QtWidgets.QFrame(TimelineNavigator)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.handleFrame = QtWidgets.QFrame(self.verticalFrame)
        self.handleFrame.setStyleSheet("#closeButton{\n"
"    padding:0px;\n"
"}")
        self.handleFrame.setObjectName("handleFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.handleFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.closeButton = QtWidgets.QPushButton(self.handleFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closeButton.sizePolicy().hasHeightForWidth())
        self.closeButton.setSizePolicy(sizePolicy)
        self.closeButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon)
        self.closeButton.setIconSize(QtCore.QSize(18, 18))
        self.closeButton.setFlat(True)
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout.addWidget(self.closeButton)
        self.verticalLayout.addWidget(self.handleFrame)
        self.listView = QtWidgets.QListView(self.verticalFrame)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.gridLayout.addWidget(self.verticalFrame, 0, 0, 1, 1)

        self.retranslateUi(TimelineNavigator)
        QtCore.QMetaObject.connectSlotsByName(TimelineNavigator)

    def retranslateUi(self, TimelineNavigator):
        _translate = QtCore.QCoreApplication.translate
        TimelineNavigator.setWindowTitle(_translate("TimelineNavigator", "TimelineNavigator"))
import resource_rc
