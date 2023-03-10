# Credit:
# Inspired by work from: https://bindpose.com/scripting-custom-shelf-in-maya-python/

import importlib
import maya.cmds as cmds
import reload_util


def _null(*args):
    pass


class _shelf():
    """
    A simple class to build shelves in maya. Since the build method is empty,
    it should be extended by the derived class to build the necessary shelf elements.
    By default, it creates an empty shelf called "customShelf".
    """

    def __init__(self, name="Xwift", iconPath=""):
        self.name = name

        self.iconPath = iconPath

        self.labelBackground = (0, 0, 0, 0)
        self.labelColour = (.9, .9, .9)

        self._clean_old_shelf()
        cmds.setParent(self.name)
        self.build()

    def build(self):
        """This method should be overwritten in derived classes to actually build the shelf
        elements. Otherwise, nothing is added to the shelf."""
        pass

    def add_button(self, label, icon="commandButton.png", command=_null, doubleCommand=_null, noLabel=False,
                   btn_annotation=""):
        """Adds a shelf button with the specified label, command, double click command and image."""
        cmds.setParent(self.name)
        if icon:
            icon = self.iconPath + icon

        if noLabel:
            cmds.shelfButton(width=37, height=37, image=icon, l=label, command=command, dcc=doubleCommand,
                           ann=btn_annotation)
        else:
            cmds.shelfButton(width=37, height=37, image=icon, l=label, command=command, dcc=doubleCommand,
                           imageOverlayLabel=label, olb=self.labelBackground, olc=self.labelColour, ann=btn_annotation)

    def add_menu_item(self, parent, label, command=_null, icon=""):
        """Adds a shelf button with the specified label, command, double click command and image."""
        if icon:
            icon = self.iconPath + icon
        return cmds.menuItem(p=parent, l=label, c=command, i="")

    def add_title_item(self, parent, label, command=_null, icon=""):
        """Adds a Shelf Title with the specified label, command, double click command and image."""
        if icon:
            icon = self.iconPath + icon
        return cmds.menuItem(p=parent, l=label, c=command, enable=False, i="")

    def add_sub_menu(self, parent, label, icon=None):
        """Adds a sub menu item with the specified label and icon to the specified parent popup menu."""
        if icon:
            icon = self.iconPath + icon
        return cmds.menuItem(p=parent, l=label, i=icon, subMenu=1)

    def _clean_old_shelf(self):
        """Checks if the shelf exists and empties it if it does or creates it if it does not."""
        if cmds.shelfLayout(self.name, ex=1):
            if cmds.shelfLayout(self.name, q=1, ca=1):
                for each in cmds.shelfLayout(self.name, q=1, ca=1):
                    cmds.deleteUI(each)
        else:
            cmds.shelfLayout(self.name, p="ShelfLayout")


###################################################################################

class xwiftshelf(_shelf):
    """
    The Xwift Shelf
    """

    def build(self):
        # Refresh the Xwift reload script
        importlib.reload(reload_util)

        # Example of a button with sub-menus.
        self.add_button(label="Sub-menu Example",
                        noLabel=True,
                        icon="xwift/xwift_animation_tools.png",
                        btn_annotation="Sub-menu Example")
        p = cmds.popupMenu(b=1)
        self.add_title_item(p, label="Sub-menu Example")

        sub = self.add_sub_menu(p, "Foo1")
        foo1 = self.add_sub_menu(sub, "Foo1")
        self.add_menu_item(foo1, label="Bar1",
                           command="import xwift_about; xwift_about.test()")
        self.add_menu_item(foo1, label="Bar2",
                           command="import xwift_about; xwift_about.test()")
        foo2 = self.add_sub_menu(sub, "Foo2")
        self.add_menu_item(foo2, label="Bar1",
                           command="import xwift_about; xwift_about.test()")
        self.add_menu_item(foo2, label="Bar2",
                           command="import xwift_about; xwift_about.test()")

        # Asset Manager
        # Example of a button that calls a script in a package.
        self.add_button(label="AssLib",
                        noLabel=True,
                        icon="xwift/xwift_iteration_tools.png",
                        command="from asset_lib import library_ui; ui = library_ui.showUI()",
                        btn_annotation="An asset library to manage reusable controllers and objects.")

        # About Xwift
        self.add_button(label="About",
                        noLabel=True,
                        icon="xwift/xwift_about.png",
                        command="import xwift_about; xwift_about.about()",
                        btn_annotation="About the current version of xwift.")


# Load xwift
xwiftshelf()
print("[Xwift Shelf]: Successfully loaded Xwift shelf!")

###################################################################################
