from PySide import QtGui
import logging
import ui
import sys

log = logging.getLogger('modular_GUI')

'''try:
'''
app = QtGui.QApplication(sys.argv)
form = ui.MyMainWindow()
form.show()
app.exec_()

'''
except:
    log.error('Failed to load the Modular GUI')
    raise Exception('Failed to load the Modular GUI')
'''
