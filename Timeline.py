from PySide6.QtWidgets import QWidget, QStyledItemDelegate, QListView
from PySide6.QtCore import Qt,  QSize
from TimelineUI import Ui_TimelineNavigator

from TimeLineModel import TimeLineModel

class CustomDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        # Set the desired height for each item
        height = 50  # Adjust the height as needed
        return QSize(option.rect.width(), height)


class Timeline(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_TimelineNavigator()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.timeline_list = self.ui.listView
        self.timeline_list.clicked.connect(self.itemClicked)
        self.timeline_list.setItemDelegate(CustomDelegate())

        self.tl_model = TimeLineModel()
        self.timeline_list.setModel(self.tl_model)

        self.ui.closeButton.clicked.connect(self.close)

    def itemClicked(self):
        index = self.timeline_list.selectedIndexes()
        item = self.tl_model.getTimeline(index[0].row())
        print(item)

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