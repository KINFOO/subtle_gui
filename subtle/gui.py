from PyQt5.QtWidgets import QMainWindow, QTreeWidget, QTreeWidgetItem

__all__ = ['SubtleMainWindow',]

class SubtleMainWindow(QMainWindow):

    def __init__(self, items=[]):
        QMainWindow.__init__( self )
        self.setWindowTitle( 'Subtle' )
        self._tree = SubtleTreeWidget(self, items)
        self.setCentralWidget( self._tree )
        self.setAcceptDrops( True )

    def dragEnterEvent(self, event):
        event.acceptProposedAction()

    def dropEvent(self, event):
        self._tree.addTopLevelItems([ QTreeWidgetItem(self._tree, [url.path()])
            for url in event.mimeData().urls() ])
        event.acceptProposedAction()

class SubtleTreeWidget(QTreeWidget):

    def __init__(self, parent, items):
        QTreeWidget.__init__( self )
        self.setColumnCount( 1 )
        self.setHeaderHidden( True )
        self.insertTopLevelItems(0, items)
