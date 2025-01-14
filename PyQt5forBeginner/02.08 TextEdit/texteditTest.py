import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont, QColor, QTextCursor, QTextCharFormat
from PyQt5 import uic

form_class = uic.loadUiType("texteditTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10

        #TextEdit과 관련된 버튼에 기능 연결
        self.btn_printTextEdit.clicked.connect(self.printTextEdit)
        self.btn_clearTextEdit.clicked.connect(self.clearTextEdit)
        self.btn_setFont.clicked.connect(self.setFont)
        self.btn_setFontItalic.clicked.connect(self.fontItalic)
        self.btn_setFontColor.clicked.connect(self.fontColorRed)
        self.btn_fontSizeUp.clicked.connect(self.fontSizeUp)
        self.btn_fontSizeDown.clicked.connect(self.fontSizeDown)

    def printTextEdit(self) :
        print(self.textedit_Test.toPlainText())

    def clearTextEdit(self) :
        self.textedit_Test.clear()

    # def setFont(self) :
    #     fontvar = QFont("Apple SD Gothic Neo",10)
    #     self.textedit_Test.setCurrentFont(fontvar)

    # def fontItalic(self) :
    #     self.textedit_Test.setFontItalic(True)

    # def fontColorRed(self) :
    #     colorvar = QColor(255,0,0)
    #     self.textedit_Test.setTextColor(colorvar)

    # def fontSizeUp(self) :
    #     self.fontSize = self.fontSize + 1
    #     self.textedit_Test.setFontPointSize(self.fontSize)

    # def fontSizeDown(self) :
    #     self.fontSize = self.fontSize - 1
    #     self.textedit_Test.setFontPointSize(self.fontSize)


    # 전체 텍스트 적용
    def setFont(self):
        font = QFont("Apple SD Gothic Neo", 10)
        cursor = self.textedit_Test.textCursor()
        cursor.select(QTextCursor.Document)  # 전체 텍스트 선택
        fmt = QTextCharFormat()
        fmt.setFont(font)
        cursor.mergeCharFormat(fmt)

    def fontItalic(self):
        cursor = self.textedit_Test.textCursor()
        cursor.select(QTextCursor.Document)
        fmt = QTextCharFormat()
        fmt.setFontItalic(True)
        cursor.mergeCharFormat(fmt)

    def fontColorRed(self):
        color = QColor(255, 0, 0)
        cursor = self.textedit_Test.textCursor()
        cursor.select(QTextCursor.Document)
        fmt = QTextCharFormat()
        fmt.setForeground(color)
        cursor.mergeCharFormat(fmt)

    def fontSizeUp(self):
        self.fontSize += 1
        cursor = self.textedit_Test.textCursor()
        cursor.select(QTextCursor.Document)
        fmt = QTextCharFormat()
        fmt.setFontPointSize(self.fontSize)
        cursor.mergeCharFormat(fmt)

    def fontSizeDown(self):
        self.fontSize -= 1
        cursor = self.textedit_Test.textCursor()
        cursor.select(QTextCursor.Document)
        fmt = QTextCharFormat()
        fmt.setFontPointSize(self.fontSize)
        cursor.mergeCharFormat(fmt)

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_() 