from PySide import QtGui
import traceback
import logging
import ui
import sys

log = logging.getLogger('modular_GUI')

try:
    app = QtGui.QApplication(sys.argv)
    form = ui.MyMainWindow()
    form.show()
    app.exec_()

except Exception:
    log.error('Failed to load the Modular GUI. Check "stacktrace.txt" '
              'for details')

    with open("stacktrace.txt", "w") as text_file:
        text_file.write(traceback.format_exc())

    raise Exception('Failed to load the Modular GUI. Check "stacktrace.txt" '
                    'for details')
