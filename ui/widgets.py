from PyQt6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel
)

from PyQt6.QtCore import Qt


class MetricCard(QFrame):

    def __init__(
        self,
        title,
        value
    ):

        super().__init__()

        self.setObjectName(
            "metricCard"
        )

        layout = QVBoxLayout()

        layout.setSpacing(6)

        title_label = QLabel(title)

        title_label.setObjectName(
            "metricTitle"
        )

        value_label = QLabel(value)

        value_label.setObjectName(
            "metricValue"
        )

        value_label.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        layout.addWidget(
            title_label
        )

        layout.addWidget(
            value_label
        )

        self.setLayout(layout)