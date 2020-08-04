from PyQt5.QtGui import QFont

### Font family ###
font_content = QFont()
font_content.setFamily("Helvetica Neue")
font_content.setPointSize(12)

font_title = QFont()
font_title.setFamily("Helvetica Neue")
font_title.setPointSize(14)
font_title.setBold(True)
font_title.setWeight(75)

### Style sheet ###
style_blank = "background-color: rgb(255, 255, 255); selection-background-color: lightblue; selection-color: black;"
style_background = "color: black; background-color: rgb(219, 223, 226);"

style_round_btn = "border-radius: 10px; border: 2px solid rgba(190, 190, 190, 0.5);"
style_round_box = "border-radius: 4px; border: 1px solid rgb(190, 190, 190);"

style_btn = "background-color: rgb(252, 252, 252);" # Yellow
style_btn_pressed = "QPushButton { "+style_btn+style_round_btn+" }\nQPushButton:pressed { background-color: rgb(47, 52, 55); color: white; }"

style_list = style_blank+style_round_box
style_list_selected = "QListWidget { "+style_list+" }\nQListWidget::item:selected { background-color: rgb(47, 52, 55); color: white; }"

style_slidebar = """
        QScrollBar:vertical {              
            border: none;
            background:white;
            width:3px;
            margin: 0px 0px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));
            min-height: 0px;
        }
        QScrollBar::add-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
            height: 0 px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }
    """

style_combobox = """
    QComboBox{
        background-color: white;
        selection-background-color: lightblue;
        border-radius: 4px; border: 1px solid rgb(190, 190, 190);
        padding: 1px 12px;
    }
    QComboBox::drop-down {
        border-top-right-radius: 4px;
        border-bottom-right-radius: 4px;
    }
    QComboBox QAbstractItemView {
        background-color: lightgray;
        border-radius: 4px; border: 1px solid rgb(190, 190, 190);
    }
    """
