# install_xwift.py
# Installs xwift shelf and its required files into the newest version of maya's /scripts folder.

import os
from sys import platform
import shutil
import logging
from datetime import datetime

# Info about this version of installer.
VERSION = "1.0.0"
BUILD = "20221203"
NEW = "Universal Xwift deploy class."

logging.basicConfig(level=logging.WARNING)


def get_date_time():
    """
    Returns the current date and time for logging purposes.

    Returns:
        (str) Date time in YearMonthDay HourMinuteSecond.

    """
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S")


def copy_and_overwrite(from_path, to_path):
    """
    General behavior: Copies one directory and overwrites it to another directory.

    Used to overwrite fresh code in Maya script folder.

    Args:
        from_path: (str) Path contain Xwift code from a repository.
        to_path: (str) Path that Maya will write when startup.
    """
    if not from_path:
        logging.info("copy_and_overwrite(): from_path in {0} is invalid.".format(from_path))
    if not to_path:
        logging.info("copy_and_overwrite(): to_path in {0} is invalid.".format(to_path))

    if from_path and to_path:
        if os.path.exists(to_path):
            shutil.rmtree(to_path)
            logging.info("Removed directory in: " + to_path)

        shutil.copytree(from_path, to_path)
        logging.info("Copied directory from {0} to {1}.".format(from_path, to_path))


def filter_ext(directory, ext):
    """
    filters out files in a directory with the same extension
    and returns a list of filenames that contains the list of filenames.

    Args:
        directory: (str) The directory it scans.
        ext: (str) Extension it looks for.

    Returns: (list(str)) A list of all files in the given directory that ends with the extension.
    """
    file_list = []
    for basename in os.listdir(directory):
        if basename.endswith(ext):
            file_list.append(basename)
    return file_list


class DeployBase(object):
    override_version = None
    maya_version = None

    maya_dir = None
    maya_script_dir = None
    maya_script_cache_dir = None
    maya_plugin_dir = None
    ffmpeg_dir = None

    xwift_dir = None
    xwift_shelf_dir = None
    xwift_script_dir = None
    xwift_icon_dir = None

    def __init__(self):
        self.xwift_dir = str(os.path.dirname(os.path.abspath(__file__)))
        self.deploy()  # Call OS specific deployment procedure.

    def deploy(self):
        # To be implemented by OS specific children classes.
        pass

    def set_maya_dir(self):
        # To be implemented by OS specific children classes.
        pass

    def install_user_setup(self):
        # To be implemented by OS specific children classes.
        pass

    def set_file_paths(self):
        # To be implemented by OS specific children classes.
        pass

    def set_maya_version(self):
        """
        Sets the Maya version to work in.
        Automatically looks for the newest version of Maya and sets self.maya_version (e.g. "2023").
        Can be overridden by self.override_version (e.g. "2017").
        """
        # Handle override Maya version.
        self.maya_version = str(self.override_version) if self.override_version else None

        # Normal operation, finding the newest Maya version based on year.
        if self.maya_dir:
            version_folders = []
            try:
                for x in os.listdir(self.maya_dir):
                    try:
                        folder = int(x)
                        version_folders += [folder]
                    except ValueError:
                        pass  # The directory name cannot be cast to int, aka not a folder with year names.
            except FileNotFoundError:
                logging.error("Cannot find the maya documents folder. "
                              "Please run Maya at least once before installing Xwift.")
            self.maya_version = str(max(version_folders))

    def set_file_paths(self):
        """
        Sets non-operating system Specific relative file paths.
        For operating system specific paths, subclasses implement in their corresponding set_maya_dir().
        """
        if self.maya_version:
            self.xwift_shelf_dir = self.xwift_dir + "/scripts/xwift_shelf.py"
            self.xwift_script_dir = "{0}{1}/scripts/xwift".format(self.maya_dir, self.maya_version)
            self.xwift_icon_dir = "{0}{1}/prefs/icons/xwift/".format(self.maya_dir, self.maya_version)

            self.maya_script_dir = "{0}{1}/scripts/xwift".format(self.maya_dir, self.maya_version)
            self.maya_script_cache_dir = "{0}{1}/scripts/__pycache__".format(self.maya_dir, self.maya_version)
            self.maya_plugin_dir = "{0}{1}/plug-ins/".format(self.maya_dir, self.maya_version)
            self.ffmpeg_dir = "{0}{1}/ffmpeg/".format(self.maya_dir, self.maya_version).replace("/", "\\")

    def install_user_setup(self):
        """
        Install userSetup.py to the location that starts with Maya.
        """
        if self.maya_dir:
            # The example UserSetup that contain Xwift launcher code.
            xwift_user_setup_path = os.path.dirname(os.path.abspath(__file__)) + "\\userSetup.py"

            # Target UserSetup that Maya will read when starting.
            user_setup_path = self.maya_dir + "scripts/userSetup.py"

            if os.path.exists(user_setup_path):
                logging.warning("UserSetup.py already exists, "
                                "you might need to manually configure Xwift in your UserSetup.")
            else:
                shutil.copyfile(xwift_user_setup_path, user_setup_path)

    def install_xwift(self):
        """
        Copy Xwift resources from the repository to Maya's corresponding installation directory.
        So it will be read by Maya on startup.
        """
        if self.xwift_dir:
            try:
                copy_and_overwrite(self.xwift_dir + "\\scripts", self.maya_script_dir)
                copy_and_overwrite(self.xwift_dir + "\\plug-ins", self.maya_plugin_dir)
                copy_and_overwrite(self.xwift_dir + "\\icons", self.xwift_icon_dir)
                copy_and_overwrite(self.xwift_dir + "\\ffmpeg", self.ffmpeg_dir)
                logging.info("Successfully installed all components of Xwift.")
            except Exception as err:
                logging.error("Installation aborted with error: " + err)

    def delete_script_cache(self):
        """
        Removes Maya's pre-compiled Python cache folder to avoid Maya referencing old script cache.
        """
        if self.maya_script_cache_dir:
            try:
                shutil.rmtree(self.maya_script_cache_dir)
            except OSError:
                pass  # No pre-compiled python cache to clear.


