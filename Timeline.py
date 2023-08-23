from PySide6.QtWidgets import QWidget, QStyledItemDelegate, QListView
from PySide6.QtCore import Qt,  QSize, QUrl
from TimelineUI import Ui_TimelineNavigator
import os

from TimeLineModel import TimeLineModel

class CustomDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        # Set the desired height for each item
        height = 30  # Adjust the height as needed
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

    def readTimeStamp(self, file_path):
        # incomplete
        with open(file_path,'r') as r:
            data = r.read()
            return data

    def addItemsToTimeline(self, file_url:QUrl):
        file_location = file_url.toLocalFile()
        print(file_location)
        basename = os.path.basename(file_location)
        folder = os.path.dirname(file_location)
        file_split = basename.split(".")
        file_timestamp = file_split[0]+".txt"

        timestamp_path = os.path.join(folder, file_timestamp)

        try:
            if os.path.exists(timestamp_path):
                print(self.readTimeStamp(timestamp_path))
            else:
                print("Timestamp file do not exist")
        except Exception as ex:
            print(ex)
                

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