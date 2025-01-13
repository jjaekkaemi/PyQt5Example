import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic

form_class = uic.loadUiType("tablewidgetTest.ui")[0]

class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initialize the header list
        self.vertical_headers = ["이세빈", "김민수", "홍길동", "이석준"]

        # Set initial vertical headers
        self.tableWidget_Test.setVerticalHeaderLabels(self.vertical_headers)

        # Connect buttons to respective functions
        self.btn_addItem.clicked.connect(self.add_row)
        self.btn_printItem.clicked.connect(self.print_selected_row)
        self.btn_printMultiItems.clicked.connect(self.print_selected_rows)
        self.btn_removeItem.clicked.connect(self.remove_selected_row)
        self.btn_clearItem.clicked.connect(self.clear_all_rows)

    def add_row(self):
        # Get input from Add Item line edit
        input_text = self.line_addItem.text().strip()
        if not input_text:
            QMessageBox.warning(self, "Input Error", "Please enter data in the format: Name,Student Number,Department")
            return

        # Split the input into name, student number, and department
        try:
            name, student_number, department = input_text.split(",")
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter data in the format: Name,Student Number,Department")
            return

        # Add a new row to the table
        row_count = self.tableWidget_Test.rowCount()
        self.tableWidget_Test.insertRow(row_count)

        # Populate the new row with data
        self.tableWidget_Test.setItem(row_count, 0, QTableWidgetItem(student_number.strip()))
        self.tableWidget_Test.setItem(row_count, 1, QTableWidgetItem(department.strip()))

        # Add the new name to the vertical headers list
        self.vertical_headers.append(name.strip())

        # Update the table's vertical headers
        self.tableWidget_Test.setVerticalHeaderLabels(self.vertical_headers)

        # Clear the input field
        self.line_addItem.clear()

    def print_selected_row(self):
        # Get the currently selected row
        selected_items = self.tableWidget_Test.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Error", "No row selected.")
            return

        # Print the content of the selected row
        row = selected_items[0].row()
        row_data = [self.tableWidget_Test.item(row, col).text() if self.tableWidget_Test.item(row, col) else "" for col in range(self.tableWidget_Test.columnCount())]
        print(f"Row {row}: {', '.join(row_data)}")

    def print_selected_rows(self):
        # Get all selected rows
        selected_ranges = self.tableWidget_Test.selectedRanges()
        if not selected_ranges:
            QMessageBox.warning(self, "Selection Error", "No rows selected.")
            return

        # Print the content of all selected rows
        for selected_range in selected_ranges:
            for row in range(selected_range.topRow(), selected_range.bottomRow() + 1):
                row_data = [self.tableWidget_Test.item(row, col).text() if self.tableWidget_Test.item(row, col) else "" for col in range(self.tableWidget_Test.columnCount())]
                print(f"Row {row}: {', '.join(row_data)}")

    def remove_selected_row(self):
        # Get the currently selected rows
        selected_items = self.tableWidget_Test.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "Selection Error", "No row selected.")
            return

        # Remove the selected rows
        rows_to_remove = sorted(set(item.row() for item in selected_items), reverse=True)
        for row in rows_to_remove:
            self.tableWidget_Test.removeRow(row)
            self.vertical_headers.pop(row)

        # Update the vertical headers
        self.tableWidget_Test.setVerticalHeaderLabels(self.vertical_headers)

    def clear_all_rows(self):
        # Clear all rows from the table
        self.tableWidget_Test.setRowCount(0)

        # Clear the vertical headers
        self.vertical_headers.clear()
        self.tableWidget_Test.setVerticalHeaderLabels(self.vertical_headers)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
