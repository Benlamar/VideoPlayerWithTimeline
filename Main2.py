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
import resource_rc
from VideoSlider import VideoSlider


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(685, 436)
        mainWindow.setAnimated(True)
        mainWindow.setDocumentMode(True)
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
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
"	background-color:rgb(216, 226, 229);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.bottomWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.progressWidget = QWidget(self.bottomWidget)
        self.progressWidget.setObjectName(u"progressWidget")
        sizePolicy.setHeightForWidth(self.progressWidget.sizePolicy().hasHeightForWidth())
        self.progressWidget.setSizePolicy(sizePolicy)
        self.progressWidget.setStyleSheet(u"")
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
        # self.videoSlider.setValue(11)
        # self.videoSlider.setSliderPosition(11)
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
        self.controlFrame.setStyleSheet(u"#volumeSlider::groove:horizontal {\n"
"	border: 1px solid #bbb;\n"
"	background: white;\n"
"	height: 6px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"#volumeSlider::sub-page:horizontal {\n"
"	background: rgb(1, 77, 255);\n"
"	border: 1px solid #777;\n"
"	height: 10px;\n"
"	border-radius: 4px;\n"
"}\n"
"\n"
"#volumeSlider::handle:horizontal {\n"
"	background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #eee, stop:1 #ccc);\n"
"	border: 1px solid #777;\n"
"	width: 10px;\n"
"	margin-top: -3px;\n"
"	margin-bottom: -3px;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#volumeSlider::add-page:horizontal {\n"
"	background: #fff;\n"
"	border: 1px solid #777;\n"
"	height: 10px;\n"
"	border-radius: 4px;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.controlFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 2, 8, 8)
        self.playButton = QPushButton(self.controlFrame)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setMinimumSize(QSize(34, 34))
        self.playButton.setMaximumSize(QSize(34, 34))
        self.playButton.setBaseSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/images/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.playButton)

        self.stopButton = QPushButton(self.controlFrame)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(34, 34))
        self.stopButton.setMaximumSize(QSize(34, 34))
        self.stopButton.setBaseSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.stopButton)

        self.previousButton = QPushButton(self.controlFrame)
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.setMinimumSize(QSize(34, 34))
        self.previousButton.setMaximumSize(QSize(34, 34))
        self.previousButton.setBaseSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previousButton.setIcon(icon2)
        self.previousButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.previousButton)

        self.nextButton = QPushButton(self.controlFrame)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMinimumSize(QSize(34, 34))
        self.nextButton.setMaximumSize(QSize(34, 34))
        self.nextButton.setBaseSize(QSize(30, 30))
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
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
        icon4.addFile(u":/images/icons/playlist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playlistButton.setIcon(icon4)
        self.playlistButton.setIconSize(QSize(20, 20))
        self.playlistButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.playlistButton)

        self.timelineButton = QPushButton(self.controlFrame)
        self.timelineButton.setObjectName(u"timelineButton")
        self.timelineButton.setBaseSize(QSize(30, 30))
        icon5 = QIcon()
        icon5.addFile(u":/images/icons/layout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.timelineButton.setIcon(icon5)
        self.timelineButton.setIconSize(QSize(20, 20))
        self.timelineButton.setAutoDefault(False)
        self.timelineButton.setFlat(True)

        self.horizontalLayout_2.addWidget(self.timelineButton)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.volumeSlider = QSlider(self.controlFrame)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMaximumSize(QSize(80, 16777215))
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(67)
        self.volumeSlider.setOrientation(Qt.Horizontal)
        self.volumeSlider.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_2.addWidget(self.volumeSlider)


        self.verticalLayout.addWidget(self.controlFrame)


        self.gridLayout_2.addWidget(self.bottomWidget, 1, 0, 1, 1, Qt.AlignBottom)

        self.videoFrame = QFrame(self.centralwidget)
        self.videoFrame.setObjectName(u"videoFrame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.videoFrame.sizePolicy().hasHeightForWidth())
        self.videoFrame.setSizePolicy(sizePolicy2)
        self.videoLayout = QGridLayout(self.videoFrame)
        self.videoLayout.setSpacing(0)
        self.videoLayout.setObjectName(u"videoLayout")
        self.videoLayout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_2.addWidget(self.videoFrame, 0, 0, 1, 1)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 685, 21))
        mainWindow.setMenuBar(self.menubar)

        self.retranslateUi(mainWindow)

        self.timelineButton.setDefault(False)


        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"MainWindow", None))
        self.startTimeLabel.setText(QCoreApplication.translate("mainWindow", u"00:00:00", None))
        self.endTimeLabel.setText(QCoreApplication.translate("mainWindow", u"00:00:00", None))
#if QT_CONFIG(tooltip)
        self.playButton.setToolTip(QCoreApplication.translate("mainWindow", u"play/pause", None))
#endif // QT_CONFIG(tooltip)
        self.playButton.setText("")
#if QT_CONFIG(tooltip)
        self.stopButton.setToolTip(QCoreApplication.translate("mainWindow", u"stop", None))
#endif // QT_CONFIG(tooltip)
        self.stopButton.setText("")
#if QT_CONFIG(tooltip)
        self.previousButton.setToolTip(QCoreApplication.translate("mainWindow", u"previous", None))
#endif // QT_CONFIG(tooltip)
        self.previousButton.setText("")
#if QT_CONFIG(tooltip)
        self.nextButton.setToolTip(QCoreApplication.translate("mainWindow", u"next", None))
#endif // QT_CONFIG(tooltip)
        self.nextButton.setText("")
#if QT_CONFIG(tooltip)
        self.playlistButton.setToolTip(QCoreApplication.translate("mainWindow", u"playlist", None))
#endif // QT_CONFIG(tooltip)
        self.playlistButton.setText("")
        self.timelineButton.setText("")
    # retranslateUi

