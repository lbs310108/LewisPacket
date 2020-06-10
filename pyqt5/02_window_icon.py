import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


# 这个类继承QWidget，super()构造器方法返回父级的对象
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 参数分别代表屏幕坐标的x、y和窗口大小的宽、高
        self.setGeometry(300, 300, 1024, 768)
        self.setWindowTitle('lewis')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.setWindowIcon(QIcon('icon.png'))
    sys.exit(app.exec_())