class DeployWindows(DeployBase):

    def deploy(self):
        """
        Deployment procedure for Windows.
        """
        self.set_maya_dir()
        self.set_maya_version()
        self.set_file_paths()
        self.install_user_setup()
        self.install_xwift()
        self.delete_script_cache()

    def set_maya_dir(self):
        """
        Sets self.maya_dir for Windows.
        """
        user = os.getenv("USERPROFILE").replace('\\', '/')
        self.maya_dir = "{0}/Documents/maya/".format(user)


class DeployMacOS(DeployBase):
    def deploy(self):
        """
        Deployment procedure for macOS.
        """
        self.set_maya_dir()
        self.set_maya_version()
        self.set_file_paths()
        self.chinese_localization()
        self.install_user_setup()
        self.install_xwift()
        self.delete_script_cache()

    def set_maya_dir(self):
        """
        Sets self.maya_dir for macOS.
        """
        user = os.environ["HOME"]
        self.maya_dir = "{0}/Library/Preferences/Autodesk/Maya/".format(user)

    def chinese_localization(self):
        """
        Simplified Chinese (zh_CN) Support.
        """
        if os.path.isdir("{0}{1}/zh_CN/".format(self.maya_dir, self.maya_version)):
            # If macOS is in Chinese, Maya will actually look for stuff in a different folder, this takes care of it.
            logging.warning("System is in Chinese, will also install into the /zh_CN directory.")
            self.maya_script_dir = "{0}{1}/zh_CN/scripts/".format(self.maya_dir, self.maya_version)
            self.maya_script_cache_dir = "{0}{1}/zh_CN/scripts/__pycache__".format(self.maya_dir, self.maya_version)
            self.maya_plugin_dir = "{0}{1}/zh_CN/plug-ins/".format(self.maya_dir, self.maya_version)
            self.xwift_icon_dir = "{0}{1}/zh_CN/prefs/icons/xwift/".format(self.maya_dir, self.maya_version)
            self.ffmpeg_dir = "{0}{1}/zh_CN/ffmpeg/".format(self.maya_dir, self.maya_version)

    def install_pymel(self):
        """
        Install pymel on macOS.
        Because unlike Windows, pymel is not bundled in installation on macOS.
        """
        print("NOTE: You might need to install pymel.")
        print("NOTE: Fortunately, all you need is to let Xwift know!")

        if input("Do you want to install pymel? We'll need your computer's password. (Y/N)").lower() == "y":
            try:
                repo_dir = str(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')))
                pymel_dir = repo_dir + "/packages/pymel-1.2.0"
                mayapy_dir = "/Applications/Autodesk/maya" + self.maya_version + "/Maya.app/Contents/bin/mayapy"
                os.system("cd " + pymel_dir + "; sudo -S " + mayapy_dir + " setup.py install")
                logging.info("Successfully installed pymel.")
            except Exception as exc:
                logging.error("Error occurred while attempting to install pymel: " + exc)
        else:
            print("[PYMEL ] Okie gotya! Will not install pymel.")


def deploy(extra_steps=False):
    """
    Deploys all resources of Xwift to Maya's script folder to load on startup.
    Can be called by reload_util for active reload or run directly.
    Can specify to perform extra steps for first time deployment.

    Args:
        extra_steps: (boolean) Perform extra steps (e.g. install pymel on macOS) for first time deployment.
    """
    xwift_shelf_dir = os.path.dirname(os.path.abspath(__file__)) + "/scripts/xwift_shelf.py"
    if os.path.isfile(xwift_shelf_dir):
        # Automatically deploy Xwift based on OS type.
        if platform == "win32":
            DeployWindows()
        elif platform == "darwin":
            task = DeployMacOS()
            if extra_steps:
                task.install_pymel()  # Prompt the user to install pymel if deploying for the first time.
        elif platform == "linux" or platform == "linux2":
            pass  # Unimplemented
    else:
        logging.error("Cannot find the xwift shelf file.")


if __name__ == "__main__":
    """
    If running this file directly, default to first time deploy procedures.
    Keyword direct_run tells deploy() to perform extra steps (e.g. install pymel on macOS) for first time deployment.
    """
    # Deploy all the code.
    deploy(extra_steps=True)
