import sys

from PyQt6.QtWidgets import QApplication

from ui.main_window import DriveMindWindow


app = QApplication(sys.argv)

window = DriveMindWindow()

window.show()

sys.exit(app.exec())