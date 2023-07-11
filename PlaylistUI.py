# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'playlist.ui'
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

class Ui_Playlist(object):
    def setupUi(self, Playlist):
        if not Playlist.objectName():
            Playlist.setObjectName(u"Playlist")
        Playlist.setWindowModality(Qt.WindowModal)
        Playlist.resize(240, 220)
        Playlist.setMinimumSize(QSize(240, 130))
        Playlist.setMaximumSize(QSize(260, 480))
        self.gridLayout = QGridLayout(Playlist)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalFrame = QFrame(Playlist)
        self.verticalFrame.setObjectName(u"verticalFrame")
        self.verticalLayout = QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.verticalFrame)
        self.listView.setObjectName(u"listView")
        self.listView.setMinimumSize(QSize(0, 0))
        self.listView.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout.addWidget(self.listView)


        self.gridLayout.addWidget(self.verticalFrame, 0, 0, 1, 1)


        self.retranslateUi(Playlist)

        QMetaObject.connectSlotsByName(Playlist)
    # setupUi

    def retranslateUi(self, Playlist):
        Playlist.setWindowTitle(QCoreApplication.translate("Playlist", u"Playlist", None))
    # retranslateUi

