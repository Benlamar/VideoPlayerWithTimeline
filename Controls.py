from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import QWidget
from ControlsUI import Ui_Form


class Controls(QWidget):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.play_pause = self.ui.playButton
        self.stop = self.ui.stopButton
        self.previous = self.ui.previousButton
        self.next = self.ui.nextButton
        self.playlist_but = self.ui.playlistButton
        self.timeline_but = self.ui.timelineButton

        self.volume_slider = self.ui.volumeSlider
        self.video_slider = self.ui.videoSlider
        self.video_slider.sliderPressed.connect(self.seekVideo)

        self.start_label = self.ui.startTimeLabel
        self.end_label = self.ui.endTimeLabel

    def seekVideo(self):
        clicked_position = self.video_slider.value()
        print(clicked_position)

    def resetVideoSlider(self):
        self.video_slider.reset()

    def setVideoSliderDuration(self, duration):
        if duration > 0:
            self.video_slider.setMaximum(duration)
            self.changeEndLabel(duration)

    # def setVolumeSlider(self, value):
    #     self.volume_slider.setValue(value)

    # def updateVolumeSlider(self, value):
    #     self.volume_slider.valueChanged.connect(self.setAudioVolume)

    def updateVideoSlider(self, pos):
        self.video_slider.blockSignals(True)
        self.video_slider.setValue(pos)
        self.video_slider.blockSignals(False)
        self.changeStartLabel(pos)

    def changeEndLabel(self, duration):
        self.end_label.setText(self.convert_milliseconds(duration))

    def changeStartLabel(self, pos):
        self.start_label.setText(self.convert_milliseconds(pos))

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