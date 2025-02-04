import sys
from PySide6 import QtCore, QtWidgets

# class TreeViewWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Tree View")
#         self.setGeometry(100,100,400,300)

class TreeViewWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tree View")
        self.setGeometry(100,100,400,300)

        menuBar = self.menuBar().addMenu("File")
        menuBar.addAction("Close", self.close)

        central_widget = QtWidgets.QLabel("This is a window label.", self)
        # central_widget.setAlignment(QtCore.Qt.AlignmentFlag())
        self.setCentralWidget(central_widget)

def main():
    app = QtWidgets.QApplication(sys.argv)

    # if QtCore.QCoreApplication.instance():
    #     app.quit()

    window = TreeViewWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()