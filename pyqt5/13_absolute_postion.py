import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 使用move()方法定位了每一个元素，使用x、y坐标。x、y坐标的原点是程序的左上角。
        test = QLabel('test', self)
        test.move(10, 10)

        test2 = QLabel('test2', self)
        test2.move(30, 30)

        test3 = QLabel('test3', self)
        test3.move(50, 50)

        self.resize(300, 300)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())