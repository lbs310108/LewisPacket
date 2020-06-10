import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建一个提示框，使用''中可以设置字体，大小是10号
        QToolTip.setFont(QFont('', 10))

        # 定义按钮
        btn = QPushButton('Button', self)
        # 创建提示框可以使用富文本格式的内容
        btn.setToolTip('This is a <b>QWidget</b> widget')
        # 定义按钮大小，btn.sizeHint()默认大小
        # 自定义按钮大小，btn.resize(100, 100)
        btn.resize(btn.sizeHint())
        # 定义在画布的位置
        btn.move(50, 50)

        self.setGeometry(300, 300, 800, 600)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
