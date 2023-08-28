# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar,
    QSizePolicy, QToolBar, QWidget)
import resource_rc

from PySide6.QtMultimediaWidgets import QVideoWidget

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(685, 474)
        mainWindow.setAnimated(False)
        mainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.videoWidget = QVideoWidget(self.centralwidget)
        self.videoWidget.setObjectName(u"videoWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.videoWidget.sizePolicy().hasHeightForWidth())
        self.videoWidget.setSizePolicy(sizePolicy)
        self.videoWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.videoLayout = QGridLayout(self.videoWidget)
        self.videoLayout.setSpacing(0)
        self.videoLayout.setObjectName(u"videoLayout")
        self.videoLayout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.videoWidget, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 685, 22))
        mainWindow.setMenuBar(self.menubar)
        self.ControlBar = QToolBar(mainWindow)
        self.ControlBar.setObjectName(u"ControlBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ControlBar.sizePolicy().hasHeightForWidth())
        self.ControlBar.setSizePolicy(sizePolicy1)
        self.ControlBar.setMinimumSize(QSize(0, 60))
        self.ControlBar.setMaximumSize(QSize(16777215, 80))
        self.ControlBar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.ControlBar.setAutoFillBackground(True)
        self.ControlBar.setMovable(False)
        self.ControlBar.setFloatable(True)
        mainWindow.addToolBar(Qt.BottomToolBarArea, self.ControlBar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.ControlBar.setWindowTitle(QCoreApplication.translate("mainWindow", u"ControlBar", None))
    # retranslateUi

