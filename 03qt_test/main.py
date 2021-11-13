import sys
import demo1
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
      #每个PyQt5应用都必须创建一个应用对象。
      # sys.argv是一组命令行参数的列表。
      # Python可以在shell里运行，
      # 这个参数提供对脚本控制的功能。
      app = QApplication(sys.argv)

      # QMainWindow控件是一个用户界面的基本控件，
      MainWindow = QMainWindow()

      
      ui = demo1.Ui_MainWindow()
      ui.setupUi(MainWindow)
      MainWindow.show()
      sys.exit(app.exec_())