from PySide import QtCore
from PySide import QtGui
import sys

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow,self).__init__()

app = QtGui.QApplication(sys.argv)
form = MyMainWindow()
form.show()
app.exec_()
