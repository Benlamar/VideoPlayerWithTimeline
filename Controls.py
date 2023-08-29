from PySide6.QtCore import Signal, QObject
from PySide6.QtWidgets import QWidget
from ControlsUI import Ui_Form
import helper

class Signals(QObject):
    seek_pos = Signal(int)


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
        self.video_slider.sliderPressed.connect(self.sliderSeekClicked)

        self.start_label = self.ui.startTimeLabel
        self.end_label = self.ui.endTimeLabel

        self.signal = Signals()

    def addTimeFrame(self, datas:list()):
        # print("Controls -->", data)
        # color_ranges = [(10000, 80000, "#ffbf31")]
        color_ranges = []

        for data in datas:
            start = int(data[0])/self.video_slider.maximum()
            end = int(data[1])/self.video_slider.maximum()
            timeframe = (start, end, data[2])
            color_ranges.append(timeframe)

        self.video_slider.setColorRanges(color_ranges)

        # self.timeline.addItemsToTimeline(url)
        # pass

    def sliderSeekClicked(self):
        clicked_position = self.video_slider.value()
        self.signal.seek_pos.emit(clicked_position)
        
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
        self.end_label.setText(helper.convert_milliseconds(duration))

    def changeStartLabel(self, pos):
        self.start_label.setText(helper.convert_milliseconds(pos))

