import sys
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.show()

    def initUI(self):
        self.resize(300, 300)
        self.center()
        self.show()

    # 目前看，不写如下函数，窗口也可以居中
    def center(self):
        # 获得主窗口所在的框架
        qr = self.frameGeometry()
        # 获取显示器的分辨率，然后得到屏幕中间点的位置。
        cp = QDesktopWidget().availableGeometry().center()
        # 然后把主窗口框架的中心点放置到屏幕的中心位置。
        qr.moveCenter(cp)
        # 通过move函数把主窗口的左上角移动到其框架的左上角
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())