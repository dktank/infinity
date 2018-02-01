# coding:utf-8

import sys
from PyQt5.QtWidgets import QApplication

from main_window import IFMainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)

    ifmw = IFMainWindow()

    ifmw.show()

    sys.exit(app.exec_())




