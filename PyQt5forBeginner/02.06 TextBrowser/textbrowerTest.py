import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QTextCursor
form_class = uic.loadUiType("textbrowserTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #버튼에 기능을 할당하는 코드
        self.btn_Print.clicked.connect(self.printTextFunction)
        self.btn_setText.clicked.connect(self.changeTextFunction)
        self.btn_appendText.clicked.connect(self.appendTextFunction)
        self.btn_Clear.clicked.connect(self.clearTextFunction)

    def printTextFunction(self) :
        #self.Textbrowser이름.toPlainText()
        #Textbrowser에 있는 글자를 가져오는 메서드
        print(self.textbrow_Test.toPlainText())

    def changeTextFunction(self) :
        #self.Textbrowser이름.setPlainText()
        #Textbrowser에 있는 글자를 가져오는 메서드
        self.textbrow_Test.setPlainText("This is Textbrowser - Change Text")


    # def appendTextFunction(self) : #줄바꿈 후 텍스트 추가
    #     #self.Textbrowser이름.append()
    #     #Textbrowser에 있는 글자를 가져오는 메서드
    #     self.textbrow_Test.append("Append Text")

    # 기존 텍스트에 바로 붙이기기
    # def appendTextFunction(self) :
    #     self.textbrow_Test.insertPlainText("Append Text")
    
    # def appendTextFunction(self):
    #     # 현재 텍스트 가져오기
    #     current_text = self.textbrow_Test.toPlainText()
        
    #     # 새로운 텍스트를 기존 텍스트에 바로 붙이기
    #     self.textbrow_Test.setPlainText(current_text + " Append Text")


    def appendTextFunction(self):
        self.textbrow_Test.moveCursor(QTextCursor.End)  # 커서를 끝으로 자동 이동
        self.textbrow_Test.insertPlainText("Append Text")

    def clearTextFunction(self) :
        #self.Textbrowser.clear()
        #Textbrowser에 있는 글자를 지우는 메서드
        self.textbrow_Test.clear()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()
