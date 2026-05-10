from PyQt6.QtWidgets import (

    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton

)

from PyQt6.QtCore import (

    Qt,
    pyqtSignal

)


class BootScreen(QWidget):

    start_clicked = pyqtSignal()

    def __init__(self):

        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        self.setStyleSheet("""

        QWidget {

            background-color: #020617;
        }

        """)

        layout = QVBoxLayout()

        layout.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.setSpacing(30)

        # ===============================
        # TOP LABEL
        # ===============================

        label = QLabel(
            "AUTONOMOUS DRIVING INTELLIGENCE"
        )

        label.setStyleSheet("""

        font-size: 18px;

        letter-spacing: 6px;

        color: #3b82f6;

        font-weight: bold;

        """)

        # ===============================
        # MAIN TITLE
        # ===============================

        title = QLabel(
            "DRIVEMIND AI"
        )

        title.setStyleSheet("""

        font-size: 110px;

        font-weight: 900;

        color: white;

        letter-spacing: 5px;

        """)

        # ===============================
        # SUBTITLE
        # ===============================

        subtitle = QLabel(
            "by Purnapragya Sinha"
        )

        subtitle.setStyleSheet("""

        font-size: 24px;

        color: rgba(255,255,255,0.45);

        """)

        # ===============================
        # BUTTON
        # ===============================

        start_btn = QPushButton(
            "INITIALIZE SYSTEM"
        )

        start_btn.setMinimumWidth(
            340
        )

        start_btn.setMinimumHeight(
            90
        )

        start_btn.clicked.connect(
            self.start_clicked.emit
        )

        # ===============================
        # ADD
        # ===============================

        layout.addWidget(
            label,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            title,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            subtitle,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        layout.addSpacing(40)

        layout.addWidget(
            start_btn,
            alignment=Qt.AlignmentFlag.AlignCenter
        )

        self.setLayout(layout)