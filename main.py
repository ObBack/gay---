from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QPushButton, QComboBox, QLabel)
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader

class Gay(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('./ui/main.ui')
        self.setWindowTitle('Gay鉴别器')
        self.setCentralWidget(self.ui)
        self.setFixedSize(480, 300)
        self.setWindowIcon(QIcon("./icon.ico"))

        ver = "v_1.0.0"

        self.examine_button = self.findChild(QPushButton, 'examine')
        self.combobox = self.findChild(QComboBox, 'comboBox')
        self.ver_label = self.findChild(QLabel, 'ver')
        # 为按钮的点击事件绑定槽函数
        self.examine_button.clicked.connect(self.check_combobox)
        self.ver_label.setText(ver)

    def check_combobox(self):
        # 获取下拉框当前选中的文本
        selected_text = self.combobox.currentText()
        if selected_text == "男":
            QMessageBox.information(self, "提示", "你是Gay", QMessageBox.Yes)
        elif selected_text == "女":
            QMessageBox.information(self, "提示", "你不是Gay", QMessageBox.Yes)
        else:
            QMessageBox.information(self, "提示", "?", QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication()
    gay = Gay()
    gay.show()
    app.exec()