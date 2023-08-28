from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
from PySide6.QtGui import QIcon

class TimeLineModel(QAbstractListModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._data = [1,2,34,75,125,200,500,520,600]

    def rowCount(self, parent=QModelIndex()):
         return len(self._data)
    
    
    def populateData(self,data):
        self._data = data

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._data[index.row()] # Display only the file name
        # if role == Qt.DecorationRole:
        #     return QIcon(":/images/icons/film.png")
        
        return None
    
    def getTimeline(self, index):
        if index < len(self._data):
            return self._data[index]