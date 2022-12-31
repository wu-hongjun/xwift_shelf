# Hongjun Wu
# Asset Library is a neat tool to save all the regularly used controllers to be reused later.

import maya.cmds as cmds
import os
import json
import pprint

USER_APP_DIR = cmds.internalVar(userAppDir=True)
DIRECTORY = os.path.join(USER_APP_DIR, "asset_library")


def create_directory(directory=DIRECTORY):
    """
    This function creates the given directory if it does not exist already.
    Args:
        directory: (str) The directory to create.
    """
    # Check if the directory does not exist.
    if not os.path.exists(directory):
        # If it does not exist, we will make the directory.
        os.mkdir(directory)


class AssetLibrary(dict):

    def save(self, name, directory=DIRECTORY, screenshot=True, **info):
        """
        Save the selected asset in the scene.
        If nothing is selected, it will save the entire scene as one asset.

        Args:
            name: (str) The name of the asset.
            directory: (str) The location where all assets are stored, USER_APP_DIR/asset_library/.
            screenshot: (boolean) Whether to save the screenshot of the asset, by default is True.
            **info: Any additional information is saved into the json data file.
        """
        # Create the directory just to make sure it exists.
        create_directory(directory)

        # The path of the output maya file.
        path = os.path.join(directory, "%s.ma" % name)
        # The path of the output json file that saves any info.
        info_file = os.path.join(directory, "%s.json" % name)

        # Store the essential information in the info dictionary.
        info["name"] = name
        info["path"] = path

        # We rename the file to where we want to save it in.
        cmds.file(rename=path)

        # If something is selected, only export the selection.
        # Else save the entire file.
        if cmds.ls(selection=True):
            cmds.file(force=True, type="mayaAscii", exportSelected=True)
        else:
            cmds.file(save=True, type="mayaAscii", force=True)

        if screenshot:
            info["screenshot"] = self.save_screenshot(name, directory=directory)

        # Dump all possible data the user might pass into save().
        # Indent 4 spaces so it is easy to read.
        with open(info_file, "w") as f:
            json.dump(info, f, indent=4)

        # Since the class is a dictionary, it can save data to itself.
        self[name] = info

    def find(self, directory=DIRECTORY):
        """
        Gather all saved assets and index them to be shown in the UI.

        Args:
            directory: (str) The location where all assets are stored, USER_APP_DIR/asset_library/.
        """
        self.clear()

        # Return if the directory does not exist.
        if not os.path.exists(directory):
            return

        # Get all maya files in that directory.
        files = os.listdir(directory)

        # Filter out all Maya Ascii files.
        maya_files = [f for f in files if f.endswith(".ma")]

        # Add all the maya files into self since self is a dict.
        for ma in maya_files:
            # Get the name and file extension of the file.
            name, ext = os.path.splitext(ma)
            path = os.path.join(directory, ma)

            # Construct the name of the json file.
            info_file = "%s.json" % name

            # If the info_file exists, construct the fill path and try to load it in.
            if info_file in files:
                info_file = os.path.join(directory, info_file)

                with open(info_file, "r") as f:
                    info = json.load(f)
                    pprint.pprint(info)

            else:
                info = {}

            screenshot = "%s.jpg" % name
            if screenshot in files:
                info["screenshot"] = os.path.join(directory, name)

            # Store some basic information.
            info["name"] = name
            info["path"] = path

            self[name] = info

    def load(self, name):
        """
        Load the controller with the given name.
        Args:
            name: (str) The name of the desired object to import.
        """
        path = self[name]["path"]
        cmds.file(path, i=True, usingNamespaces=False)  # Import the file into the scene. i=import

    def save_screenshot(self, name, directory=DIRECTORY):
        """
        Save the screenshot of the object in the directory.
        Args:
            name: (str) Name of the object.
            directory: (str) Directory of the object.

        Returns: The path of the saved screenshot image.

        """
        path = os.path.join(directory, "%s.jpg" % name)

        # Fit the viewport to the selected file to get the best pic
        cmds.viewFit()
        # Set image format to jpg.
        cmds.setAttr("defaultRenderGlobals.imageFormat", 8)

        # Generate an image from the viewport.
        cmds.playblast(completeFilename=path, forceOverwrite=True, format="image", width=200, height=200,
                       showOrnaments=False, startTime=1, endTime=1, viewer=False)
        return path
