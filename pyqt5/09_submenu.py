import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        file_bar = menubar.addMenu('File')

        # QMenu是显示菜单，QAction是执行菜单
        imp_bar = QMenu('import', self)
        imp_act = QAction('import mail', self)
        # 在菜单中加入执行菜单，实现子菜单
        imp_bar.addAction(imp_act)

        # 创建执行菜单
        new_file = QAction('new', self)

        # addAction是添加执行菜单，addMenu是添加显示菜单
        file_bar.addAction(new_file)
        file_bar.addMenu(imp_bar)

        menubar.setNativeMenuBar(False)
        self.resize(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())