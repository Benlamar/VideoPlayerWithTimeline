from PySide6.QtWidgets import QWidget
from TimelineUI import Ui_TimelineNavigator

class Timeline(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.ui = Ui_TimelineNavigator()
        self.ui.setupUi(self)