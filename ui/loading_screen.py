from PyQt6.QtWidgets import (

    QWidget,
    QVBoxLayout,
    QLabel,
    QProgressBar

)

from PyQt6.QtCore import (

    Qt,
    QTimer,
    pyqtSignal

)


class LoadingScreen(QWidget):

    finished = pyqtSignal()

    def __init__(self):

        super().__init__()

        self.progress = 0

        self.setup_ui()

    def setup_ui(self):

        self.setStyleSheet("""

        QWidget {

            background-color: #020617;

            color: white;
        }

        QProgressBar {

            border: none;

            height: 28px;

            background-color: rgba(255,255,255,0.05);

            border-radius: 14px;

            text-align: center;

            font-size: 14px;

        }

        QProgressBar::chunk {

            border-radius: 14px;

            background-color: #2563eb;
        }

        """)

        layout = QVBoxLayout()

        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.setSpacing(28)

        self.title = QLabel(
            "INITIALIZING DRIVE SYSTEM"
        )

        self.title.setStyleSheet("""

        font-size: 56px;

        font-weight: bold;

        """)

        self.status = QLabel(
            "Starting..."
        )

        self.status.setStyleSheet("""

        font-size: 24px;

        color: #94a3b8;

        """)

        self.progressbar = QProgressBar()

        self.progressbar.setMinimumWidth(
            700
        )

        self.progressbar.setMaximum(
            100
        )

        layout.addWidget(
            self.title,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            self.status,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addSpacing(20)

        layout.addWidget(
            self.progressbar
        )

        self.setLayout(layout)

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_progress
        )

    # ==================================
    # START
    # ==================================

    def start_loading(self):

        self.progress = 0

        self.timer.start(45)

    # ==================================
    # UPDATE
    # ==================================

    def update_progress(self):

        self.progress += 1

        self.progressbar.setValue(
            self.progress
        )

        if self.progress < 20:

            text = (
                "Initializing Neural Vision..."
            )

        elif self.progress < 40:

            text = (
                "Starting Collision Engine..."
            )

        elif self.progress < 60:

            text = (
                "Calibrating Lane Assist..."
            )

        elif self.progress < 80:

            text = (
                "Loading Perception Stack..."
            )

        else:

            text = (
                "System Online"
            )

        self.status.setText(text)

        if self.progress >= 100:

            self.timer.stop()

            self.finished.emit()