from typing import Optional, Union
from PyQt5.QtCore import QAbstractListModel, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimedia import QMediaPlaylist


class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist : QMediaPlaylist, parent=None):
        super().__init__(parent)
        self.playlist = playlist

    def rowCount(self, parent=None):
        return self.playlist.mediaCount()

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            data = self.playlist.media(index.row())
            return data.canonicalUrl().fileName()
        
        if role == Qt.DecorationRole:
            return QIcon(":/images/icons/film.png")

        return None
        
    