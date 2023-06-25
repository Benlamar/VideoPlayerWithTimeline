# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main.ui'
##
# Created by: Qt User Interface Compiler version 6.5.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QStandardPaths, Qt, Slot)
from PySide6.QtGui import (QAction, QIcon, QKeySequence)
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QFileDialog)


# multi media module
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaFormat,
                                  QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget

from Main import Ui_MainWindow

import sys
import os
PATH = os.path.dirname(__file__)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # audio and mediaplayer init
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        # adding the menu
        file_menu = self.ui.menubar.addMenu("&File")
        icon = QIcon.fromTheme("document-open")
        open_action = QAction(icon, "&Open...", self,
                              shortcut=QKeySequence.Open, triggered=self.open)
        file_menu.addAction(open_action)
        # adding the video widget
        self._video_widget = QVideoWidget()
        self._player.setVideoOutput(self._video_widget)
        self.ui.videoLayout.addWidget(self._video_widget)

        # controls trigger
        self.ui.playButton.clicked.connect(self.playPause)
        self.ui.stopButton.clicked.connect(self.stopPlayer) 
        self.ui.nextButton.clicked.connect(self.nextVideo)
        self.ui.previousButton.clicked.connect(self.previousVideo)
        
        # volume slider
        volume = self._audio_output.volume() * 100
        self.ui.volumeSlider.setValue(volume)
        self.ui.volumeSlider.valueChanged.connect(self.setAudioVolume)

        # video progress
        self._player.durationChanged.connect(self.durationUpdate)
        self._player.positionChanged.connect(self.positionUpdate)

        self.video_slider = self.ui.videoSlider
        # self.video_slider.valueChanged.connect(lambda x : print(x))


        color_ranges = [(55/100, 60/100, "#ffbf31")]
        self.video_slider.setColorRanges(color_ranges)

    # open options currently only single files
    @Slot()
    def open(self):
        file_dialog = QFileDialog(self, directory='C:\\Users\\BLACK\\Desktop\\BLACK\\PyQT\\VideoSeek')
        movies_location = QStandardPaths.writableLocation(QStandardPaths.MoviesLocation)
        file_dialog.setDirectory(movies_location)

        if file_dialog.exec() == QDialog.Accepted:
            url = file_dialog.selectedUrls()[0]
            self._player.setSource(url)
            self._player.play()

    # toggle play/pause
    def playPause(self):
        if self._player.isPlaying():
            icon = PATH + "/pause.png"
            self._player.pause()
        else:
            icon = PATH + "/play.png"
            self._player.play()
        # toggle icons as well
        self.ui.playButton.setIcon(QIcon(icon))

    # stop player
    def stopPlayer(self):
        self._player.stop()

    # next player
    def nextVideo(self):
        print("Next")

    # next player
    def previousVideo(self):
        print("Previous")

    # change volume when change
    def setAudioVolume(self, value):
        self._audio_output.setVolume(value/100)

    # vidoe progress update
    def durationUpdate(self, duration):
        self.video_slider.setMaximum(duration)
        if duration >= 0:
                self.ui.endTimeLabel.setText(str(duration))
        # self.progress.setMaximum(duration)

    def positionUpdate(self, pos):
        self.video_slider.blockSignals(True)
        self.video_slider.setValue(pos)
        self.video_slider.blockSignals(False)
        # self.progress.setValue(pos)
        # print("position",pos)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
