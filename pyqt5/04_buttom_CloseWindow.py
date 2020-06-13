import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        btn = QPushButton('QUIT', self)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)
        # QCoreApplication包含了事件的主循环，它能添加和删除所有的事件，instance()创建了一个它的实例
        btn.clicked.connect(QCoreApplication.instance().quit)
        self.setGeometry(300, 300, 1024, 768)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())