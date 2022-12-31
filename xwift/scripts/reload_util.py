import maya.cmds as cmds
import os
import logging
from importlib.util import module_from_spec, spec_from_file_location
from os.path import basename, isfile, join
import glob
import importlib


def reload_scripts_in_directory(directory):
    """
    Work in progress, not actually used in production.

    Recursively reload all the scripts in the directory as well as its subdirectories.

    Args:
        directory: (str) Maya directory that contains all the scripts.
    """

    from os.path import basename, isfile, join
    import glob
    import importlib
    import pathlib

    from pathlib import Path

    dir_path = Path(directory)
    assert dir_path.is_dir()

    file_list = []
    for x in dir_path.iterdir():
        if x.is_file():
            file_list.append(x)
        elif x.is_dir():
            file_list.extend(reload_scripts_in_directory(x))

    return file_list


def reload_scripts(directory, is_sub_directory=False):
    """
    Reload all the scripts in a directory.

    Note: Legacy implementation, will be replaced by a better recursive method.
    Limitation: Can only process one folder deep, that is, it cannot reload ~/scripts/foo/bar/script.py

    Args:
        directory: (str) The folder that contains all the scripts to be reloaded.
        is_sub_directory: (bool) A workaround to reload scripts in subdirectories of the main root.

    Returns:

    """
    try:
        # Get a list of all the scripts, dynamically.
        # Can't import dev tools by itself.
        modules = glob.glob(join(directory, "*.py"))
        excluded_scripts = tuple(["__init__.py", "developer_tools.py", "xwift_shelf.py"])
        all_scripts = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith(excluded_scripts)]

        # Import and reload all the scripts once again.
        for script in all_scripts:
            try:
                if is_sub_directory:
                    # This makes it able to reload scripts in a sub-folder.
                    # Admitting, it is not a good implementation.
                    # Limitation is it only works with one folder deep.
                    # But should be sufficient for what I need to write more complex modules now.
                    module = importlib.import_module(os.path.basename(os.path.normpath(directory)) + "." + script)
                else:
                    module = importlib.import_module(script)
                importlib.reload(module)
            except Exception as e:
                logging.error("[Reload Shelf] Failed to attempt reloading scripts in subdirectories with error: " + str(e))

    except Exception as e:
        logging.error("[Reload Shelf] Failed to attempt reloading scripts with error: " + str(e))


def reload_shelf():
    """
    reload_shelf: Reload all scripts.
    """

    from os.path import dirname, join, isdir

    root_dir = dirname(__file__)

    # Reload all scripts in the root directory.
    reload_scripts(root_dir)

    # Reload all scripts in the subdirectory.
    for file in os.listdir(root_dir):
        d = join(root_dir, file)
        if isdir(d):
            reload_scripts(d, is_sub_directory=True)

    # Rebuild the shelf, and reload all icons and plugins.
    cmds.evalDeferred("import xwift_shelf; xwift_shelf.xwiftshelf()")


def reload_shelf_from_shelf(self):
    """
    This wraps reload_shelf() into a function to call from a button press on the shelf.
    """
    reload_shelf()
    # Produce output in log and a popup window.
    print("[Reload Shelf] Xwift shelf and scripts reloaded successfully!")
    cmds.confirmDialog(title='Xwift Reload', message='Xwift shelf and scripts reloaded successfully!',
                       button=['Okie!'], defaultButton='Okie!', dismissString='Okie!')


def reinstall_scripts_from_repo(repository_path):
    """
    This copies all the scripts in your current development repo and overwrites them in the Maya Script Path.

    Args:
        repository_path:

    Returns:

    """
    install_script_path = repository_path + "deploy_xwift.py"
    spec = spec_from_file_location("deploy_xwift", install_script_path)

    # creates a new module based on spec
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    module.deploy()


def reload_from_playground(repository_path):
    if repository_path != "" and repository_path is not None:
        # Set MayaCharm Port
        if not cmds.commandPort(':4434', q=True):
            cmds.commandPort(n=':4434')

        reinstall_scripts_from_repo(repository_path)
        reload_shelf()
        logging.info("Successfully reloaded Xwift from playground.")
