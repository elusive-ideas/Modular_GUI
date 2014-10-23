from PySide import QtGui


def create(menubar):
    # Actions
    exitAction = QtGui.QAction('Exit', menubar)

    # Menus
    fileMenu = menubar.addMenu('&File')
    fileMenu.addAction(exitAction)
