import maya.cmds as cmds


def about():
    """
    About the current version of xwift.
    """
    intro = "Xwift Shelf is developed with love by Hongjun Wu. " \
            "Special thanks to Cody Wilcoxon, Rick Gilliland, and Alexander Xavier James " \
            "for helping me make Xwift possible. " \
            "Visit xwift.hongjunwu.com for documentations. "
    version = "1.0.0"
    last_updated = "Janurary 1, 2023"
    version_highlights = "Initial Release"
    copy_right = "\n\nWebsite: \nhongjunwu.com \n\nHongjun Wu, 2023, All rights reserved."

    message = intro + "\n\nCurrent Version: " + version + " (" + last_updated + "). \n\nVersion Highlights:\n" + version_highlights + copy_right

    cmds.confirmDialog(title='About Xwift',
                       message=message,
                       button=['OK'], messageAlign="center", defaultButton='OK', dismissString='OK')


def test():
    print("Hello world!")


