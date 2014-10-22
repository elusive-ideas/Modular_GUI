from PySide import QtCore
from PySide import QtGui
import sys

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow,self).__init__()
        self.setWindowTitle('Modular GUI')
        self.resize(1000,700)

app = QtGui.QApplication(sys.argv)
form = MyMainWindow()
form.show()
app.exec_()
