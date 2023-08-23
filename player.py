from PySide6.QtCore import (Slot, QUrl)
from PySide6.QtGui import (QAction, QIcon, QKeySequence)
from PySide6.QtWidgets import (QApplication, QMainWindow, QDialog, QFileDialog)
from time import sleep

# multi media module
from PySide6.QtMultimedia import (QAudio, QAudioOutput, QMediaPlayer)
from PySide6.QtMultimediaWidgets import QVideoWidget

# from Main import Ui_MainWindow
from Main import Ui_mainWindow
from Playlist import Playlist
from Timeline import Timeline

import sys
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()
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

        # controls trigger
        self.ui.playButton.clicked.connect(self.playPause)
        self.ui.stopButton.clicked.connect(self.ensureStopped) 
        self.ui.nextButton.clicked.connect(self.nextVideo)
        self.ui.previousButton.clicked.connect(self.previousVideo)
        self.ui.playlistButton.clicked.connect(self.showPlaylist)
        self.ui.timelineButton.clicked.connect(self.showTimeline)
        
        # volume slider
        volume = self._audio_output.volume() * 100
        self.ui.volumeSlider.setValue(volume)
        self.ui.volumeSlider.valueChanged.connect(self.setAudioVolume)

        # video progress
        self._player.durationChanged.connect(self.durationUpdate)
        self._player.positionChanged.connect(self.positionUpdate)

        self.video_slider = self.ui.videoSlider

        # adding the video widget
        self._video_widget = QVideoWidget()
        self._player.setVideoOutput(self._video_widget)
        self.ui.videoLayout.addWidget(self._video_widget)

        system_palette = self.palette()
        highlight = system_palette.alternateBase()
        # print(highlight.color().getRgb(), type(highlight.color().getRgb()))

        # playlist
        self.playlist = Playlist()
        self.playlist.signal.play_signal.connect(self.playnow)
        self.playlist.signal.stop_signal.connect(self.ensureStopped)
        # timeline
        self.timeline = Timeline()

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
        self.timeline.addItemsToTimeline(url)

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
        # print("State",current_state)
        if current_state == QMediaPlayer.PlayingState:
            icon = u":/images/icons/pause.png"
        elif current_state == QMediaPlayer.PausedState:
            icon = u":/images/icons/play.png"
        elif current_state == QMediaPlayer.StoppedState:
            icon = u":/images/icons/play.png"
        self.ui.playButton.setIcon(QIcon(icon))

    # next player
    def nextVideo(self):
        self.playlist.playNext()

    # next player
    def previousVideo(self):
        self.playlist.playPrevious()

    # change volume when change
    def setAudioVolume(self, value):
        self._audio_output.setVolume(value/100)

    # videe progress update
    def durationUpdate(self, duration):
        if duration >= 0:
            self.ui.endTimeLabel.setText(self.convert_milliseconds(duration))
        if duration > 0:
            self.video_slider.setMaximum(duration)


    def positionUpdate(self, pos):
        # print("Position ",pos)
        self.video_slider.blockSignals(True)
        self.video_slider.setValue(pos)
        self.video_slider.blockSignals(False)
        self.ui.startTimeLabel.setText(self.convert_milliseconds(pos))

    def hhmmss(self, ms):
        # s = 1000, # m = 60000, # h = 360000
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
            h ="hello"

    def ensureStopped(self):
        if self._player.playbackState() != QMediaPlayer.StoppedState:
            self._player.stop()
            # self._player.disconnect()
            self.video_slider.reset()
            self.handleStateChange(self._player.playbackState())
            print("ensure stoped ran")

    def closeEvent(self, event) -> None:
        self.ensureStopped()
        self.playlist.close()
        self.timeline.close()
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
