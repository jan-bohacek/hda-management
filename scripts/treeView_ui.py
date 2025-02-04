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

        # add menus
        fileMenu = self.menuBar().addMenu("File")
        fileMenu.addAction("Close", self.close)

        editMenu = self.menuBar().addMenu("Edit")
        editMenu.addAction("Undo", self.undo)
        editMenu.addAction("Redo", self.redo)
        editMenu.addSeparator()
        editMenu.addAction("Cut", self.undo)
        editMenu.addAction("Copy", self.undo)
        editMenu.addAction("Paste", self.undo)
        

        central_widget = QtWidgets.QLabel("This is a window label.", self)
        # central_widget.setAlignment(QtCore.Qt.AlignmentFlag())
        self.setCentralWidget(central_widget)

    def undo(self):
        print("Pressed undo!")

    def redo(self):
        print("Pressed redo!")

def main():
    app = QtWidgets.QApplication(sys.argv)

    # if QtCore.QCoreApplication.instance():
    #     app.quit()

    window = TreeViewWindow()
    window.show()

    sys.exit(app.exec())

def loadTest():
    print("treeView module is loaded")

if __name__ == "__main__":
    main()