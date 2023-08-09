# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main.ui'
##
# Created by: Qt User Interface Compiler version 6.5.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWidgets import QAction, QFileDialog, QMainWindow, QApplication, QStyle

# multi media module
from PyQt5.QtMultimedia import (QMediaPlayer, QMediaPlaylist, QMediaContent)
from PyQt5.QtMultimediaWidgets import QVideoWidget

# from Main import Ui_MainWindow
from Main import Ui_mainWindow
from PlaylistView import PlaylistView
from Timeline import Timeline

import sys
from pathlib import Path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # audio and mediaplayer init
        # self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        # self._player.setAudioOutput(self._audio_output)
        
        # define a playlist here
        self.playlist = QMediaPlaylist()
        self._player.setPlaylist(self.playlist)
        self.playlist.currentIndexChanged.connect(self.playlistPositionChanged)

        # define a playlist viewer here
        self.playlistView = PlaylistView(self.playlist)
        self.playlistView.video_list.doubleClicked.connect(self.playlistViewClicked)
        self.playlistView.closeButton.clicked.connect(self.showPlaylist)
        # self.playlistView.hide()

        # define a timeline list here
        self.timeline = Timeline()
        self.timeline.closeButton.clicked.connect(self.showTimeline)
        # self.timeline.hide()

        # adding the menu
        file_menu = self.ui.menubar.addMenu("&File")
        icon = QIcon.fromTheme("document-open")
        open_action = QAction(icon, "&Open...", self,
                              shortcut=QKeySequence.Open, triggered=self.open)
        file_menu.addAction(open_action)

        # adding the video widget
        self._video_widget = QVideoWidget(self)
        self._player.setVideoOutput(self._video_widget)
        self.ui.videoLayout.addWidget(self._video_widget)

        # controls trigger
        self.ui.playButton.clicked.connect(self.playPause)
        self.ui.stopButton.clicked.connect(self.stopPlayer) 
        self.ui.nextButton.clicked.connect(self.nextVideo)
        self.ui.previousButton.clicked.connect(self.previousVideo)
        self.ui.playlistButton.clicked.connect(self.showPlaylist)
        self.ui.timelineButton.clicked.connect(self.showTimeline)
        
        # volume slider
        volume = self._player.volume()
        self.ui.volumeSlider.setValue(volume)
        self.ui.volumeSlider.valueChanged.connect(self.setAudioVolume)

        # video progress
        self._player.durationChanged.connect(self.durationUpdate)
        self._player.positionChanged.connect(self.positionUpdate)
        self._player.stateChanged.connect(self.mediaStateChanged)

        self.video_slider = self.ui.videoSlider
        # self.video_slider.valueChanged.connect(lambda x : print(x))

        # color_ranges = [(55/100, 60/100, "#ffbf31")]
        # self.video_slider.setColorRanges(color_ranges)

    # open options currently only single files
    def open(self):
        home = str(Path.home())
        home_url = QUrl.fromLocalFile(home)
        file_filter = "Video Files (*.mp4 *.avi *.mkv *.mov *.wmv)"
        file_list, _ = QFileDialog.getOpenFileUrls(self, caption="Select video files", directory=home_url, filter=file_filter)
        file_contents = [QMediaContent(content) for content in file_list]

        self.playlist.addMedia(file_contents)
        
    # toggle play/pause
    def playPause(self):
        if self._player.state() == QMediaPlayer.PlayingState:
            self._player.pause()
        else:
            self._player.play()


    def mediaStateChanged(self, state):
        if self._player.state() == QMediaPlayer.PlayingState:
            self.ui.playButton.setIcon(QIcon(":/images/icons/play.png"))
        else:
            self.ui.playButton.setIcon(QIcon(":/images/icons/pause.png"))

    # stop player
    def stopPlayer(self):
        self.video_slider.reset()
        self._player.stop()

    # next player
    def nextVideo(self):
        print("Next")
        # self._player.stop()

    # next player
    def previousVideo(self):
        print("Previous")

    # change volume when change
    def setAudioVolume(self, value):
        self._player.setVolume(value)

    # videe progress update
    def durationUpdate(self, duration):
        self.video_slider.setMaximum(duration)
        if duration >= 0:
            self.ui.endTimeLabel.setText(self.convert_milliseconds(duration))

    def positionUpdate(self, pos):
        self.video_slider.blockSignals(True)
        self.video_slider.setValue(pos)
        self.video_slider.blockSignals(False)
        self.ui.startTimeLabel.setText(self.convert_milliseconds(pos))

    def showPlaylist(self):
        if self.playlistView.isVisible():
            self.playlistView.hide()
        else:
            self.playlistView.show()

    def showTimeline(self):
        if self.timeline.isVisible():
            self.timeline.hide()
        else:
            self.timeline.show()

    def _ensure_stopped(self):
        if self._player.state() != QMediaPlayer.StoppedState:
            self._player.stop()

    def hhmmss(self, ms):
        # s = 1000
        # m = 60000
        # h = 360000
        h, r = divmod(ms, 36000)
        m, r = divmod(r, 60000)
        s, _ = divmod(r, 1000)
        return ("%d:%02d:%02d" % (h,m,s)) if h else ("%d:%02d" % (m,s))
    
    def convert_milliseconds(self, ms):
        total_secs = ms // 1000
        # Convert total seconds to hours, minutes, and remaining seconds
        hours = total_secs // 3600
        mins = (total_secs % 3600) // 60
        secs = total_secs % 60
        
        # Use string formatting to ensure two digits for each unit of time
        return f"{hours:02d}:{mins:02d}:{secs:02d}"
        
    def playlistPositionChanged(self, index):
        if index > -1:
            self.playlistView.playlistPositionChanged(index)

    def playlistViewClicked(self):
        self._ensure_stopped()
        self.playlistView.itemClicked()

    def closeEvent(self, event) -> None:
        self._ensure_stopped()
        self._player.disconnect()
        self.playlistView.close()
        self.timeline.close()
        self.close()

    def showMinimized(self):
        self.playlistView.hide()
        self.timeline.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
