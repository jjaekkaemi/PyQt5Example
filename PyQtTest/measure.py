import sys
import cv2
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, QDateTime
from measure_ui import MeasureUI

# 메시지 상수
MSG_RECENT_CHECK = "최근 진단일시: {}"

class MeasureWindow(MeasureUI):
    def __init__(self):
        super().__init__()

    def _on_cctv_measure_clicked(self):
        """CCTV 측정 버튼 클릭 이벤트 처리"""
        self.check_camera_connection()

    def check_camera_connection(self):
        """카메라 연결 확인 시작"""
        self.loading_dialog, self.progress_bar = self.create_loading_dialog()
        self.loading_dialog.show()
        self._start_progress_timer()

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
        self.show_result_message(is_connected)

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

def main():
    app = QApplication(sys.argv)
    window = MeasureWindow()
    window.show()
    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())
