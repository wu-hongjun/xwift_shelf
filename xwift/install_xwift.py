# Windows
def install_windows():
    import deploy_xwift_windows
    deploy_xwift_windows.main_setup(verbose=True)


# macOS
def install_macos():
    import deploy_xwift_macos
    deploy_xwift_macos.main_setup(verbose=True)


install_windows()
