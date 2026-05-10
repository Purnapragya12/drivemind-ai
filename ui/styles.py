STYLE = """

QMainWindow {

    background-color: #020617;
}

QWidget {

    background-color: #020617;

    color: white;

    font-family: Segoe UI;
}

/* =========================
   GLASS PANELS
========================= */

QFrame {

    background-color: rgba(15, 23, 42, 220);

    border-radius: 28px;

    border: 1px solid rgba(255,255,255,0.06);
}

/* =========================
   TITLE
========================= */

#titleLabel {

    font-size: 68px;

    font-weight: 800;

    color: white;

    letter-spacing: 4px;
}

#subTitle {

    font-size: 20px;

    color: #94a3b8;
}

/* =========================
   METRIC CARDS
========================= */

#metricCard {

    background-color: rgba(255,255,255,0.03);

    border-radius: 24px;

    border: 1px solid rgba(255,255,255,0.05);

    padding: 20px;
}

#metricCard:hover {

    background-color: rgba(37,99,235,0.15);

    border: 1px solid rgba(59,130,246,0.35);
}

#metricTitle {

    color: #94a3b8;

    font-size: 15px;

    padding-bottom: 8px;
}

#metricValue {

    font-size: 34px;

    font-weight: bold;

    color: white;
}

/* =========================
   VIDEO PANEL
========================= */

#videoPanel {

    background-color: rgba(255,255,255,0.02);

    border-radius: 32px;

    border: 1px solid rgba(255,255,255,0.05);

    padding: 18px;
}

/* =========================
   CINEMATIC BUTTONS
========================= */

QPushButton {

    background-color:
    qlineargradient(
        x1:0,
        y1:0,
        x2:1,
        y2:1,
        stop:0 #2563eb,
        stop:1 #1d4ed8
    );

    color: white;

    border-radius: 24px;

    padding: 18px 34px;

    font-size: 18px;

    font-weight: 700;

    border: none;
}

QPushButton:hover {

    background-color:
    qlineargradient(
        x1:0,
        y1:0,
        x2:1,
        y2:1,
        stop:0 #3b82f6,
        stop:1 #2563eb
    );
}

QPushButton:pressed {

    padding-top: 20px;

    padding-left: 36px;

    background-color: #1e40af;
}

/* =========================
   SCROLLBAR
========================= */

QScrollBar:vertical {

    background: transparent;

    width: 10px;

    margin: 0px;
}

QScrollBar::handle:vertical {

    background: rgba(255,255,255,0.15);

    border-radius: 5px;

    min-height: 20px;
}

QScrollBar::handle:vertical:hover {

    background: rgba(59,130,246,0.5);
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical {

    height: 0px;
}

/* =========================
   LABELS
========================= */

QLabel {

    color: white;
}

"""