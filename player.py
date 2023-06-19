# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main.ui'
##
# Created by: Qt User Interface Compiler version 6.5.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QStandardPaths, QRect,
                            QSize, QTime, QUrl, Qt, Slot)
from PySide6.QtGui import (QAction, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QMainWindow, QMenuBar, QSpacerItem,
                               QSizePolicy, QStatusBar, QToolBar, QWidget, QStyle, QSlider, QHBoxLayout, QDialog, QMessageBox, QFileDialog)

from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        if not self.objectName():
            self.setObjectName(u"MainWindow")
        self.resize(539, 395)
        self.setAnimated(True)
        self.setDocumentMode(True)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.videoLayout = QGridLayout()
        self.videoLayout.setObjectName(u"videoLayout")

        # adding the video widget here
        self._video_widget = QVideoWidget()
        self._player.setVideoOutput(self._video_widget)
        self.videoLayout.addWidget(self._video_widget)

        self.gridLayout_2.addLayout(self.videoLayout, 0, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(self)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 539, 21))
        self.setMenuBar(self.menubar)

        ## adding to mennu bar
        file_menu = self.menubar.addMenu("&Menu")
        icon = QIcon.fromTheme("document-open")
        open_action = QAction(icon, "&Open...", self,
                              shortcut=QKeySequence.Open, triggered=self.open)
        file_menu.addAction(open_action)


        self.statusbar = QStatusBar(self)
        self.statusbar.setObjectName(u"statusbar")
        self.setStatusBar(self.statusbar)

        self.toolBar = QToolBar(self)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        self.toolBar.setOrientation(Qt.Horizontal)

        # add buttons to toolbar (play, pause, previous, next)
        style = self.style()
        # play
        play_icon = QIcon.fromTheme("play.png",
                                    style.standardIcon(QStyle.SP_MediaPlay))
        self.play_action = self.toolBar.addAction(play_icon, 'play')
        self.play_action.triggered.connect(self.playPause)
        # stop
        stop_icon = QIcon.fromTheme("stop.png",
                                    style.standardIcon(QStyle.SP_MediaStop))
        self.stop_action = self.toolBar.addAction(stop_icon, 'stop')
        # previous
        previous_icon = QIcon.fromTheme("previous.png",
                                        style.standardIcon(QStyle.SP_MediaSkipBackward))
        self.previous_action = self.toolBar.addAction(
            previous_icon, 'previous')
        # next
        next_icon = QIcon.fromTheme("next.png",
                                    style.standardIcon(QStyle.SP_MediaSkipForward))
        self.next_action = self.toolBar.addAction(next_icon, 'next')

        # adding volume slider to the toolbar
        self._volume_slider = QSlider()
        self._volume_slider.setToolTip("Volume")
        self._volume_slider.setMinimum(0)
        self._volume_slider.setMaximum(100)
        self._volume_slider.setTickInterval(10)
        self._volume_slider.setOrientation(Qt.Horizontal)
        current_volume  = self._audio_output.volume()*100
        self._volume_slider.setValue(current_volume)
        self._volume_slider.setTickPosition(QSlider.TicksBelow)
        available_width = self.screen().availableGeometry().width()
        self._volume_slider.setFixedWidth(available_width / 10)
        self._volume_slider.valueChanged.connect(self.setAudioVolume)

        ## creating a widget to add the volume slider to push to the right side
        self.horizontalWidget = QWidget(self.toolBar)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.horizontalWidget.sizePolicy().hasHeightForWidth())
        self.horizontalWidget.setSizePolicy(sizePolicy)

        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        # expandable spacer here
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.horizontalSpacer)

        # self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.toolBar.addWidget(self.horizontalWidget)
        self.toolBar.addWidget(self._volume_slider)

        # added the toolbar to the bottom of the window
        self.addToolBar(Qt.BottomToolBarArea, self.toolBar)

        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.toolBar.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

    def _player_error(self, error, error_string):
        print("Error palying ",error_string, file=sys.stderr)

    def show_status_message(self, message):
        self.statusBar().showMessage(message, 5000)

    def playPause(self):
        if self._player.isPlaying():
            print("paused!")
            self._player.pause()
        else:
            print("play!")
            self._player.play()

    def setAudioVolume(self, value):
        # print(self._audio_output.volume())
        print(value)
        self._audio_output.setVolume(value/100)
        # self._audio_output.setVolume

    @Slot()
    def open(self):
        file_dialog = QFileDialog(self, directory='C:\\Users\\BLACK\\Desktop\\BLACK\\PyQT\\VideoSeek')
        movies_location = QStandardPaths.writableLocation(
            QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_location)

        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedUrls()[0]
            # print(url)
            self._player.setSource(url)
            self._player.play()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
