import sys
from tvRemoteUI import Television
from PyQt5 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    tv1 = Television()
    tv1.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())