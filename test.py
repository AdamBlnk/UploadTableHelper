import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton

def create_main_window():
    main_window = QMainWindow()
    main_window.setWindowTitle("Main Window")

    # Create a central widget and layout
    central_widget = QWidget()
    main_layout = QVBoxLayout(central_widget)

    # Create a form layout to arrange the line edits
    form_layout = QFormLayout()

    # Create line edits and add them to the form layout
    line_edit_1 = QLineEdit()
    line_edit_2 = QLineEdit()
    line_edit_3 = QLineEdit()
    form_layout.addRow("Fiesssssssld 1:", line_edit_1)
    form_layout.addRow("Fissssseld 2:", line_edit_2)
    form_layout.addRow("Field 3:", line_edit_3)

    # Set fixed width for line edits
    line_edit_1.setFixedWidth(200)
    line_edit_2.setFixedWidth(200)
    line_edit_3.setFixedWidth(200)

    # Add the form layout to the main layout
    main_layout.addLayout(form_layout)

    # Create a button
    button = QPushButton("Submit")
    main_layout.addWidget(button)

    # Set the central widget
    main_window.setCentralWidget(central_widget)

    return main_window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = create_main_window()
    main_window.show()
    sys.exit(app.exec())
