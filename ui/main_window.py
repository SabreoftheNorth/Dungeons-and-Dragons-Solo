from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout,
    QTabWidget, QStatusBar, QMenuBar, QMenu
)
from PyQt6.QtGui import QAction
from PyQt6.QtCore import Qt

#constants used throughout this code
WINDOW_TITLE = "Solo DnD Adventures"
WINDOW_MIN_SIZE = (1100, 750)
WINDOW_START_SIZE = (1280, 800)
STATUS_READY_MESSAGE = "Ready... No campaign loaded."
APP_VERSION = "v0.1.0"

TAB_NAMES = [
    "Characters",
    "Dice Rollers",
    "Combat",
    "Journals"
]

MENU_SHORTCUTS = {
    "new": "Ctrl+N",
    "load": "Ctrl+O",
    "save": "Ctrl+S",
    "quit": "Ctrl+Q"
}

#main application windows for this app
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self._setup_window()
        self._create_menu_bar()
        self._create_tab_widget()
        self._create_status_bar()

    def _setup_window(self):
        #configure the main window properties as well as the central widget
        self.setWindowTitle(WINDOW_TITLE)
        self.setMinimumSize(*WINDOW_MIN_SIZE)
        self.resize(*WINDOW_START_SIZE)

        central_widget = QWidget()
        self._root_layout = QVBoxLayout(central_widget)
        self._root_layout.setContentsMargins(0, 0, 0, 0)
        self.setCentralWidget(central_widget)

    def _create_menu_bar(self):
        #initialize the menu bar with File and Help menus.
        menu_bar = self.menuBar()

        self._setup_file_menu(menu_bar.addMenu("&File"))
        self._setup_help_menu(menu_bar.addMenu("&Help"))

    def _setup_file_menu(self, file_menu: QMenu): #add file operations to the File menu
        actions = [
            (self._create_new_campaign_action(), None),
            (self._create_load_save_action(), None),
            (self._create_save_action(), None),
            (None, None), #this acts as a separator
            (self._create_quit_action(), None)
        ]

        self._add_actions_to_menu(file_menu, actions)

    def _setup_help_menu(self, help_menu: QMenu): #adding help-related actions to the help menu
        about_action = QAction("&About", self)
        about_action.triggered.connect(self._show_about_dialog)
        help_menu.addAction(about_action)

    def _add_actions_to_menu(self, menu: QMenu, actions: list):
        #adds list of actions or even separators to menu.
        for action, _ in actions:
            if action is None:
                menu.addSeparator()
            else:
                menu.addAction(action)

    def _create_new_campaign_action(self) -> QAction:
        #creatE "New Campaign" menu action
        action = QAction("&New Campaign", self)
        action.setShortcut(MENU_SHORTCUTS["new"])
        action.triggered.connect(self._on_new_campaign)
        return action
    
    def _create_load_save_action(self) -> QAction:
        #create "Load Save" menu action
        action = QAction("&Load Save", self)
        action.setShortcut(MENU_SHORTCUTS["load"])
        action.triggered.connect(self._on_load_save)
        return action
    
    def _create_save_action(self) -> QAction:
        #create "Save Campaign" menu action
        action = QAction("&Save Campaign", self)
        action.setShortcut(MENU_SHORTCUTS["save"])
        action.triggered.connect(self._on_save)
        return action
    
    def _create_quit_action(self) -> QAction:
        #create "Quit"
        action = QAction("Quit", self)
        action.setShortcut(MENU_SHORTCUTS["quit"])
        action.triggered.connect(self.close)
        return action
    
    def _create_tab_widget(self):
        #created the tab widget with placeholder tabs.
        self._tabs = QTabWidget()
        self._tabs.setTabPosition(QTabWidget.TabPosition.North)
        self._tabs.setDocumentMode(True)

        #adding some placeholder tabs
        for tab_name in TAB_NAMES:
            self._tabs.addTab(QWidget(), tab_name)

        self._root_layout.addWidget(self._tabs)

    def _create_status_bar(self):
        #initializing the status bar with the "ready" message //STATUS_READY_MESSAGE//
        self._status_bar = QStatusBar()
        self.setStatusBar(self._status_bar)
        self._status_bar.showMessage(STATUS_READY_MESSAGE)

#the event handlers for this app
    def _on_new_campaign(self):
        #handles the NEW CAMPAIGN menu action + LOAD + SAVE
        self._status_bar.showMessage("NEW CAMPAIGN (COMING SOON)")

    def _on_load_save(self):
        self._status_bar.showMessage("LOAD SAVE (COMING SOON)")

    def _on_save(self):
        self._status_bar.showMessage("SAVE")

    def _show_about_dialog(self):
        #handles the ABOUT menu action
        self._status_bar.showMessage(f"Solo DnD Adventures unreleased ver0.1.0")