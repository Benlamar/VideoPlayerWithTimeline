from PyQt5.QtWidgets import QWidget, QStyledItemDelegate
from PyQt5.QtCore import QSize, Qt

from PlaylistUI import Ui_Playlist
from PlaylistModel import PlaylistModel
from PyQt5.QtMultimedia import QMediaPlaylist

class CustomDelegate(QStyledItemDelegate):
    def sizeHint(self, option, index):
        # Set the desired height for each item
        height = 50  # Adjust the height as needed
        return QSize(option.rect.width(), height)

class PlaylistView(QWidget):
    def __init__(self, playlist : QMediaPlaylist, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Playlist()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        self.video_list = self.ui.listView
        self.video_list.setItemDelegate(CustomDelegate())

        self.playlist = playlist
        self.model = PlaylistModel(self.playlist)
        self.video_list.setModel(self.model)

        self.ui.closeButton.clicked.connect(self.hide)

    def itemClicked(self):
        indexes = self.video_list.selectedIndexes()
        for index in indexes:
            self.playlist.setCurrentIndex(index.row())

    def playlistPositionChanged(self, index):
        pos = self.model.index(index)
        self.video_list.setCurrentIndex(pos)
