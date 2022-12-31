# Only run this outside of Maya. Used to get REPO_PATH
# import os
# print(os.path.abspath(os.getcwd()).replace("\\", "/"))

# Reload Utility
import reload_util
import maya.cmds as cmds

# Reload Codebase
REPO_PATH = "C:/Users/hongj/PycharmProjects/Xwift/xwift/"
reload_util.reload_from_playground(REPO_PATH)



# Run code
from con_library import library_ui

ui = library_ui.showUI()
