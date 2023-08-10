from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
from PySide6.QtGui import QIcon


class PlaylistModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._data = []

    def getplaylist(self):
        return self._data

    def populateData(self,data):
        self._data = data

    def rowCount(self, parent=QModelIndex()):
         return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            url = self._data[index.row()]
            return url.fileName()  # Display only the file name

        if role == Qt.DecorationRole:
            return QIcon(":/images/icons/film.png")
        
        return None
    
    def getURL(self, index):
        return self._data[index]