import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 设置图标和标签
        exitAct = QAction(QIcon('icon.png'), '&Exit', self)
        # 设置快捷键
        exitAct.setShortcut('Ctrl+q')
        # 设置状态栏说明
        exitAct.setStatusTip('exit app')
        # 绑定动作，退出程序
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        # 基于MAC OS的测试
        menubar.setNativeMenuBar(False)

        self.resize(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())