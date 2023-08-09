from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from TimelineUI import Ui_TimelineNavigator

class Timeline(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_TimelineNavigator()
        self.ui.setupUi(self)
        
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.closeButton = self.ui.closeButton


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event):
        if self.dragging:
            self.move(self.pos() + event.pos() - self.offset)
    
    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Clear dragging flag
            self.dragging = False