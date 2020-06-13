import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, qApp


class example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(300, 300)
        self.show()

    # 使用contextMenuEvent()方法实现这个菜单
    def contextMenuEvent(self, event):
        cmenu = QMenu(self)

        act_new = cmenu.addAction("new")
        act_open = cmenu.addAction('open')
        act_quit = cmenu.addAction('quit')

        # 使用exec_()方法显示菜单。从鼠标右键事件对象中获得当前坐标。
        # mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
        action = cmenu.exec_(self.mapToGlobal(event.pos()))

        # 如果右键菜单里触发了事件，也就触发了退出事件，执行关闭菜单行为。
        if action == act_quit:
            qApp.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = example()
    sys.exit(app.exec_())