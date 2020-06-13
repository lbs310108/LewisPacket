import sys
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.show()

    # 函数重构，但关闭窗口时候，会自动调用它
    def closeEvent(self, event):
        replay = QMessageBox.question(self, 'message',
                             'Are you sure to quit',
                             QMessageBox.Yes | QMessageBox.No,
                             QMessageBox.No)

        if replay == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())