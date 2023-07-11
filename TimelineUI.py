# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'timeline.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QListView,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_TimelineNavigator(object):
    def setupUi(self, TimelineNavigator):
        if not TimelineNavigator.objectName():
            TimelineNavigator.setObjectName(u"TimelineNavigator")
        TimelineNavigator.resize(240, 191)
        TimelineNavigator.setMinimumSize(QSize(240, 140))
        TimelineNavigator.setMaximumSize(QSize(260, 480))
        self.gridLayout = QGridLayout(TimelineNavigator)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(TimelineNavigator)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.verticalFrame)
        self.listView.setObjectName(u"listView")

        self.verticalLayout.addWidget(self.listView)


        self.gridLayout.addWidget(self.verticalFrame, 0, 0, 1, 1)


        self.retranslateUi(TimelineNavigator)

        QMetaObject.connectSlotsByName(TimelineNavigator)
    # setupUi

    def retranslateUi(self, TimelineNavigator):
        TimelineNavigator.setWindowTitle(QCoreApplication.translate("TimelineNavigator", u"TimelineNavigator", None))
    # retranslateUi

