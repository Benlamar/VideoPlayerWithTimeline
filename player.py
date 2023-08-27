from PySide6.QtCore import (Slot, QUrl)
from PySide6.QtWidgets import (QMainWindow, QFileDialog)
from PySide6.QtGui import (QAction, QIcon, QKeySequence)
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget

from PlayerUI import Ui_mainWindow
from Playlist import Playlist
from Timeline import Timeline

from Controls import Controls

from time import sleep
from pathlib import Path

class Player(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # player components
        self.video_widget = self.ui.videoWidget

        # add controls UI to ToolBar
        self.control_toolbar = self.ui.ControlBar
        self.controls = Controls()
        self.controls.setParent(self.control_toolbar)
        self.control_toolbar.addWidget(self.controls)

        # control components
        self.volume_slider = self.controls.volume_slider
                        
        # controls trigger
        self.controls.play_pause.clicked.connect(self.playPause)
        self.controls.stop.clicked.connect(self.ensureStopped) 
        self.controls.next.clicked.connect(self.nextVideo)
        self.controls.previous.clicked.connect(self.previousVideo)
        self.controls.playlist_but.clicked.connect(self.showPlaylist)
        self.controls.timeline_but.clicked.connect(self.showTimeline)
        
        self.setupMenu()
        self.initializePlayer()
        
        # playlist
        self.playlist = Playlist()
        self.playlist.signal.play_signal.connect(self.playnow)
        self.playlist.signal.stop_signal.connect(self.ensureStopped)
        
        # timeline
        self.timeline = Timeline()

    def initializePlayer(self):
        # audio connections
        self._audio_output = QAudioOutput()
        self._player = QMediaPlayer()
        self._player.setAudioOutput(self._audio_output)

        # setup video player
        self._player.setVideoOutput(self.video_widget)

        # volume slider
        volume = self._audio_output.volume() * 100
        self.volume_slider.setValue(volume)
        self.volume_slider.valueChanged.connect(self.setAudioVolume)

        # video progress
        self._player.durationChanged.connect(self.durationUpdate)
        self._player.positionChanged.connect(self.positionUpdate)

    def setupMenu(self):
         # adding the menu
        file_menu = self.ui.menubar.addMenu("&File")
        icon = QIcon.fromTheme("document-open")
        open_action = QAction(icon, "&Open...", self,
                              shortcut=QKeySequence.Open, triggered=self.open)
        file_menu.addAction(open_action)

    # open options currently only single files
    @Slot()
    def open(self):
        home = str(Path.home())
        home_url = QUrl.fromLocalFile(home)
        file_filter = "Supported Files (*.mp4 *.avi *.mkv *.mov *.wmv)"
        file_list, _ = QFileDialog.getOpenFileUrls(self, caption="Select video files", dir=home_url, filter=file_filter)
        
        if len(file_list):
            self.ensureStopped()
            self.playlist.addItemsToPlaylist(file_list)

    def playnow(self, url):        
        self.ensureStopped()
        sleep(0.3)
        
        # color_ranges = [(55/100, 60/100, "#ffbf31")]
        # self.video_slider.setColorRanges(color_ranges)
        # self.timeline.addItemsToTimeline(url)

        self._player.setSource(url)
        self._player.play()
        
        self.handleStateChange(self._player.playbackState())

    # toggle play/pause
    def playPause(self):
        if self._player.playbackState() == QMediaPlayer.PlayingState:
            self._player.pause()
        elif self._player.playbackState() == QMediaPlayer.PausedState:
            self._player.play()
        elif self._player.playbackState() == QMediaPlayer.StoppedState:
            self.playlist.play()
        
        self.handleStateChange(self._player.playbackState())

    def handleStateChange(self, current_state):
        if current_state == QMediaPlayer.PlayingState:
            icon = u":/images/icons/pause.png"
        elif current_state == QMediaPlayer.PausedState:
            icon = u":/images/icons/play.png"
        elif current_state == QMediaPlayer.StoppedState:
            icon = u":/images/icons/play.png"
        self.controls.play_pause.setIcon(QIcon(icon))

    # next player
    def nextVideo(self):
        self.playlist.playNext()

    # next player
    def previousVideo(self):
        self.playlist.playPrevious()

    # change volume when change
    def setAudioVolume(self, value):
        self._audio_output.setVolume(value/100)

    # video total duraion is received here
    def durationUpdate(self, duration):
        self.controls.setVideoSliderDuration(duration)

    # receives the current position of the video player
    def positionUpdate(self, pos):
        self.controls.updateVideoSlider(pos)

    def showPlaylist(self):
        if self.playlist.isVisible():
            self.playlist.hide()
        else:
            self.playlist.show()
            self.playlist.raise_()

    def showTimeline(self):
        if self.timeline.isVisible():
            self.timeline.hide()
        else:
            self.timeline.show()

    def ensureStopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()
            self.controls.resetVideoSlider()
            self.handleStateChange(self._player.playbackState())
            print("ensure stoped ran")

    def closeEvent(self, event) -> None:
        self.ensureStopped()
        self.playlist.close()
        self.timeline.close()
        self.close()