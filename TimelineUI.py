# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\timeline.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TimelineNavigator(object):
    def setupUi(self, TimelineNavigator):
        TimelineNavigator.setObjectName("TimelineNavigator")
        TimelineNavigator.resize(240, 191)
        TimelineNavigator.setMinimumSize(QtCore.QSize(240, 140))
        TimelineNavigator.setMaximumSize(QtCore.QSize(260, 480))
        self.gridLayout = QtWidgets.QGridLayout(TimelineNavigator)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalFrame = QtWidgets.QFrame(TimelineNavigator)
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listView = QtWidgets.QListView(self.verticalFrame)
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)
        self.gridLayout.addWidget(self.verticalFrame, 0, 0, 1, 1)

        self.retranslateUi(TimelineNavigator)
        QtCore.QMetaObject.connectSlotsByName(TimelineNavigator)

    def retranslateUi(self, TimelineNavigator):
        _translate = QtCore.QCoreApplication.translate
        TimelineNavigator.setWindowTitle(_translate("TimelineNavigator", "TimelineNavigator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TimelineNavigator = QtWidgets.QWidget()
    ui = Ui_TimelineNavigator()
    ui.setupUi(TimelineNavigator)
    TimelineNavigator.show()
    sys.exit(app.exec_())