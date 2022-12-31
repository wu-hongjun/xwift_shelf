import reload_util

"""Uncomment the below and run for the first time to get REPO_PATH."""
# def get_repo_path():
#     """Used to get REPO_PATH. Only run this in PyCharm outside of Maya. """
#     import os
#     print(os.path.abspath(os.getcwd()).replace("\\", "/"))
# get_repo_path()  

REPO_PATH = ""  # e.g. "C:/Users/hongj/PycharmProjects/Xwift/xwift/"
reload_util.reload_from_playground(REPO_PATH)


# =============== Run your code below =============
from con_library import library_ui

ui = library_ui.showUI()
