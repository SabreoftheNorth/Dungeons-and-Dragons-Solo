from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QTabWidget, QStatusBar, QMenuBar, QMenu
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._init_window()
        self._init_menu()
        self._init_tabs()
        self._init_statusbar()

    # this is for the window itself, yazz

    def _init_window(self):
        self.setWindowTitle("Solo D&D Adventures")
        self.setMinimumSize(1100, 750)
        self.resize(1280, 800)

        # the central widget and root layout
        self._central = QWidget()
        self._root_layout = QVBoxLayout(self._central)
        self._root_layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(self._central)

    #this is for the menubar of the appzz
    def _init_menu(self):
        menubar: QMenuBar = self.menuBar()
        file_menu: QMenu = menubar.addMenu("&File")

        new_action = QAction("&New Campaign", self)
        new_action.setShortcut("Ctrl+N")
        new_action.triggered.connect(self._on_new_campaign)

        #YADAYADAYADA