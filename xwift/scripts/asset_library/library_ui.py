import pprint

from maya import cmds

import asset_library
from Qt import QtWidgets, QtCore, QtGui
# from PySide2 import QtWidgets, QtCore, QtGui


class AssetLibraryUI(QtWidgets.QDialog):
    """
    The AssetLibraryUI is a dialog that lets us save and import controllers
    """
    def __init__(self):
        # Run the parent class (QDialog)'s __init__ method.
        super(AssetLibraryUI, self).__init__()

        self.setWindowTitle("Asset Library UI")

        # The library variable points to an instance of our controller library
        self.library = asset_library.asset_library.AssetLibrary()

        # Every time we create a new instance, we will automatically build the ui and populate it.
        self.build_ui()
        self.populate()

    def build_ui(self):
        """
        This method builds out the UI.

        Returns:

        """
        # Master layout
        layout = QtWidgets.QVBoxLayout(self)

        # Child horizontal widget
        save_widget = QtWidgets.QWidget()
        save_layout = QtWidgets.QHBoxLayout(save_widget)
        layout.addWidget(save_widget)

        self.save_name_field = QtWidgets.QLineEdit()
        save_layout.addWidget(self.save_name_field)

        save_btn = QtWidgets.QPushButton("Save")
        save_btn.clicked.connect(self.save)
        save_layout.addWidget(save_btn)

        # These are the parameters for our thumbnail size
        size = 64
        buffer = 12

        # This will create a grid list widget to display our controller thumbnails
        self.list_widget = QtWidgets.QListWidget()
        self.list_widget.setViewMode(QtWidgets.QListWidget.IconMode)
        self.list_widget.setIconSize(QtCore.QSize(size, size))
        self.list_widget.setResizeMode(QtWidgets.QListWidget.Adjust)
        self.list_widget.setGridSize(QtCore.QSize(size+buffer, size+buffer))
        layout.addWidget(self.list_widget)

        # This is the child widget that adds all the buttons.
        btn_widget = QtWidgets.QWidget()
        btn_layout = QtWidgets.QHBoxLayout(btn_widget)
        layout.addWidget(btn_widget)

        import_btn = QtWidgets.QPushButton("Import!")
        import_btn.clicked.connect(self.load)
        btn_layout.addWidget(import_btn)

        refresh_btn = QtWidgets.QPushButton("Refresh")
        refresh_btn.clicked.connect(self.populate)  # Not populate() because we don't want to run it.
        btn_layout.addWidget(refresh_btn)

        close_btn = QtWidgets.QPushButton("Close")
        close_btn.clicked.connect(self.close)
        btn_layout.addWidget(close_btn)

    def populate(self):
        """
        This clears the listWidget and repopulates it with the contents in the library.
        """
        self.list_widget.clear()
        self.library.find()

        for name, info in self.library.items():
            item = QtWidgets.QListWidgetItem(name)
            self.list_widget.addItem(item)

            screenshot = info.get("screenshot")
            if screenshot:
                icon = QtGui.QIcon(screenshot)
                item.setIcon(icon)

            item.setToolTip(pprint.pformat(info))

    def load(self):
        """
        This loads the currently selected controller.
        """
        current_item = self.list_widget.currentItem()
        if not current_item:
            return

        name = current_item.text()
        self.library.load(name)

    def save(self):
        """
        This saves the asset with the given file name.
        """
        name = self.save_name_field.text()
        if not name.strip():
            cmds.warning("You must give a name!")
            return

        self.library.save(name)
        self.populate()
        self.save_name_field.setText("")


def showUI():
    """
    This shows and returns a dialog UI.

    Returns: QDialog
    """
    ui = AssetLibraryUI()
    ui.show()
    return ui

