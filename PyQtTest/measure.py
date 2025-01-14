import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressBar, QLabel, QDialog, QVBoxLayout
from PyQt5.QtCore import QTimer, QDateTime, Qt
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5 import uic

# 상수 정의
UI_PATH = "ui/measure.ui"
FONT_PATH = "font/NanumGothic.ttf"

# 폰트 크기 상수
FONT_SIZE_LARGE = 14
FONT_SIZE_MEDIUM = 12
FONT_SIZE_SMALL = 10
FONT_SIZE_XSMALL = 9

# 메시지 상수
MSG_LOADING = "진단 중입니다. 잠시만 기다려주세요."
MSG_CAMERA_CONNECTED = "카메라가 연결되어 있습니다."
MSG_CAMERA_DISCONNECTED = "카메라가 연결되어 있지 않습니다."
MSG_FONT_LOAD_FAILED = "Failed to load font"
MSG_DIALOG_TITLE = "진단 중"
MSG_RESULT_TITLE = "결과"
MSG_RECENT_CHECK = "최근 진단일시: {}"

# 다이얼로그 크기
DIALOG_WIDTH = 300
DIALOG_HEIGHT = 150

class WindowClass(QMainWindow, uic.loadUiType(UI_PATH)[0]):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._setup_fonts()
        self._init_ui()
        self._connect_signals()

    def _setup_fonts(self):
        """폰트 설정"""
        self.font_family = self._load_font(FONT_PATH)
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
        self.cctv_measure_btn.clicked.connect(self.check_camera_connection)

    def check_camera_connection(self):
        """카메라 연결 확인 시작"""
        self._create_loading_dialog()
        self._start_progress_timer()

    def _create_loading_dialog(self):
        """로딩 다이얼로그 생성"""
        self.loading_dialog = QDialog(self)
        self.loading_dialog.setWindowTitle(MSG_DIALOG_TITLE)
        self.loading_dialog.setFixedSize(DIALOG_WIDTH, DIALOG_HEIGHT)

        layout = QVBoxLayout(self.loading_dialog)

        self.loading_label = QLabel(MSG_LOADING, self.loading_dialog)
        self.loading_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.loading_label)

        self.progress_bar = QProgressBar(self.loading_dialog)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        self.loading_dialog.show()

    def _start_progress_timer(self):
        """진행 상태 타이머 시작"""
        self.timer = QTimer(self)
        self.timer.timeout.connect(self._update_progress)
        self.progress_value = 0
        self.timer.start(1000)

    def _update_progress(self):
        """진행 상태 업데이트"""
        self.progress_value += 33
        self.progress_bar.setValue(self.progress_value)

        if self.progress_value >= 100:
            self.timer.stop()
            self.loading_dialog.close()
            self._check_connection_result()

    def _check_connection_result(self):
        """카메라 연결 상태 확인 및 결과 표시"""
        is_connected = self._check_camera()
        self._update_check_time()
        self._show_result_message(is_connected)

    def _check_camera(self):
        """카메라 연결 확인"""
        cap = cv2.VideoCapture(0)
        is_connected = cap.isOpened()
        cap.release()
        return is_connected

    def _update_check_time(self):
        """진단 시간 업데이트"""
        current_time = QDateTime.currentDateTime()
        formatted_time = current_time.toString("yyyy.MM.dd hh:mm")
        self.cctv_date.setText(MSG_RECENT_CHECK.format(formatted_time))

    def _show_result_message(self, is_connected):
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

def main():
    app = QApplication(sys.argv)
    window = WindowClass()
    window.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
