import sys
from PyQt5.QtWidgets import QMainWindow,QApplication, QAction, qApp, QTextEdit
from PyQt5.QtGui import QIcon


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar()

        # set action for menu_bar
        new_act = QAction('new', self)
        open_act = QAction('open', self)
        quit_act = QAction('quit', self)
        quit_act.triggered.connect(qApp.quit)
        quit_act.setShortcut('Ctrl+q')
        quit_act.setStatusTip('quit app')

        # set menu_bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')
        file_menu.addAction(new_act)
        file_menu.addAction(open_act)
        file_menu.addAction(quit_act)

        # set tool_bar action
        tool_act = QAction(QIcon('icon.png'), 'exit', self)
        tool_act.triggered.connect(qApp.quit)
        tool_act.setStatusTip('quit app')
        tool_act.setShortcut('Ctrl+q')

        # set tool_bar
        tool_bar = self.addToolBar('exit')
        tool_bar.addAction(tool_act)

        # 这里创建了一个文本编辑区域，并把它放在QMainWindow的中间区域。这个组件或占满所有剩余的区域。
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        menubar.setNativeMenuBar(False)
        self.resize(400, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())