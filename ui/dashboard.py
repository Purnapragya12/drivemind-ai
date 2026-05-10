import cv2

from PyQt6.QtWidgets import (

    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog,
    QScrollArea,
    QFrame

)

from PyQt6.QtCore import (

    Qt,
    QTimer

)

from PyQt6.QtGui import (

    QImage,
    QPixmap,
    QMovie

)

from vision.video_adas import (
    VideoADAS
)

from ui.widgets import (
    MetricCard
)


class Dashboard(QWidget):

    def __init__(self):

        super().__init__()

        self.adas = VideoADAS()

        self.cap = None

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_frame
        )

        self.setup_ui()

    # =====================================
    # UI
    # =====================================

    def setup_ui(self):

        outer_layout = QVBoxLayout()

        outer_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        # =====================================
        # SCROLL AREA
        # =====================================

        scroll = QScrollArea()

        scroll.setWidgetResizable(True)

        scroll.setStyleSheet("""

        QScrollArea {

            border: none;

        }

        """)

        container = QWidget()

        self.main_layout = QVBoxLayout()

        self.main_layout.setSpacing(18)

        self.main_layout.setContentsMargins(
            24,
            24,
            24,
            24
        )

        dashboard_title = QLabel(
            "ADAS CONTROL CENTER"
        )

        dashboard_title.setStyleSheet("""

        font-size: 42px;

        font-weight: 800;

        color: white;

        padding-bottom: 10px;

        """)

        dashboard_subtitle = QLabel(
            "Simulation-grade autonomous driving perception interface"
        )

        dashboard_subtitle.setStyleSheet("""

        font-size: 18px;

        color: #94a3b8;

        padding-bottom: 20px;

        """)

        self.main_layout.addWidget(
            dashboard_title
        )

        self.main_layout.addWidget(
            dashboard_subtitle
        )

        # =====================================
        # METRICS
        # =====================================

        metrics_layout = QHBoxLayout()

        metrics_layout.setSpacing(12)

        metrics_layout.addWidget(

            MetricCard(
                "Lane Assist",
                "ACTIVE"
            )
        )

        metrics_layout.addWidget(

            MetricCard(
                "FCW",
                "ONLINE"
            )
        )

        metrics_layout.addWidget(

            MetricCard(
                "AI Vision",
                "LIVE"
            )
        )

        metrics_layout.addWidget(

            MetricCard(
                "Autonomy",
                "LEVEL 2"
            )
        )

        self.main_layout.addLayout(
            metrics_layout
        )

        # =====================================
        # VIDEO FRAME
        # =====================================

        self.video_frame = QLabel()
        self.video_frame.setObjectName(
            "videoPanel"
        )

        self.video_frame.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        self.video_frame.setMinimumHeight(
            620
        )

        self.video_frame.setMaximumHeight(
            700
        )

        self.video_frame.setStyleSheet("""

        QLabel {

            border-radius: 28px;

            background-color: #020617;

            border:
            1px solid rgba(255,255,255,0.06);

            padding: 12px;
        }

        """)

        self.main_layout.addWidget(
            self.video_frame
        )

        # =====================================
        # UPLOAD BUTTON
        # =====================================

        upload_layout = QHBoxLayout()

        self.upload_btn = QPushButton(
            "UPLOAD DRIVING FOOTAGE"
        )

        self.upload_btn.setMinimumHeight(
            65
        )

        self.upload_btn.clicked.connect(
            self.open_video
        )

        upload_layout.addWidget(
            self.upload_btn
        )

        self.main_layout.addLayout(
            upload_layout
        )

        container.setLayout(
            self.main_layout
        )

        scroll.setWidget(container)

        outer_layout.addWidget(scroll)

        self.setLayout(outer_layout)

    # =====================================
    # START SYSTEM
    # =====================================

    def start_system(self):

        self.start_btn.setText(
            "SYSTEM ONLINE"
        )

    # =====================================
    # VIDEO UPLOAD
    # =====================================

    def open_video(self):

        path, _ = QFileDialog.getOpenFileName(

            self,

            "Open Video",

            "",

            "Video Files (*.mp4 *.avi)"
        )

        if path:

            self.cap = cv2.VideoCapture(
                path
            )

            self.timer.start(30)

    # =====================================
    # FRAME UPDATE
    # =====================================

    def update_frame(self):

        if self.cap is None:

            return

        success, frame = self.cap.read()

        if not success:

            self.cap.set(
                cv2.CAP_PROP_POS_FRAMES,
                0
            )

            return

        frame = cv2.resize(

            frame,

            (1180, 620)
        )

        processed = self.adas.process(
            frame
        )

        rgb = cv2.cvtColor(

            processed,

            cv2.COLOR_BGR2RGB
        )

        h, w, ch = rgb.shape

        bytes_per_line = ch * w

        qt_image = QImage(

            rgb.data,

            w,

            h,

            bytes_per_line,

            QImage.Format.Format_RGB888
        )

        pixmap = QPixmap.fromImage(
            qt_image
        )

        self.video_frame.setPixmap(
            pixmap
        )