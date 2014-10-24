from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem
from PyQt5.QtCore import QUrl

import os

__all__ = ['SubtleMainWindow',]

class SubtleMainWindow(QMainWindow):

    def __init__(self, paths=[]):
        QMainWindow.__init__( self )
        self.setWindowTitle( 'Subtle' )
        self._tree = SubtleTreeWidget(self, paths_to_items_list(self, paths))
        self.setCentralWidget( self._tree )
        self.setAcceptDrops( True )

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        items = paths_to_items_list(self._tree, event.mimeData().urls())
        self._tree.addTopLevelItems( items )
        event.acceptProposedAction()

class SubtleTreeWidget(QTreeWidget):

    def __init__(self, parent, items):
        QTreeWidget.__init__( self )
        self.setColumnCount( 1 )
        self.setHeaderHidden( True )
        self.addTopLevelItems( items )

def paths_to_items_list(parent, paths):
    items = []
    for path in paths:
        path = QUrl(path) if type(path) == QUrl else path
        item = QTreeWidgetItem(parent, [ path.path() ])
        item.setData(0, 0, path)
        item.setText(0, os.path.basename(path.fileName()))
        items.append( item )
    return items
