from PyQt6.QtWidgets import (

    QMainWindow,
    QStackedWidget

)

from ui.boot_screen import (
    BootScreen
)

from ui.loading_screen import (
    LoadingScreen
)

from ui.dashboard import (
    Dashboard
)

from ui.styles import STYLE


class DriveMindWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "DriveMind AI"
        )

        self.resize(
            1600,
            950
        )

        self.setStyleSheet(
            STYLE
        )

        # ==================================
        # STACK
        # ==================================

        self.stack = QStackedWidget()

        self.setCentralWidget(
            self.stack
        )

        # ==================================
        # SCREENS
        # ==================================

        self.boot = BootScreen()

        self.loading = LoadingScreen()

        self.dashboard = Dashboard()

        self.stack.addWidget(
            self.boot
        )

        self.stack.addWidget(
            self.loading
        )

        self.stack.addWidget(
            self.dashboard
        )

        # ==================================
        # CONNECT FLOW
        # ==================================

        self.boot.start_clicked.connect(
            self.show_loading
        )

        self.loading.finished.connect(
            self.show_dashboard
        )

        self.stack.setCurrentWidget(
            self.boot
        )

    # ==================================
    # SHOW LOADING
    # ==================================

    def show_loading(self):

        self.stack.setCurrentWidget(
            self.loading
        )

        self.loading.start_loading()

    # ==================================
    # SHOW DASHBOARD
    # ==================================

    def show_dashboard(self):

        self.stack.setCurrentWidget(
            self.dashboard
        )