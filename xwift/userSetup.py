# start Xwift
import os
import platform
import sys

from maya import cmds


def get_latest_version(maya_folder):
    version_folders = []
    for x in os.listdir(maya_folder):
        try:
            folder = int(x)
            version_folders += [folder]
        except:
            pass
    return str(max(version_folders))


# Add the custom xwift path to a place where Maya can find.
# https://subscription.packtpub.com/book/business/9781785283987/1/ch01lvl1sec15/adding-custom-folders-to-your-script-path
def add_xwift_script_path():
    PLAT = str(platform.system())
    if "Darwin" in PLAT:
        USER = os.environ["HOME"]
        MAYA_FOLDER = "{0}/Library/Preferences/Autodesk/Maya/".format(USER)
    else:
        USER = os.getenv("USERPROFILE").replace('\\', '/')
        MAYA_FOLDER = "{0}/Documents/maya/".format(USER)

    MAYA_VERSION = get_latest_version(MAYA_FOLDER)
    xwift_script_path = "{0}{1}/scripts/".format(MAYA_FOLDER, MAYA_VERSION) + "xwift"
    if xwift_script_path not in sys.path:
        sys.path.append(xwift_script_path)
        print("Appended xwift script to sys.path: " + xwift_script_path)
    else:
        print("sys.path already exists xwift script path: " + xwift_script_path)


if not cmds.about(batch=True):
    add_xwift_script_path()  # Add Xwift script path so the script folder is nice and tidy.
    cmds.evalDeferred("import xwift_shelf; xwift_shelf.xwiftshelf()")  # Load Xwift Shelf
# end Xwift

