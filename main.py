from PySide import QtGui
import ui
import sys

app = QtGui.QApplication(sys.argv)
form = ui.MyMainWindow()
form.show()
app.exec_()