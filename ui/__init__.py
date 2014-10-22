from PySide import QtGui
import logging

log = logging.getLogger('modular_GUI.ui')

class MyMainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        log.debug('Initialising the Modular GUI')
        super(MyMainWindow,self).__init__()
        
        self.setWindowTitle('Modular GUI')
        self.resize(1000,700)
        
        log.debug('The Modular GUI has been initialised')