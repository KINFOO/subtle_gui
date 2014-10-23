#!/usr/bin/env python3
from PyQt5.QtWidgets import QApplication
from subtle.gui import SubtleMainWindow

import sys

if __name__ == '__main__':
    app = QApplication( sys.argv )
    main = SubtleMainWindow()
    main.show()
    sys.exit( app.exec_() )
