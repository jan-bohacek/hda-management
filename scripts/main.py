import sys
from PySide6.QtWidgets import QApplication
from treeView_ui import TreeViewWindow

def open_tree_view():
    app = QApplication(sys.argv)

    # if QtCore.QCoreApplication.instance():
    #     app.quit()

    window = TreeViewWindow()
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    open_tree_view()