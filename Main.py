# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QVBoxLayout,
    QWidget)

from VideoSlider import VideoSlider

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(860, 560)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.videoLayout = QGridLayout()
        self.videoLayout.setSpacing(0)
        self.videoLayout.setObjectName(u"videoLayout")

        self.gridLayout_2.addLayout(self.videoLayout, 0, 0, 1, 1)

        self.bottomWidget = QWidget(self.centralwidget)
        self.bottomWidget.setObjectName(u"bottomWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bottomWidget.sizePolicy().hasHeightForWidth())
        self.bottomWidget.setSizePolicy(sizePolicy)
        self.bottomWidget.setStyleSheet(u"*{\n"
"	background:None;\n"
"}\n"
"#bottomWidget{\n"
"	background-color:rgb(195, 195, 195);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.bottomWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.progressWidget = QWidget(self.bottomWidget)
        self.progressWidget.setObjectName(u"progressWidget")
        sizePolicy.setHeightForWidth(self.progressWidget.sizePolicy().hasHeightForWidth())
        self.progressWidget.setSizePolicy(sizePolicy)
#         self.progressWidget.setStyleSheet(u"QSlider::groove:horizontal {\n"
# "	border: 1px solid #bbb;\n"
# "	background: white;\n"
# "	height: 6px;\n"
# "	border-radius: 4px;\n"
# "}\n"
# "\n"
# "QSlider::handle:horizontal {\n"
# "	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ccc);\n"
# "	border: 1px solid #777;\n"
# "\n"
# "	width: 9px;\n"
# "	margin-top: -2px;\n"
# "	margin-bottom: -2px;\n"
# "	border-radius: 5px;\n"
# "\n"
# "	\n"
# "}\n"
# "\n"
# "QSlider::sub-page:horizontal {\n"
# "	background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1, stop: 0 #67bed0, stop: 1 #67bed0);\n"
# "	background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,  stop: 0 #0800ec, stop: 1 #0800ec);\n"
# "	border: 1px solid #777;\n"
# "	height: 10px;\n"
# "	border-radius: 4px;\n"
# "}\n"
# "\n"
# "QSlider::add-page:horizontal {\n"
# "	background: #fff;\n"
# "	border: 1px solid #777;\n"
# "	height: 10px;\n"
# "	border-radius: 4px;\n"
# "}\n"
# "\n"
# "\n"
# "\n"
# "QSlider::handle:horizontal:hover {\n"
# "	background: qlineargradient(x1:0, y1:0, x2:1, y2:1,   stop:0 #fff, stop:1 #ddd);\n"
# "	border: 1px solid #444;\n"
# ""
#                         "	width: 11px;\n"
# "	margin-top: -3.5px;\n"
# "	margin-bottom: -3.5px;\n"
# "	border-radius: 5px;\n"
# "}\n"
# "\n"
# "QSlider::sub-page:horizontal:disabled {\n"
# "	background: #bbb;\n"
# "	border-color: #999;\n"
# "}\n"
# "\n"
# "QSlider::add-page:horizontal:disabled {\n"
# "	background: #eee;\n"
# "	border-color: #999;\n"
# "}\n"
# "\n"
# "QSlider::handle:horizontal:disabled {\n"
# "	background: #eee;\n"
# "	border: 1px solid #aaa;\n"
# "	border-radius: 4px;\n"
# "}")
        self.horizontalLayout = QHBoxLayout(self.progressWidget)
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(12, 4, 12, 0)
        self.startTimeLabel = QLabel(self.progressWidget)
        self.startTimeLabel.setObjectName(u"startTimeLabel")

        self.horizontalLayout.addWidget(self.startTimeLabel)

        self.videoSlider = VideoSlider(self.progressWidget)
        self.videoSlider.setObjectName(u"videoSlider")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.videoSlider.sizePolicy().hasHeightForWidth())
        self.videoSlider.setSizePolicy(sizePolicy1)
        self.videoSlider.setMinimumSize(QSize(0, 0))
        self.videoSlider.setMaximumSize(QSize(16777215, 16))
        self.videoSlider.setAutoFillBackground(False)
        self.videoSlider.setStyleSheet(u"")
        # self.videoSlider.setValue(54)
        # self.videoSlider.setSliderPosition(54)
        self.videoSlider.setTracking(True)
        self.videoSlider.setOrientation(Qt.Horizontal)
        self.videoSlider.setInvertedAppearance(False)
        self.videoSlider.setInvertedControls(False)

        self.horizontalLayout.addWidget(self.videoSlider)

        self.endTimeLabel = QLabel(self.progressWidget)
        self.endTimeLabel.setObjectName(u"endTimeLabel")

        self.horizontalLayout.addWidget(self.endTimeLabel)


        self.verticalLayout.addWidget(self.progressWidget)

        self.controlFrame = QFrame(self.bottomWidget)
        self.controlFrame.setObjectName(u"controlFrame")
        sizePolicy.setHeightForWidth(self.controlFrame.sizePolicy().hasHeightForWidth())
        self.controlFrame.setSizePolicy(sizePolicy)
        self.controlFrame.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.controlFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 2, 8, 8)
        self.playButton = QPushButton(self.controlFrame)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setMinimumSize(QSize(34, 34))
        self.playButton.setMaximumSize(QSize(34, 34))
        self.playButton.setBaseSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u"play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.playButton)

        self.stopButton = QPushButton(self.controlFrame)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(34, 34))
        self.stopButton.setMaximumSize(QSize(34, 34))
        self.stopButton.setBaseSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u"stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.stopButton)

        self.previousButton = QPushButton(self.controlFrame)
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.setMinimumSize(QSize(34, 34))
        self.previousButton.setMaximumSize(QSize(34, 34))
        self.previousButton.setBaseSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u"previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previousButton.setIcon(icon2)
        self.previousButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.previousButton)

        self.nextButton = QPushButton(self.controlFrame)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMinimumSize(QSize(34, 34))
        self.nextButton.setMaximumSize(QSize(34, 34))
        self.nextButton.setBaseSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u"next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextButton.setIcon(icon3)
        self.nextButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.nextButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.playlistButton = QPushButton(self.controlFrame)
        self.playlistButton.setObjectName(u"playlistButton")
        self.playlistButton.setMaximumSize(QSize(34, 34))
        self.playlistButton.setBaseSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u"playlist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playlistButton.setIcon(icon4)
        self.playlistButton.setIconSize(QSize(20, 20))
        self.playlistButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.playlistButton)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.volumeSlider = QSlider(self.controlFrame)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMaximumSize(QSize(80, 16777215))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setOrientation(Qt.Horizontal)
        self.volumeSlider.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_2.addWidget(self.volumeSlider)


        self.verticalLayout.addWidget(self.controlFrame)


        self.gridLayout_2.addWidget(self.bottomWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 860, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.startTimeLabel.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
        self.endTimeLabel.setText(QCoreApplication.translate("MainWindow", u"00:00:00", None))
#if QT_CONFIG(tooltip)
        self.playButton.setToolTip(QCoreApplication.translate("MainWindow", u"play/pause", None))
#endif // QT_CONFIG(tooltip)
        self.playButton.setText("")
#if QT_CONFIG(tooltip)
        self.stopButton.setToolTip(QCoreApplication.translate("MainWindow", u"stop", None))
#endif // QT_CONFIG(tooltip)
        self.stopButton.setText("")
#if QT_CONFIG(tooltip)
        self.previousButton.setToolTip(QCoreApplication.translate("MainWindow", u"previous", None))
#endif // QT_CONFIG(tooltip)
        self.previousButton.setText("")
#if QT_CONFIG(tooltip)
        self.nextButton.setToolTip(QCoreApplication.translate("MainWindow", u"next", None))
#endif // QT_CONFIG(tooltip)
        self.nextButton.setText("")
#if QT_CONFIG(tooltip)
        self.playlistButton.setToolTip(QCoreApplication.translate("MainWindow", u"playlist", None))
#endif // QT_CONFIG(tooltip)
        self.playlistButton.setText("")
    # retranslateUi

