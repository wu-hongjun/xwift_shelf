# Xwift Shelf
> Hongjun Wu

## Introduction

Xwift Shelf is the backbone technology that powers Hongjun's Xwift toolkit.
It makes developing for Maya so much easier.

Xwift Shelf gives you three benefits:
* A modern and flexible Maya shelf written in Python 3.
* Automatically reload any code you wrote in the repository into Maya.
* Ability to develop in PyCharm and manage code using Git.

Additionally, I also included a Asset Manager to manage your digital assets in Maya, both as an example of how to embed fairly advanced scripts into the shelf and as a useful tool to have.

## How To: Setup
* For first time users, run `deploy_xwift.py` in Pycharm.
* Make sure you installed MayaCharm plugin in Pycharm, which is not a part of Xwift but necessary for it to run.
* Open `playground.py`, uncomment line 4-8, and run the script.
* A file path like `"C:/Users/hongj/PycharmProjects/Xwift/xwift/"` will appear in the PyCharm output.
* Enter this path into the `REPO_PATH` variable in `playground.py`. You may now delete line 4-8 for a cleaner playground.

## How To: Daily Development
* You may now write any script and modules in their corresponding scripts in the `/scripts` folder.
* To run them, simply write a function call in `playground.py` similar to the example I gave, and `Alt+A` to pass the call into Maya.
* Xwift will do all the dirty job and automatically install, reload, and refresh your script into Maya.
* Once you are happy with your code, make it a button into the shelf and you are all done!