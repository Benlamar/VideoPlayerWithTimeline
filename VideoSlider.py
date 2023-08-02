from PyQt5.QtWidgets import QSlider, QStyle, QStyleOptionSlider
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QPainter, QColor, QLinearGradient, QPainterPath

class VideoSlider(QSlider):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.color_ranges = []
        self.original_state = {
            'range': (self.minimum(), self.maximum()),
            'value': self.value(),
        }

    def setColorRanges(self, color_ranges):
        self.color_ranges = color_ranges
        self.update()

    def paintEvent(self, event):
        with QPainter(self) as painter:
            painter.setRenderHint(QPainter.Antialiasing)

            groove_rect = self.style().subControlRect(
                QStyle.CC_Slider, self.styleOptionSlider(), QStyle.SC_SliderGroove, self
            )

            # Adjust groove height and position
            groove_rect.setHeight(8)
            groove_rect.moveCenter(self.rect().center())

            # Draw default groove
            painter.setPen(Qt.NoPen)
            painter.setBrush(self.palette().color(self.backgroundRole()))
            painter.drawRoundedRect(groove_rect,4, 4)

            # Draw completed part
            completed_rect = QRect(
                groove_rect.x(),
                groove_rect.y(),
                groove_rect.width() * self.sliderPosition() / self.maximum(),
                groove_rect.height(),
            )
            # Set color
            # Create a linear gradient color
            painter.setBrush(QColor("#5e59ff"))
            painter.drawRoundedRect(completed_rect, 4, 4)

            # print(groove_rect.x(), groove_rect.y(), groove_rect.width())
            # Draw color ranges
            for start, end, color in self.color_ranges:
                color_rect = QRect(
                    groove_rect.x() + groove_rect.width() * start,
                    groove_rect.y(),
                    groove_rect.width() * (end - start),
                    groove_rect.height(),
                )

                painter.setBrush(QColor(color))              
            
                painter.setBrush(QColor(color))
                painter.drawRect(color_rect)


            # Draw handle
            handle_rect = self.style().subControlRect(
                QStyle.CC_Slider, self.styleOptionSlider(), QStyle.SC_SliderHandle, self
            )
            handle_rect.moveCenter(QPoint(groove_rect.x(), groove_rect.y()+(groove_rect.height()-2.6))) #groove_rect.center()
            # handle_rect.moveCenter(groove_rect.center()) #groove_rect.center()
            handle_position = groove_rect.left() + groove_rect.width() * self.sliderPosition() / self.maximum() - handle_rect.width() / 2
            handle_rect.moveLeft(max(groove_rect.left(), min(handle_position, groove_rect.right() - (handle_rect.width())))-0.5)
            painter.setBrush(self.palette().color(self.foregroundRole()))
            painter.setPen(Qt.NoPen)

            # Set the width and height of the handle_rect to be equal
            factor = 0.8
            handle_rect.setWidth(int(handle_rect.height() * factor))
            handle_rect.setHeight(int(handle_rect.height() * factor))

            painter.drawEllipse(handle_rect)

    def styleOptionSlider(self):
        option = QStyleOptionSlider()
        option.initFrom(self)
        option.orientation = self.orientation()
        option.minimum = self.minimum()
        option.maximum = self.maximum()
        option.sliderPosition = self.sliderPosition()
        option.sliderValue = self.value()
        option.singleStep = self.singleStep()
        option.pageStep = self.pageStep()
        option.upsideDown = self.invertedAppearance()
        option.invertedAppearance = self.invertedControls()
        option.activeSubControls = QStyle.SC_None
        option.tickPosition = self.tickPosition()
        option.tickInterval = self.tickInterval()
        return option
    
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            opt = QStyleOptionSlider()
            self.initStyleOption(opt)
            groove_rect = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderGroove, self)
            handle_rect = self.style().subControlRect(QStyle.CC_Slider, opt, QStyle.SC_SliderHandle, self)

            slider_length = handle_rect.width()
            slider_min = groove_rect.x()
            slider_max = groove_rect.right() - slider_length + 1

            pr = event.pos() - handle_rect.center() + handle_rect.topLeft()
            p = pr.x()
            new_position = QStyle.sliderValueFromPosition(self.minimum(), self.maximum(), p - slider_min, slider_max - slider_min, opt.upsideDown)

            self.setSliderPosition(new_position)

        super().mousePressEvent(event)

    def reset(self):
         # Reset to original state
        self.setRange(*self.original_state['range'])
        self.setValue(self.original_state['value'])

        # Clear color_ranges
        self.color_ranges = []
        self.update()