from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QScrollArea, QDialog, QTextEdit, QLabel, QLineEdit, QFormLayout
from PyQt5.QtCore import Qt
from openpyxl import load_workbook


class scriptSelector:
    name, desc = "", ""
    
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc



def AddTextToCellBeginning(excelPath):
    # load the workbook and get the first sheet (Assets sheet)
    wb = load_workbook(excelPath)
    mySheet = wb.worksheets[0]

    # New window beginnings
    dialog = QDialog()
    dialog.setWindowTitle("Add Text To The Beginning of the Cell")

    # Buttons
    previewButton = QPushButton("Preview Changes")
    previewButton.setFixedSize(100, 25)
    confirmButton = QPushButton("Confirm")
    confirmButton.setFixedSize(100, 25)

    # Labels
    cellLabel = QLabel("Cell columns:")
    phraseLabel = QLabel("Phrase to insert:")

    # User input boxes (QLineEdit)
    cellEdit = QLineEdit()
    phraseEdit = QLineEdit()

    # Scroll area 
    scrollArea = QScrollArea()
    textEdit = QTextEdit()
    textEdit.setReadOnly(True)
    scrollArea.setWidgetResizable(True)
    scrollArea.setWidget(textEdit)

    # Grid to hold the Labels, Edits, and Buttons
    grid = QFormLayout()
    grid.addRow(cellLabel, cellEdit)
    grid.addRow(phraseLabel, phraseEdit)
    grid.addRow(previewButton, confirmButton)
    grid.setAlignment(confirmButton, Qt.AlignRight)

    # Layout boxes
    vbox = QVBoxLayout()
    vbox.setAlignment(Qt.AlignTop)

    vbox.addLayout(grid)
    vbox.addWidget(scrollArea)

    # Set the layout to the vbox
    dialog.setLayout(vbox)

    # Set the initial window size
    dialog.resize(400, 200)  # width, height
    dialog.exec_()