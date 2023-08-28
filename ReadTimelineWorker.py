from cgi import print_arguments
from PySide6.QtCore import QRunnable, Signal, QUrl, QObject
import os
import glob

FILE_TYPE = [".txt", '.json', '.csv']

class Signals(QObject):
    time_list = Signal(list)

class ReadTimelineWorker(QRunnable):
    def __init__(self, qurl:QUrl) -> None:
        super().__init__()
        self.url = qurl
        self.signal = Signals()
        self.setAutoDelete(True)
    
    def run(self) -> None:
        file_location = self.url.toLocalFile()
        folder = os.path.dirname(file_location)
        basename = os.path.splitext(os.path.basename(file_location))[0]

        read_file = ""
        data = []

        for file_type in FILE_TYPE:
            if glob.glob(f'{folder}/{basename}{file_type}'):
                read_file = folder+r"/"+basename+file_type
                break

        if read_file:
            with open(read_file, 'r') as f:
                data = [tuple(line.strip().split()) for line in f]

        if len(data):
            self.signal.time_list.emit(data)