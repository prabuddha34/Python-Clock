import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
)
from PyQt5.QtCore import QTimer, QTime, Qt

class Digital(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size: 30px;")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # update every 1 second

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = Digital()
    clock.show()
    sys.exit(app.exec_())
