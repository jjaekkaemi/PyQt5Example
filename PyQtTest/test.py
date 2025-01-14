import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5 import uic

# 상수 정의
FONT_PATH = "font/NanumGothic.ttf"
FONT_SIZE = 10
FONT_SIZE_TITLE = 14
LIST_ITEM_WIDTH = 730
LIST_ITEM_HEIGHT = 45
MAIN_UI_PATH = "ui/test4.ui"
CUSTOM_UI_PATH = "ui/custom_list_item.ui"
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType(MAIN_UI_PATH)[0]
custom_item_class = uic.loadUiType(CUSTOM_UI_PATH)[0]

class CustomListItem(QWidget, custom_item_class):
    def __init__(self, data, font):
        super().__init__()
        self.setupUi(self)
        self._init_ui(data, font)
        
    def _init_ui(self, data, font):
        # UI 요소 초기화
        self.index.setText(data["index"])
        self.type.setText(data["type"])
        self.type_detail.setText(data["type_detail"])
        self.status_code = data["status_code"]
        
        # 폰트 설정
        font_elements = [self.index, self.type, self.type_detail, 
                        self.result, self.result_detail, 
                        self.label_12, self.label_13]
        for element in font_elements:
            element.setFont(font)

    def set_status_style(self):
        status_styles = {
            0: ("정상", "#28a745"),
            1: ("비정상", "#dc3545")
        }
        status_text, bg_color = status_styles.get(self.status_code, ("알 수 없음", "#gray"))
        self.result.setText(status_text)
        self.result.setStyleSheet(f"background-color: {bg_color};")

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.custom_font = self._setup_font()
        self._init_ui()
        self._populate_list()

    def _setup_font(self):
        """폰트 설정 및 반환"""
        font_id = QFontDatabase.addApplicationFont(FONT_PATH)
        if font_id == -1:
            print("Failed to load font")
            return QFont()
        
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        print(f"Loaded font: {font_family}")
        return QFont(font_family, FONT_SIZE)

    def _init_ui(self):
        """UI 요소 초기화"""
        font_family = self.custom_font.family()
        
        # 타이틀 폰트 설정
        self.title.setFont(QFont(font_family, FONT_SIZE_TITLE))
        
        # 일반 폰트 설정
        ui_elements = [
            self.title_no_sent, self.value_no_sent, 
            self.title_detail, self.detail_btn,
            self.label_6, self.label_4, self.index,
            self.type, self.type_detail, self.result,
            self.result_detail, self.label_12, self.label_13
        ]
        for element in ui_elements:
            element.setFont(self.custom_font)

    def _populate_list(self):
        """리스트 위젯에 아이템 추가"""
        for i in range(50):
            data = {
                "index": f"{i+1}",
                "type": "계량값",
                "type_detail": "계근값",
                "status_code": i % 2,
            }
            self.add_custom_item(data)

    def add_custom_item(self, data):
        """커스텀 아이템을 리스트에 추가"""
        custom_item_widget = CustomListItem(data, self.custom_font)
        custom_item_widget.set_status_style()

        list_item = QListWidgetItem(self.listWidget)
        list_item.setSizeHint(QSize(LIST_ITEM_WIDTH, LIST_ITEM_HEIGHT))
        
        self.listWidget.addItem(list_item)
        self.listWidget.setItemWidget(list_item, custom_item_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()