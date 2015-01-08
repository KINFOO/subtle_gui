from PyQt5 import QtCore
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QKeySequence
from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem, QMenuBar,\
    QAction

import os

__all__ = ['SubtleMainWindow',]

class SubtleMainWindow(QMainWindow):

    def __init__(self, paths=[]):
        QMainWindow.__init__( self )
        self.setWindowTitle( 'Subtle' )
        self.setAcceptDrops( True )

        self._menu = QMenuBar( self )
        fileMenu = self._menu.addMenu( '&File' )
        fileMenu.addAction( QAction('&Open', fileMenu) )
        close = QAction('&Quit', fileMenu)
        close.setShortcut( QKeySequence(QKeySequence.Quit) )
        close.triggered.connect( self._close_action )
        fileMenu.addAction( close )
        self.setMenuBar( self._menu )

        self._tree = SubtleTreeWidget(self, paths_to_items_list(self, paths))
        self.setCentralWidget( self._tree )

    @QtCore.pyqtSlot()
    def _close_action(self):
        self.close()

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        items = paths_to_items_list(self._tree, event.mimeData().urls())
        self._tree.addTopLevelItems( items )
        self.update()
        event.acceptProposedAction()

    def update(self):
        items = [ self._tree.itemAt(i, 0)
            for i in range(0, self._tree.topLevelItemCount()) ]
        for item in items:
            print( 'item {}'.format(item.data(0, SubtleTreeWidget.ITEM_ROLE)) )

class SubtleTreeWidget(QTreeWidget):

    ITEM_ROLE = 0

    def __init__(self, parent, items):
        QTreeWidget.__init__( self )
        self.setColumnCount( 2 )
        header = QTreeWidgetItem( SubtleTreeWidget.ITEM_ROLE )
        header.setText(0, 'File')
        header.setText(1, 'Status')
        self.setHeaderItem( header )
        self.addTopLevelItems( items )

def paths_to_items_list(parent, paths):
    items = []
    for path in paths:
        url = QUrl(path) if type(path) == QUrl else path
        path = url.path()
        item = QTreeWidgetItem(parent, [ path ])
        item.setData(0, SubtleTreeWidget.ITEM_ROLE, url)
        item.setText(0, os.path.basename(path))
        item.setToolTip(0, path)
        items.append( item )
    return items
