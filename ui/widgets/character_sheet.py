#setting up essential libraries as well as the constants used in 
# core/character.py

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QLineEdit, QTextEdit, QCheckBox, QSpinBox,
    QComboBox, QFrame, QScrollArea, QSizePolicy,
    QPushButton, QGroupBox
)

from PyQt6.QtGui import (
    QFont, QColor, QPalette, QIntValidator,
    QPainter, QPen, QBrush, QLinearGradient, QFontDatabase
)

from PyQt6.QtCore import Qt, pyqtSignal, QSize

from core.character import (
    Character, ABILITIES, SKILL_ABILITY_MAP,
    PLAYABLE_RACES, RACE_BONUSES,
    PERSONALITY_TRAIT_PRESENTS, IDEAL_PRESETS,
    BOND_PRESETS, FLAW_PRESETS,
    FEATURE_PRESETS, PROFICIENCY_LANGUAGE_PRESETS,
)

# color palette and fonts
# I am going to achieve some medieval fantasy color palettes, where it will
# used everywhere using these constants:
COL_BG              = "#1a1714"         #the background color
COL_SURFACE         = "#242018"         #slightly lighter surface color
COL_CARD            = "#2c2620"         #border accent color, slightly lighter
COL_BORDER          = "#6b5a3e"         #aged leather border color
COL_BORDER_LIGHT    = "#8a7455"         #lighter border accent
COL_GOLD            = "#c9a84c"         #primary gold accent color
COL_GOLD_LIGHT      = "#e8c97a"         #bright gold color for highlights
COL_TEXT_PRIMARY    = "#e8dcc8"         #warm primary text
COL_TEXT_MUTED      = "#9a8a70"         #muted label text color accent
COL_TEXT_LABEL      = "#c4a96b"         #gold label text
COL_INPUT_BG        = "#1e1b16"         #input field background
COL_INPUT_BORDER    = "#4a3f2e"         #border of input field
COL_ACCENT_RED      = "#8b2020"         #health points or danger accent color
COL_ACCENT_BLUE     = "#1e4060"         #information accent color
COL_CHECK_ON        = "#c9a84c"         #proficiency checkbox active colors
COL_SCROLLBAR       = "#3a3020"         #scrollbar track

#CSS-like stylesheet, using used python libraries.
STYLESHEET = f"""
/* global colors */
QWidget {{
    background-color: {COL_BG};
    color: {COL_TEXT_PRIMARY};
    font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
    font-size: 12px;
}}
 
/* for the scroll areas */
QScrollArea {{
    border: none;
    background-color: {COL_BG};
}}
QScrollBar:vertical {{
    background: {COL_SCROLLBAR};
    width: 8px;
    border-radius: 4px;
}}
QScrollBar::handle:vertical {{
    background: {COL_BORDER};
    border-radius: 4px;
    min-height: 24px;
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0px;
}}
 
/* section group boxes */
QGroupBox {{
    border: 1px solid {COL_BORDER};
    border-radius: 4px;
    margin-top: 14px;
    padding: 6px 6px 6px 6px;
    background-color: {COL_CARD};
    font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    subcontrol-position: top center;
    padding: 0 6px;
    color: {COL_GOLD};
    font-size: 9px;
    font-weight: bold;
    letter-spacing: 2px;
    text-transform: uppercase;
}}
 
/* for line edits */
QLineEdit {{
    background-color: {COL_INPUT_BG};
    border: 1px solid {COL_INPUT_BORDER};
    border-radius: 3px;
    color: {COL_TEXT_PRIMARY};
    padding: 3px 6px;
    selection-background-color: {COL_GOLD};
    selection-color: {COL_BG};
    font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
}}
QLineEdit:focus {{
    border: 1px solid {COL_GOLD};
    background-color: #221e18;
}}
QLineEdit:read-only {{
    background-color: {COL_SURFACE};
    color: {COL_GOLD_LIGHT};
    border: 1px solid {COL_BORDER};
}}
 
/* text edits */
QTextEdit {{
    background-color: {COL_INPUT_BG};
    border: 1px solid {COL_INPUT_BORDER};
    border-radius: 3px;
    color: {COL_TEXT_PRIMARY};
    padding: 4px;
    font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
    font-size: 11px;
}}
QTextEdit:focus {{
    border: 1px solid {COL_GOLD};
}}
 
/* spin boxes */
QSpinBox {{
    background-color: {COL_INPUT_BG};
    border: 1px solid {COL_INPUT_BORDER};
    border-radius: 3px;
    color: {COL_TEXT_PRIMARY};
    padding: 2px 4px;
    font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
}}
QSpinBox:focus {{
    border: 1px solid {COL_GOLD};
}}
QSpinBox::up-button, QSpinBox::down-button {{
    background-color: {COL_BORDER};
    width: 14px;
    border-radius: 2px;
}}
QSpinBox::up-button:hover, QSpinBox::down-button:hover {{
    background-color: {COL_GOLD};
}}
 
/* combo boxes */
QComboBox {{
    background-color: {COL_INPUT_BG};
    border: 1px solid {COL_INPUT_BORDER};
    border-radius: 3px;
    color: {COL_TEXT_PRIMARY};
    padding: 3px 6px;
    font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
}}
QComboBox:focus {{
    border: 1px solid {COL_GOLD};
}}
QComboBox::drop-down {{
    border: none;
    width: 20px;
}}
QComboBox::down-arrow {{
    width: 10px;
    height: 10px;
    border-left: 4px solid transparent;
    border-right: 4px solid transparent;
    border-top: 6px solid {COL_GOLD};
}}
QComboBox QAbstractItemView {{
    background-color: {COL_CARD};
    border: 1px solid {COL_BORDER};
    color: {COL_TEXT_PRIMARY};
    selection-background-color: {COL_BORDER};
}}
 
/* checkboxes */
QCheckBox {{
    color: {COL_TEXT_MUTED};
    spacing: 4px;
}}
QCheckBox::indicator {{
    width: 12px;
    height: 12px;
    border-radius: 6px;
    border: 1px solid {COL_BORDER_LIGHT};
    background-color: {COL_INPUT_BG};
}}
QCheckBox::indicator:checked {{
    background-color: {COL_GOLD};
    border: 1px solid {COL_GOLD_LIGHT};
}}
 
/* for the buttons */
QPushButton {{
    background-color: {COL_CARD};
    border: 1px solid {COL_BORDER};
    border-radius: 3px;
    color: {COL_TEXT_LABEL};
    padding: 5px 12px;
    font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, serif;
    font-size: 11px;
    letter-spacing: 1px;
}}
QPushButton:hover {{
    background-color: {COL_BORDER};
    color: {COL_GOLD_LIGHT};
    border: 1px solid {COL_GOLD};
}}
QPushButton:pressed {{
    background-color: {COL_BG};
}}
 
/* labels */
QLabel {{
    background: transparent;
}}
"""