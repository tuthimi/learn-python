from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 设置窗口标题
        self.setWindowTitle('My First App')

        # 设置标签
        label = QLabel('Welcome to Shiyanlou!')
        # 设置标签显示在中央
        label.setAlignment(Qt.AlignCenter)
        # 添加标签到主窗口
        self.setCentralWidget(label)

        # 创建工具栏
        tb = QToolBar('Tool Bar')
        # 设置工具栏中按钮的大小
        tb.setIconSize(QSize(32, 32))
        # 添加工具栏到主窗口
        self.addToolBar(tb)

        # 添加按钮动作，并加载图标图像
        button_action = QAction(QIcon('icons/penguin.png'), 'Menu button', self)
        # 设置状态栏提示
        button_action.setStatusTip('This is menu button')
        button_action.triggered.connect(self.onButtonClick)
        button_action.setCheckable(True)
        # 添加到工具栏
        tb.addAction(button_action)
        # 为主窗口设置状态栏
        self.setStatusBar(QStatusBar(self))

    def onButtonClick(self, s):
        print(s)


# 创建应用实例，通过 sys.argv 传入命令行参数
app = QApplication(sys.argv)
# 创建窗口实例
window = MainWindow()
# 显示窗口
window.show()
# 执行应用，进入事件循环
app.exec_()