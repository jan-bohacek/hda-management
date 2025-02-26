from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QTreeView, QPushButton
from PySide6.QtGui import QStandardItemModel, QStandardItem, QFont, QColor
from PySide6.QtCore import Qt
import os

class DirModel(QStandardItem):
    def __init__(self, text="", font_size=8):
        super().__init__()
        font = QFont("Open Sans", font_size)
        font.setBold(True)
        self.setFont(font)
        self.setText(text)
        self.setEditable(False)
        self.setData("dir", Qt.UserRole)

class FileModel(QStandardItem):
    def __init__(self, text="", font_size=8):
        super().__init__()
        font = QFont("Open Sans", font_size)
        self.setFont(font)
        self.setText(text)
        self.setEditable(False)
        self.setData("file", Qt.UserRole)
        self.setCheckable(True)
        self.checkSta

    def checked_color(self):
        self.setForeground(QColor(1,0,0))

class TreeViewWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tree View")
        self.setGeometry(100,100,400,600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # add menus
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction("Close", self.close)

        edit_menu = self.menuBar().addMenu("Edit")
        edit_menu.addAction("Undo", self.undo)
        edit_menu.addAction("Redo", self.redo)
        edit_menu.addSeparator()
        edit_menu.addAction("Cut", self.undo)
        edit_menu.addAction("Copy", self.undo)
        edit_menu.addAction("Paste", self.undo)

        view_menu = self.menuBar().addMenu("View")
        view_menu.addAction("Sort Ascending", lambda : self.sort_tree(tree_model, Qt.AscendingOrder))
        view_menu.addAction("Sort Descending", lambda : self.sort_tree(tree_model, Qt.DescendingOrder))

        # add tree
        tree_view = QTreeView()
        tree_view.setHeaderHidden(True)
        # tree_view.clicked.connect(self.print_selected)

        tree_model = QStandardItemModel()
        root_node = tree_model.invisibleRootItem()
        
        # populate tree
        path = "C:/Users/janbo/Documents/Projekty/practice/houdini/td/hda-management/_pipeline/_treeView/"
        root = root_node

        def list_dir(path, root):
            for i in os.listdir(path):
                i_path = f"{path}{i}"
                if os.path.isdir(i_path):
                    dir = DirModel(i)
                    root.appendRow(dir)
                    list_dir(f"{i_path}/", dir)
                if os.path.isfile(i_path):
                    file = FileModel(i)
                    root.appendRow(file)

        list_dir(path, root)

        tree_model.sort(0, order=Qt.AscendingOrder)

        tree_view.setModel(tree_model)

        # add buttons
        print_button = QPushButton("Print Selection")
        print_button.pressed.connect(lambda : self.print_checked(tree_model, root))
        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(print_button)

        # main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(tree_view)
        main_layout.addLayout(buttons_layout)
        central_widget.setLayout(main_layout)
        
    ### ACTIONS
    def sort_tree(self, model, order):
        model.sort(0, order)

    # print selected items
    def print_selected(self, value):
        print(value.data())
        print(value.parent().data())

    # print checked items
    def print_checked(self, model, root):
        checked_items = []
        stack = [root]
        while len(stack) > 0:
            item = stack.pop(0)
            if item.checkState() == Qt.CheckState.Checked:
                checked_items.append(item)
            for i in range(item.rowCount()):
                child = item.child(i)
                stack.append(child)
        # print checked
        print("SELECTED ITEMS:")
        for i in checked_items:
            print(i.text())

    def undo(self):
        print("Pressed undo!")

    def redo(self):
        print("Pressed redo!")

