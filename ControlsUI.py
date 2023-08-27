# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ControlsUI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QWidget)
import resource_rc

from VideoSlider import VideoSlider

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(732, 57)
        Form.setStyleSheet(u"#Form{background-color: rgb(238, 238, 238);}")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 8)
        self.controlWidget = QWidget(Form)
        self.controlWidget.setObjectName(u"controlWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlWidget.sizePolicy().hasHeightForWidth())
        self.controlWidget.setSizePolicy(sizePolicy)
        self.controlWidget.setStyleSheet(u"#volumeSlider::groove:horizontal {\n"
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
"}\n"
"\n"
"QPushButton{\n"
"   	border-color: rgb(255, 219, 168);\n"
"   	background-color: rgb(255, 190, 111);\n"
"	border-radius: 2px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	border: 1px solid rgb(24, 103, 155);\n"
"	background-color: rgb(255, 163, 72);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	borde"
                        "r: 1px solid rgb(24, 103, 155);\n"
"	background-color: rgb(230, 97, 0);\n"
"	border-radius: 4px;\n"
" }")
        self.horizontalLayout_2 = QHBoxLayout(self.controlWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, 2, 8, 2)
        self.playButton = QPushButton(self.controlWidget)
        self.playButton.setObjectName(u"playButton")
        self.playButton.setMinimumSize(QSize(26, 26))
        self.playButton.setMaximumSize(QSize(26, 26))
        self.playButton.setBaseSize(QSize(30, 30))
        self.playButton.setToolTipDuration(2)
        self.playButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/images/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playButton.setIcon(icon)
        self.playButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.playButton)

        self.stopButton = QPushButton(self.controlWidget)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(26, 26))
        self.stopButton.setMaximumSize(QSize(26, 26))
        self.stopButton.setBaseSize(QSize(30, 30))
        self.stopButton.setToolTipDuration(2)
        icon1 = QIcon()
        icon1.addFile(u":/images/icons/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.stopButton)

        self.previousButton = QPushButton(self.controlWidget)
        self.previousButton.setObjectName(u"previousButton")
        self.previousButton.setMinimumSize(QSize(26, 26))
        self.previousButton.setMaximumSize(QSize(26, 26))
        self.previousButton.setBaseSize(QSize(30, 30))
        self.previousButton.setToolTipDuration(2)
        icon2 = QIcon()
        icon2.addFile(u":/images/icons/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previousButton.setIcon(icon2)
        self.previousButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.previousButton)

        self.nextButton = QPushButton(self.controlWidget)
        self.nextButton.setObjectName(u"nextButton")
        self.nextButton.setMinimumSize(QSize(26, 26))
        self.nextButton.setMaximumSize(QSize(26, 26))
        self.nextButton.setBaseSize(QSize(30, 30))
        self.nextButton.setToolTipDuration(2)
        icon3 = QIcon()
        icon3.addFile(u":/images/icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.nextButton.setIcon(icon3)
        self.nextButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.nextButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.playlistButton = QPushButton(self.controlWidget)
        self.playlistButton.setObjectName(u"playlistButton")
        self.playlistButton.setMinimumSize(QSize(26, 26))
        self.playlistButton.setMaximumSize(QSize(26, 26))
        self.playlistButton.setBaseSize(QSize(30, 30))
        self.playlistButton.setToolTipDuration(2)
        icon4 = QIcon()
        icon4.addFile(u":/images/icons/playlist.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playlistButton.setIcon(icon4)
        self.playlistButton.setIconSize(QSize(20, 20))
        self.playlistButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.playlistButton)

        self.timelineButton = QPushButton(self.controlWidget)
        self.timelineButton.setObjectName(u"timelineButton")
        self.timelineButton.setMinimumSize(QSize(26, 26))
        self.timelineButton.setMaximumSize(QSize(26, 26))
        self.timelineButton.setBaseSize(QSize(30, 30))
        self.timelineButton.setToolTipDuration(2)
        icon5 = QIcon()
        icon5.addFile(u":/images/icons/layout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.timelineButton.setIcon(icon5)
        self.timelineButton.setIconSize(QSize(20, 20))
        self.timelineButton.setAutoDefault(False)
        self.timelineButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.timelineButton)

        self.horizontalSpacer_2 = QSpacerItem(10, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.volumeSlider = QSlider(self.controlWidget)
        self.volumeSlider.setObjectName(u"volumeSlider")
        self.volumeSlider.setMaximumSize(QSize(80, 16777215))
        self.volumeSlider.setToolTipDuration(2)
        self.volumeSlider.setMaximum(100)
        self.volumeSlider.setValue(67)
        self.volumeSlider.setOrientation(Qt.Horizontal)
        self.volumeSlider.setTickPosition(QSlider.TicksBelow)

        self.horizontalLayout_2.addWidget(self.volumeSlider)


        self.gridLayout.addWidget(self.controlWidget, 1, 0, 1, 1)

        self.progressWidget = QWidget(Form)
        self.progressWidget.setObjectName(u"progressWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.progressWidget.sizePolicy().hasHeightForWidth())
        self.progressWidget.setSizePolicy(sizePolicy1)
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
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.videoSlider.sizePolicy().hasHeightForWidth())
        self.videoSlider.setSizePolicy(sizePolicy2)
        self.videoSlider.setMinimumSize(QSize(0, 0))
        self.videoSlider.setMaximumSize(QSize(16777215, 16))
        self.videoSlider.setAutoFillBackground(False)
        self.videoSlider.setStyleSheet(u"")
        self.videoSlider.setValue(0)
        self.videoSlider.setSliderPosition(0)
        self.videoSlider.setTracking(True)
        self.videoSlider.setOrientation(Qt.Horizontal)
        self.videoSlider.setInvertedAppearance(False)
        self.videoSlider.setInvertedControls(False)

        self.horizontalLayout.addWidget(self.videoSlider)

        self.endTimeLabel = QLabel(self.progressWidget)
        self.endTimeLabel.setObjectName(u"endTimeLabel")

        self.horizontalLayout.addWidget(self.endTimeLabel)


        self.gridLayout.addWidget(self.progressWidget, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.timelineButton.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.playButton.setToolTip(QCoreApplication.translate("Form", u"play/pause", None))
#endif // QT_CONFIG(tooltip)
        self.playButton.setText("")
#if QT_CONFIG(shortcut)
        self.playButton.setShortcut(QCoreApplication.translate("Form", u"Space", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.stopButton.setToolTip(QCoreApplication.translate("Form", u"stop", None))
#endif // QT_CONFIG(tooltip)
        self.stopButton.setText("")
#if QT_CONFIG(tooltip)
        self.previousButton.setToolTip(QCoreApplication.translate("Form", u"previous", None))
#endif // QT_CONFIG(tooltip)
        self.previousButton.setText("")
#if QT_CONFIG(shortcut)
        self.previousButton.setShortcut(QCoreApplication.translate("Form", u"P", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.nextButton.setToolTip(QCoreApplication.translate("Form", u"next", None))
#endif // QT_CONFIG(tooltip)
        self.nextButton.setText("")
#if QT_CONFIG(shortcut)
        self.nextButton.setShortcut(QCoreApplication.translate("Form", u"N", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.playlistButton.setToolTip(QCoreApplication.translate("Form", u"playlist", None))
#endif // QT_CONFIG(tooltip)
        self.playlistButton.setText("")
#if QT_CONFIG(shortcut)
        self.playlistButton.setShortcut(QCoreApplication.translate("Form", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.timelineButton.setToolTip(QCoreApplication.translate("Form", u"Timelines", None))
#endif // QT_CONFIG(tooltip)
        self.timelineButton.setText("")
#if QT_CONFIG(shortcut)
        self.timelineButton.setShortcut(QCoreApplication.translate("Form", u"Ctrl+T", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.volumeSlider.setToolTip(QCoreApplication.translate("Form", u"volume", None))
#endif // QT_CONFIG(tooltip)
        self.startTimeLabel.setText(QCoreApplication.translate("Form", u"00:00:00", None))
        self.endTimeLabel.setText(QCoreApplication.translate("Form", u"00:00:00", None))
    # retranslateUi
