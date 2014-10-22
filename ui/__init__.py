from PySide import QtGui

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow,self).__init__()
        
        self.setWindowTitle('Modular GUI')
        self.resize(1000,700)