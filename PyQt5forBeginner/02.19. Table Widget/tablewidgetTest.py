import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("tablewidgetTest.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initialize_table()
        self.connect_signals()

    def initialize_table(self):
        """테이블 초기 설정"""
        self.tableWidget_Test.setColumnCount(2)  # 학번, 학부 컬럼
        self.tableWidget_Test.setHorizontalHeaderLabels(["학번", "학부"])
        

    def connect_signals(self):
        """버튼 시그널 연결"""
        self.btn_addItem.clicked.connect(self.add_row)
        self.btn_printItem.clicked.connect(self.print_selected_row)
        self.btn_printMultiItems.clicked.connect(self.print_selected_rows)
        self.btn_removeItem.clicked.connect(self.remove_selected_row)
        self.btn_clearItem.clicked.connect(self.clear_all_rows)

    def add_empty_row(self, header_text):
        """새로운 빈 행 추가"""
        row_position = self.tableWidget_Test.rowCount()
        self.tableWidget_Test.insertRow(row_position)
        self.tableWidget_Test.setVerticalHeaderItem(row_position, QTableWidgetItem(header_text))

    def validate_input(self, input_text):
        """입력값 검증"""
        if not input_text:
            self.show_error_message("Please enter data in the format: Name,Student Number,Department")
            return None

        try:
            name, student_number, department = [item.strip() for item in input_text.split(",")]
            return name, student_number, department
        except ValueError:
            self.show_error_message("Please enter data in the format: Name,Student Number,Department")
            return None

    def show_error_message(self, message):
        """에러 메시지 표시"""
        QMessageBox.warning(self, "Input Error", message)

    def add_row(self):
        """새로운 행 추가"""
        input_data = self.validate_input(self.line_addItem.text().strip())
        if not input_data:
            return

        name, student_number, department = input_data
        row_position = self.tableWidget_Test.rowCount()
        
        # 새 행 추가 및 데이터 설정
        self.tableWidget_Test.insertRow(row_position)
        self.tableWidget_Test.setVerticalHeaderItem(row_position, QTableWidgetItem(name))
        self.tableWidget_Test.setItem(row_position, 0, QTableWidgetItem(student_number))
        self.tableWidget_Test.setItem(row_position, 1, QTableWidgetItem(department))
        
        self.line_addItem.clear()

    def get_row_data(self, row):
        """특정 행의 데이터 가져오기"""
        header = self.tableWidget_Test.verticalHeaderItem(row).text()
        student_number = self.tableWidget_Test.item(row, 0).text() if self.tableWidget_Test.item(row, 0) else ""
        department = self.tableWidget_Test.item(row, 1).text() if self.tableWidget_Test.item(row, 1) else ""
        return header, student_number, department

    def print_selected_row(self):
        """선택된 행 출력"""
        selected_items = self.tableWidget_Test.selectedItems()
        if not selected_items:
            self.show_error_message("No row selected.")
            return

        row = selected_items[0].row()
        header, student_number, department = self.get_row_data(row)
        print(f"Row {row} {header}, {student_number}, {department}")

    def print_selected_rows(self):
        """선택된 모든 행 출력"""
        selected_ranges = self.tableWidget_Test.selectedRanges()
        if not selected_ranges:
            self.show_error_message("No rows selected.")
            return

        for selected_range in selected_ranges:
            for row in range(selected_range.topRow(), selected_range.bottomRow() + 1):
                header, student_number, department = self.get_row_data(row)
                print(f"Row {row} {header}, {student_number}, {department}")

    def remove_selected_row(self):
        """선택된 행 삭제"""
        selected_items = self.tableWidget_Test.selectedItems()
        if not selected_items:
            self.show_error_message("No row selected.")
            return

        rows_to_remove = sorted(set(item.row() for item in selected_items), reverse=True)
        for row in rows_to_remove:
            self.tableWidget_Test.removeRow(row)

    def clear_all_rows(self):
        """모든 행 삭제"""
        self.tableWidget_Test.setRowCount(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()