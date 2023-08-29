from PySide6.QtCore import QAbstractListModel, Qt, QModelIndex
from PySide6.QtGui import QIcon
import helper


class TimeLineModel(QAbstractListModel):
    def __init__(self, data=[], parent=None):
        super().__init__(parent)
        self._data = data

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if len(self._data):
                start, end = helper.convert_milliseconds(
                    self._data[index.row()][0]
                ), helper.convert_milliseconds(self._data[index.row()][1])

                return str(start) + " - " + str(end)  # Display only the file name

        # if role == Qt.DecorationRole:
        #     return QIcon(":/images/icons/film.png")
        return None

    def getTimeline(self, index):
        if index < len(self._data):
            return self._data[index]
