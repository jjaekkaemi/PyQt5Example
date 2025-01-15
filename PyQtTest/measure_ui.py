from PyQt5.QtWidgets import QMainWindow, QDialog, QVBoxLayout, QLabel, QProgressBar, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5 import uic

# 상수 정의
UI_PATH = "ui/test2.ui"
FONT_SRC = "font/NanumGothic.ttf"
FONT_BOLD_SRC = "font/NanumGothicExtraBold.ttf"

# 폰트 크기 상수
FONT_SIZE_LARGE = 14
FONT_SIZE_MEDIUM = 12
FONT_SIZE_SMALL = 10
FONT_SIZE_XSMALL = 9

# 메시지 상수
MSG_LOADING = "진단 중입니다. 잠시만 기다려주세요."
MSG_FONT_LOAD_FAILED = "Failed to load font"
MSG_DIALOG_TITLE = "진단 중"
MSG_RESULT_TITLE = "결과"
MSG_CAMERA_CONNECTED = "카메라가 연결되었습니다."
MSG_CAMERA_DISCONNECTED = "카메라가 연결되지 않았습니다."

# 다이얼로그 크기
DIALOG_WIDTH = 300
DIALOG_HEIGHT = 150

class MeasureUI(QMainWindow, uic.loadUiType(UI_PATH)[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._setup_fonts()
        self._init_ui()
        self._connect_signals()

    def _setup_fonts(self):
        """폰트 설정"""
        self.font_family = self._load_font(FONT_SRC)
        self.font_bold_family = self._load_font(FONT_BOLD_SRC)

    def _load_font(self, font_path):
        """폰트 로드"""
        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print(MSG_FONT_LOAD_FAILED)
            return None
        return QFontDatabase.applicationFontFamilies(font_id)[0]

    def _init_ui(self):
        """UI 요소 초기화"""
        if not self.font_family:
            return

        # 폰트 크기별 위젯 그룹화
        font_groups = {
            FONT_SIZE_LARGE: [self.title],
            FONT_SIZE_MEDIUM: [self.cctv_measure, self.weight_measure],
            FONT_SIZE_SMALL: [self.cctv_desc, self.weight_desc, self.weight_warning],
            FONT_SIZE_XSMALL: [
                self.cctv_radio1, self.cctv_radio2, self.cctv_radio3,
                self.weight_radio, self.cctv_date, self.weight_date,
                self.cctv_measure_btn, self.weight_measure_btn
            ]
        }

        # 폰트 적용
        for size, widgets in font_groups.items():
            for widget in widgets:
                widget.setFont(QFont(self.font_family, size))

    def _connect_signals(self):
        """시그널 연결"""
        self.cctv_measure_btn.clicked.connect(self._on_cctv_measure_clicked)

    def _on_cctv_measure_clicked(self):
        """CCTV 측정 버튼 클릭 시 실행될 메서드"""
        # measure.py에서 오버라이드하여 사용
        pass

    def show_result_message(self, is_connected):
        """결과 메시지 표시"""
        result_msg = QMessageBox(self)
        result_msg.setWindowTitle(MSG_RESULT_TITLE)
        
        if is_connected:
            result_msg.setText(MSG_CAMERA_CONNECTED)
            result_msg.setIcon(QMessageBox.Information)
        else:
            result_msg.setText(MSG_CAMERA_DISCONNECTED)
            result_msg.setIcon(QMessageBox.Warning)
            
        result_msg.exec_()

    def create_loading_dialog(self):
        """로딩 다이얼로그 생성"""
        loading_dialog = QDialog(self)
        loading_dialog.setWindowTitle(MSG_DIALOG_TITLE)
        loading_dialog.setFixedSize(DIALOG_WIDTH, DIALOG_HEIGHT)

        layout = QVBoxLayout(loading_dialog)

        loading_label = QLabel(MSG_LOADING, loading_dialog)
        loading_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(loading_label)

        progress_bar = QProgressBar(loading_dialog)
        progress_bar.setValue(0)
        layout.addWidget(progress_bar)

        return loading_dialog, progress_bar 