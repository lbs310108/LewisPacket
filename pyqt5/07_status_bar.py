# QMainWindow中在setUi时自动为用户创建了一个菜单栏、工具栏、中心窗口和状态栏
# 而QWidget是没有这几点的。

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 300)
        # 创建statusBar
        self.statusBar().showMessage('Ready')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())