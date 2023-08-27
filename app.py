from PySide6.QtWidgets import QApplication
from Player import Player

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Player()
    window.show()
    sys.exit(app.exec())