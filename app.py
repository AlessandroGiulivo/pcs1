from PySide.QtGui import *

# creates a Qt application
app = QApplication([])

# creates a window
window = QWidget()

# creates a layout
layout = QVBoxLayout()

# creates two buttons
button1 = QPushButton('Exit')
button2 = QPushButton('Print')

# adds the buttons to the layout
layout.addWidget(button1)
layout.addWidget(button2)

# sets the title and the dimensions of the window
window.resize(500,300)
window.setWindowTitle('Principles of Computer Science')

# sets the layout
window.setLayout(layout)

# defines a simple callback
def print_callback():
    print 'hello'

# sets the callbacks for the "clicked" event of the two buttons
button1.clicked.connect(app.quit)
button2.clicked.connect(print_callback)

# shows the window
window.show()

# starts the interaction with the user
app.exec_()
