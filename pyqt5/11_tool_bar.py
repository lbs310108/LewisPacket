import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        act_tool = QAction(QIcon('icon.png'), 'exit', self)
        act_tool.setShortcut('Ctrl+q')
        act_tool.triggered.connect(qApp.quit)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(act_tool)

        self.resize(400, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())