import sys
from os import getcwd, listdir, stat
from os.path import dirname, isdir, isfile, join
from time import localtime, strftime
try:
    # Windows.
    from os import startfile
except ImportError:
    # Otras plataformas.
    from webbrowser import open as startfile
from hurry.filesize import size
#from PyQt4.QtCore import QStringList
from PyQt4.QtGui import (QApplication, QHBoxLayout, QIcon, QMainWindow,
                         QLineEdit, QPushButton, QTreeWidget,
                         QTreeWidgetItem, QVBoxLayout, QWidget)
