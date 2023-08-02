from PySide6.QtWidgets import QFileDialog
from pathlib import Path

home = str(Path.home())
file_extensions = [
    "*.mpg", "*.mov", "*.wmv", "*.rm", "*.avi", "*.flv", "*.mkv", "*.mp4",
    "*.webm", "*.ogv", "*.m4v", "*.3gp", "*.asf", "*.vob", "*.ts", "*.mts",
    "*.m2ts"
]
filters = "Video Files (" + " ".join(file_extensions) + ")"
file_dialog = QFileDialog.getOpenFileUrls(self, dir=home, caption="Select Video Files", filter=filters)
print(file_dialog)
