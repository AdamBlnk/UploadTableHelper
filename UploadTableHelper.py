import re, sys, time
from scriptSelector import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFileDialog, QTextEdit, QScrollArea, QComboBox
from PyQt5.QtCore import Qt


# Slot method to handle file selection
def SelectFile():
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileDialog = QFileDialog()
    filename, _ = fileDialog.getOpenFileName(window, "Select Excel File", "", "Excel Files (*.xlsx *.xls)", options=options)

    # if file actually chosen, do the thing
    if filename:
        # This takes the file path and only uses the last bit to get the filename
        pattern = r"/([^/]+)$"
        matches = re.findall(pattern, filename)

        # display just the filename, without the whole path, and strip the ['square brackets and single quotes']
        filePathLabel.setText(f"File selected: {matches[0].strip()}")

    # save the whole path to window.filename
    window.filename = filename


# Slot method that loads the script selected in the dropdown menu
def ConfirmPress():
    selection = dropdown.currentText()

    # if no file selected, return nothing and do nothing
    if window.filename == '':
        return
    
    # Go into a switch statement to figure out which script to load
    else:
        match selection:
            case "Add Text To Start Of Cell":
                AddTextToCellBeginning(str(window.filename))

            case "Placeholder Option":
                return






# Declare the scripts to be listed
frontOfCell = scriptSelector("Add Text To Start Of Cell", "This script will add text to the front of a range of cells, such as ASSET IDs")

# Add the scripts to a list
scriptList = [frontOfCell] 
# More to be added
# More to be added
# More to be added




# Create a QWidget as the main window
app = QApplication(sys.argv)
window = QWidget()
window.filename = ""

# Create the dropdown of scripts, more to be added 
dropdown = QComboBox()
dropdown.addItem(scriptList[0].name)
dropdown.addItem("Option 2")
dropdown.addItem("Option 3")
dropdown.addItem("Option 4")
dropdown.addItem("Option 5")

# Set the initial selection
dropdown.setCurrentIndex(0)
# Set the position and size of the combo box
dropdown.setGeometry(50, 50, 50, 30)



# Labels created here
filePathLabel = QLabel("File selected: ")
actionLabel = QLabel("Select an action")

# Buttons created here
# set fixed size (width, height)
fileSelectButton = QPushButton("Select Excel File")
fileSelectButton.setFixedSize(100, 25)
confirmButton = QPushButton("Confirm")
confirmButton.setFixedSize(100, 25)


# Create QVBoxLayout and QHBoxLayout instances
vbox = QVBoxLayout()
vbox.setAlignment(Qt.AlignTop)
# AlignTop will not be seen for an autocomplete thru VSCode
hbox = QHBoxLayout()
hbox.setAlignment(Qt.AlignTop)


# Create the layout / add widgets here
vbox.addWidget(filePathLabel)
vbox.addWidget(fileSelectButton)

hbox.addWidget(dropdown)
hbox.addWidget(confirmButton)

vbox.addWidget(actionLabel)
vbox.addLayout(hbox)



# Connect the clicked signal of button1 to the select_file slot
fileSelectButton.clicked.connect(SelectFile)
confirmButton.clicked.connect(ConfirmPress)



# Set the QVBoxLayout as the main layout of the window
window.setLayout(vbox)

# Set the title of the window
window.setWindowTitle("Adam's Upload Table Helper")

# Set the initial window size
window.resize(400, 10)  # width, height

# Show the window
window.show()
sys.exit(app.exec_())