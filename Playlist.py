from PySide6.QtWidgets import QWidget, QStyledItemDelegate, QListView
from PySide6.QtCore import Qt, QSize, Signal, QObject, QUrl

from PlaylistUI import Ui_Playlist
from PlaylistModel import PlaylistModel

class Signals(QObject):
    play_signal = Signal(QUrl)

class CustomDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        # Set the desired height for each item
        height = 50  # Adjust the height as needed
        return QSize(option.rect.width(), height)

class Playlist(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Playlist()
        self.ui.setupUi(self)

        self.signal = Signals()

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlags(self.windowFlags() | Qt.Dialog | Qt.FramelessWindowHint)
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # QApplication.instance().applicationStateChanged.connect(self.handleStateChange)

        self.video_list : QListView = self.ui.listView
        self.video_list.doubleClicked.connect(self.itemClicked)
        self.video_list.setItemDelegate(CustomDelegate())

        self.playlist_model = PlaylistModel()
        
        self.ui.closeButton.clicked.connect(self.close)

    def addItemsToPlaylist(self, data):
        existing_data = self.playlist_model.getplaylist()

        for item in data:
            if item not in existing_data:
                existing_data.append(item)

        self.playlist_model.populateData(existing_data)
        self.video_list.setModel(self.playlist_model)

    def itemClicked(self):
        index = self.video_list.selectedIndexes()
        item_url = self.playlist_model.getURL(index[0].row())
        self.signal.play_signal.emit(item_url)
        
    def playlistPositionChanged(self, index):
        pos = self.model.index(index)
        self.video_list.setCurrentIndex(pos)

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