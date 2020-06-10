import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 每个PyQt5都必须要有的应用对象，sys.argv是一组命令行参数的列表
app = QApplication(sys.argv)

# 定义一个窗口对象
w = QWidget()
# 定义窗口大小
w.resize(800, 600)
# 定义窗口在屏幕中的位置
w.move(300, 300)
# 显示窗口
w.show()

# 主循环从窗口上接收事件，并把事件传入到派发到应用控件里
sys.exit(app.exec_())