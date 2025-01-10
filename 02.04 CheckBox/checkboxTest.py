import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("checkboxTest.ui")[0]

class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        #GroupBox밖에 있는 CheckBox에 기능 연결
        self.chk_1.stateChanged.connect(lambda: self.chkFunction(1))
        self.chk_2.stateChanged.connect(lambda: self.chkFunction(2))
        self.chk_3.stateChanged.connect(lambda: self.chkFunction(3))
        self.chk_4.stateChanged.connect(lambda: self.chkFunction(4))

        #GroupBox안에 있는 CheckBox에 기능 연결
        self.groupchk_1.stateChanged.connect(lambda: self.groupchkFunction(1))
        self.groupchk_2.stateChanged.connect(lambda: self.groupchkFunction(2))
        self.groupchk_3.stateChanged.connect(lambda: self.groupchkFunction(3))
        self.groupchk_4.stateChanged.connect(lambda: self.groupchkFunction(4))

    def chkFunction(self, num) :
        #CheckBox는 여러개가 선택될 수 있기 때문에 elif를 사용하지 않습니다.
        if num == 1 :
            if self.chk_1.isChecked() : print("chk_1 isChecked")
            else : print("chk_1 isUnchecked")
        elif num == 2 :
            if self.chk_2.isChecked() : print("chk_2 isChecked")
            else : print("chk_2 isUnchecked")
        elif num == 3 :
            if self.chk_3.isChecked() : print("chk_3 isChecked")
            else : print("chk_3 isUnchecked")
        elif num == 4 :
            if self.chk_4.isChecked() : print("chk_4 isChecked")
            else : print("chk_4 isUnchecked")

    def groupchkFunction(self, num) :
        if num == 1 :
            if self.groupchk_1.isChecked() : print("groupchk_1 isChecked")
            else : print("groupchk_1 isUnchecked")
        elif num == 2 :
            if self.groupchk_2.isChecked() : print("groupchk_2 isChecked")
            else : print("groupchk_2 isUnchecked")
        elif num == 3 :
            if self.groupchk_3.isChecked() : print("groupchk_3 isChecked")
        elif num == 4 :
            if self.groupchk_4.isChecked() : print("groupchk_4 isChecked")
            else : print("groupchk_4 isUnchecked")

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()