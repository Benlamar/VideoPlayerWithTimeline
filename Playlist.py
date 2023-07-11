from PySide6.QtWidgets import QWidget
from PlaylistUI import Ui_Playlist

class Playlist(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_Playlist()
        self.ui.setupUi(self)