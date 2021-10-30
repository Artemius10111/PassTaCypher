import os
import sys
from generator import generator_logic as gl
from interface_pyqt import *
from PyQt5 import QtCore, QtGui, QtWidgets
from cryptographer import cipher, decipher
class Main_file(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setMaximumSize(480, 640)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.setWindowIcon(QtGui.QIcon(scriptDir + os.path.sep + "pasta.ico"))
        self.ui.GenerateButton.setStyleSheet(
            ""
            "background-color: rgb(100, 100, 100)"
            "}\n"
            "")
        # #Page 1
        self.ui.GenerateButton.clicked.connect(lambda: self.ui.Stacked_widget.setCurrentWidget(self.ui.page_1))
        self.ui.GenerateButton.clicked.connect(lambda: self.ui.GenerateButton.setStyleSheet(
            ""
            "background-color: rgb(100, 100, 100)"
            "}\n"
            ""))
        self.ui.GenerateButton.clicked.connect(lambda: self.ui.Cipher_button.setStyleSheet(
            ""
            "background-color: rgb(255, 120, 57)"
            "}\n"
            ""))
        self.ui.GenerateButton.clicked.connect(lambda: self.ui.Decipher_Button.setStyleSheet(
            ""
            "background-color: rgb(255, 120, 57)"
            "}\n"
            ""))
            
        # # #Page 2\
        self.ui.Cipher_button.clicked.connect(lambda: self.ui.Stacked_widget.setCurrentWidget(self.ui.page_2))
        self.ui.Cipher_button.clicked.connect(lambda: self.ui.GenerateButton.setStyleSheet(
            ""
            "background-color: rgb(255, 120, 57)"
            "}\n"
            ""))
        self.ui.Cipher_button.clicked.connect(lambda: self.ui.Cipher_button.setStyleSheet(
            ""
            "background-color: rgb(100, 100, 100)"
            "}\n"
            ""))
        self.ui.Cipher_button.clicked.connect(lambda: self.ui.Decipher_Button.setStyleSheet(
            ""
            "background-color: rgb(255, 120, 57))"
            "}\n"
            ""))
        # self.ui.Cipher_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        # # #Page 3
        self.ui.Decipher_Button.clicked.connect(lambda: self.ui.Stacked_widget.setCurrentWidget(self.ui.page_3))
        self.ui.Decipher_Button.clicked.connect(lambda: self.ui.GenerateButton.setStyleSheet(
            ""
            "background-color: rgb(255, 120, 57)"
            "}\n"
            ""))
        self.ui.Decipher_Button.clicked.connect(lambda: self.ui.Cipher_button.setStyleSheet(
            ""
            "background-color: rgb(255, 120, 57)"
            "}\n"
            ""))
        self.ui.Decipher_Button.clicked.connect(lambda: self.ui.Decipher_Button.setStyleSheet(
            ""
            "background-color: rgb(100, 100, 100)"
            "}\n"
            ""
        ))
        self.button_list = [
            self.ui.radio_symbols_,
            self.ui.radio_symbols_2,
            self.ui.radio_symbols_3,
            self.ui.radio_symbols_4
        ] 
        self.list_password_key = []
        self.ui.Generate_start.clicked.connect(self.check_empty_and_setText)
        self.ui.Cipher_start.clicked.connect(self.one_list_cipher)
        self.ui.Cipher_start.clicked.connect(lambda: self.ui.Password_text_cipher_2.setText(self.list_password_key[1]))
        self.ui.Cipher_start.clicked.connect(lambda: self.ui.Password_text_cipher_3.setText(self.list_password_key[0]))
    
    def radio_clicked(self):
        for i in self.button_list:
            if i.isChecked():
                return self.button_list.index(i)+1
        
    def one_list_cipher(self):
        self.list_password_key = cipher(self.ui.Password_text_cipher_1.toPlainText())
        self.ui.Decipher_start.clicked.connect(lambda: self.ui.Password_text_decipher_3.setText(decipher({
            self.ui.Password_text_decipher_1.toPlainText():
            self.ui.Password_text_decipher_2.toPlainText()
        })))

    def check_empty_and_setText(self):
        if len(self.ui.Length_password.text()) == 0 or self.isInt(self.ui.Length_password.text()):
            self.ui.Length_password.setStyleSheet(
                ""
                "QLineEdit{\n"
                "    border: 2px solid rgb(255, 78, 78)"
                "}\n"
                ""
            )
            self.ui.Password_text.setText("ERROR")
        else:
            self.ui.Length_password.setStyleSheet(
                ""
                "QLineEdit{\n"
                "    border: None"
                "}\n"
                ""
            )
            self.ui.Password_text.setText(
            gl(self.radio_clicked(), int(self.ui.Length_password.text())).generate_password()
            )

    def isInt(self, string_) -> str:
        try: 
            int(string_)
            return False
        except: 
            return True
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_app = Main_file()
    main_app.show()
    sys.exit(app.exec_())