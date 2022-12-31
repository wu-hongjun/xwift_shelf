# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pymel',
 'pymel.api',
 'pymel.cache',
 'pymel.core',
 'pymel.internal',
 'pymel.tools',
 'pymel.tools.mel2py',
 'pymel.tools.scriptEditor',
 'pymel.util',
 'pymel.util.external',
 'pymel.util.external.ply']

package_data = \
{'': ['*'], 'pymel.tools': ['bin/*']}

install_requires = \
['future>=0.18']

entry_points = \
{'console_scripts': ['ipymel = pymel.tools.ipymel:main']}

setup_kwargs = {
    'name': 'pymel',
    'version': '1.2.0',
    'description': 'Python in Maya Done Right',
    'long_description': '\nPython in Maya Done Right\n=========================\n\nPyMEL makes python scripting with Maya work the way it should.\n\nMaya\'s command module is a direct translation of mel commands into python commands. The result is a very awkward and unpythonic syntax which does not take advantage of python\'s strengths -- particulary, a flexible, object-oriented design. PyMEL builds on the `maya.cmds` module by organizing its commands into a class hierarchy, and by customizing them to operate in a more succinct and intuitive way.\n\nProject Goals\n-------------\n\n- Create an open-source python module for Maya that is intuitive to MEL users and python users alike\n- Fix bugs and design limitations in Maya\'s python modues, maya.cmds and maya.mel\n- Keep code concise and readable\n- Add organization through class hierarchy and sub-modules\n- Provide documentation accessible via html and the builtin `help() function\n- Make it "just work"\n\nProduction Proven\n-----------------\n\nSince its release in 2008, PyMEL has accumulated an impressive resume in both feature films and games, and is now bundled with every release of Maya.\n\nHere\'s what Seth Gibson of Bungie Studios, makers of *Halo*, has to say:\n\n> Having done production python code myself for many years, wrapping my head around Maya\'s native implementation took a little bit of time. With PyMel, I can think and write the python code and syntax I\'m already used to, which speeds up my development time considerably. It\'s also going to help our other Technical Artists with their Python learning curve, since PyMEL\'s syntax is consistent with most other python packages. Kudos to the PyMel team for such a well thought out project!\n\nBSD License\n-----------\n\nPyMEL is released under the BSD license, which is as open as open source gets. Your studio can freely use, contribute to, and modify this module with no strings attached.\n\nFeatures\n--------\n\n### API Hybridization\n\nPyMEL harnesses the API to create a name-independent representation of your object. This means that the annoying inconsistencies of string comparisons are over: no more worrying about short names versus long names, DAG paths, unique paths, instance paths... it\'s all handled intelligently for you. And what\'s more, if anything causes the name of your object to change it will automatically be reflected in your python object.\n\nPyMEL node classes now include hundreds of new methods derived from the API, but with the same intuitive and unified design as before. With PyMEL you get the benefits of API speed and versatility without the advanced learning curve.\n\n### Improved Batch / Standalone Support\n\nEver wonder why python scripts that work in the Maya UI or in Maya batch don\'t work in Maya\'s python interpreter?  Here\'s a possible explanation: in both GUI and batch modes Maya sources all of its lowest-level MEL scripts, like those that load user plugins, whereas mayapy and `maya.initialize` does not.\n\nPyMEL ensures that Maya is properly initialized when used from Maya\'s python interpreter, which makes runtime environments more consistent and your scripts more portable, which adds up to fewer bugs.\n\n### Tighter MEL Integration\n\nExecuting a MEL script with arguments can be an unsightly mess when done the default way:\n\n**default**\n```python\nvalues = [\'one\', \'two\', \'three\', \'four\']\nmaya.mel.eval(\'stringArrayRemoveDuplicates({"\'+\'","\'.join(values)+\'"})\')\n```\n\nSo PyMEL provides a handy interface which makes calling MEL procedures just like calling a python function:\n\n**PyMEL**\n```python\nvalues = [\'one\', \'two\', \'three\', \'four\']\npm.mel.stringArrayRemoveDuplicates(values)\n```\n\nAlso, unlike `maya.mel.eval`, PyMEL will give you the specific MEL error message in a python traceback, along with line numbers:\n\n```python\n>>> mel.myScript(\'foo\', [])\nTraceback (most recent call last):\n    ...\nMelConversionError: Error occurred during execution of MEL script: line 2: Cannot convert data of type string[] to type float.\n```\n\nAlso, getting and setting MEL global variables is as easy as working with a dictionary:\n\n```python\nprint pm.melGlobals[\'gMainFileMenu\']\npm.melGlobals[\'gGridDisplayGridLinesDefault\'] = 2\n```\n\n### Powerful Classes\n\n#### Nodes\n\n```python\ncamTrans, cam = pm.camera()  # create a new camera\ncam.setFocalLength(100)\nfov = cam.getHorizontalFieldOfView()\ncam.dolly(-3)\ncam.track(left=10)\ncam.addBookmark(\'new\')\n```\n\n#### Attributes\n\n```python\ns = pm.polySphere()[0]\nif s.visibility.isKeyable() and not s.visibility.isLocked():\n    s.visibility.set(True)\n    s.visibility.lock()\n    print s.visibility.type()\n```\n\n#### File paths\n\nbackup all mb files in the current scene\'s directory\n\n```python\nbasedir = pm.sceneName().parent\nbackupDir = basedir / "backup" #slash op joins paths\nif not backupDir.exists:\n    backupDir.mkdir()\nfor path in basedir.files(\'*.mb\'):\n    print "backing up: ", path.name\n    path.copy(backupDir / (path.namebase + ".old"))\n```\n\n#### Shape components and vectors/matrices\n\nselect all faces that point up in world space\n\n```python\ns = pm.polySphere()[0]\nfor face in s.faces:\n    if face.getNormal(\'world\').y > 0.0:\n       pm.select(face, add=1)\n```\n\n#### optionVars dictionary\n\n```python\nif \'numbers\' not in pm.optionVar:\n    pm.optionVar[\'numbers\'] = [1, 24, 47]\npm.optionVar[\'numbers\'].append(9)\nnumArray = pm.optionVar.pop(\'numbers\')\n```\n\nWho is PyMEL for?\n-----------------\n\n### For the Novice\n\nObject-oriented programming, like that provided by PyMEL, is more intuitive to learn because the functionality of an object is directly associated with the object itself.\n\nFor an artist starting to program in Maya, the first question you might ask is "what can I do with this node?" Using a procedural approach, like that offered by MEL or maya.cmds, you\'ll have to dig through the thousands of MEL commands looking for the one that you want. For a camera node, the `camera` MEL command is easy to find, but did you find `orbit`, `track`, `dolly`, and `tumble`, which also work on cameras?  What about the API methods?\n\nIn PyMEL, all you have to do is type `help(nt.Camera)` in the python script editor to find out all the things a camera node can do, or just look up the Camera class in the PyMEL docs.\n\n### For the MEL Scripter\n\nWhen we say PyMEL is concise and easy to read, we mean it.\n\n***MEL***\n\n```mel\nstring $sel[] = `ls -sl`;\nstring $shapes[] = `listRelatives -s $sel[0]`;\nstring $conn[] = `listConnections -s 1 -d 0 $shapes[0]`;\nsetAttr ( $conn[0] + ".radius") 3;\n```\n\n***PyMEL***\n\n```python\npm.selected()[0].getShape().inputs()[0].radius.set(3)\n```\n\n### For the Technical Director\n\nFor those looking to master python in a production environment, PyMEL is more than a module for Maya scripting, it is a repository of example python code -- a self-contained pipeline demonstrating advanced python concepts like function factories, metaclasses, and decorators, as well as essential production practices such as parsing, pickling, logging, and unit testing.\n\nFor those who are already masters of python and who naturally expect more out of a python package, PyMEL is for you, too. It was written for use in production by experiened programmers with a vision for how to add object-oriented design to Maya.\n\nCode Comparison\n---------------\n\n**with Mel**\n\n```mel\nstring $objs[] = `ls -type transform`;\nfor ($x in $objs) {\n    print (longNameOf($x)); print "\\n";\n\n    // make and break some connections\n    connectAttr( $x + ".sx") ($x + ".sy");\n    connectAttr( $x + ".sx") ($x + ".sz");\n\n    // disconnect all connections to .sx\n    string $conn[] = `listConnections -s 0 -d 1 -p 1 ($x + ".sx")`;\n    for ($inputPlug in $conn)\n        disconnectAttr ($x + ".sx") $inputPlug;\n\n    // add and set a string array attribute with the history of this transform\'s shape\n    if ( !`attributeExists "newAt" $x`)\n        addAttr -ln newAt -dataType stringArray $x;\n    string $shape[] = `listRelatives -s $x`;\n    string $history[] = `listHistory $shape[0]`;\n    string $elements = "";\n    for ($elem in $history)\n        $elements += """ + $elem + "" ";\n    eval ("setAttr -type stringArray " + $x + ".newAt " + `size $history` + $elements);\n    print `getAttr ( $x + ".newAt" )`;\n\n    // get and set some attributes\n    setAttr ($x + ".rotate") 1 1 1;\n    float $trans[] = `getAttr ($x + ".translate")`;\n    float $scale[] = `getAttr ($x + ".scale")`;\n    $trans[0] *= $scale[0];\n    $trans[1] *= $scale[1];\n    $trans[2] *= $scale[2];\n    setAttr ($x + ".scale") $trans[0] $trans[1] $trans[2];\n\n    // call a mel procedure\n    myMelScript( `nodeType $x`, $trans );\n}\n```\n\n**with default Python**\n\n```python\nimport maya.cmds as cmds\nobjs = cmds.ls(type=\'transform\')\n# returns None when it finds no matches\nif objs is not None:\n    for x in objs:\n        print mm.eval(\'longNameOf("%s")\' % x)\n\n        # make and break some connections\n        cmds.connectAttr(\'%s.sx\' % x,  \'%s.sy\' % x)\n        cmds.connectAttr(\'%s.sx\' % x,  \'%s.sz\' % x)\n\n        # disconnect all connections to .sx\n        conn = cmds.listConnections(x + ".sx", s=0, d=1, p=1)\n        # returns None when it finds no match:\n        if conn is not None:\n            for inputPlug in conn:\n                cmds.disconnectAttr(x + ".sx", inputPlug)\n\n        # add and set a string array attribute with the history of this transform\'s shape\n        if not mm.eval(\'attributeExists "newAt" "%s"\' % x):\n            cmds.addAttr(x, ln=\'newAt\', dataType=\'stringArray\')\n        shape = cmds.listRelatives(x, s=1 )\n        if shape is not None:\n            history = cmds.listHistory( shape[0] )\n        else:\n            history = []\n        args = tuple([\'%s.newAt\' % x, len(history)] + history)\n        cmds.setAttr(*args,  type=\'stringArray\' )\n\n        # get and set some attributes\n        cmds.setAttr(\'%s.rotate\' % x, 1, 1, 1)\n        scale = cmds.getAttr(\'%s.scale\' % x)\n        # maya packs the previous result in a list for no apparent reason:\n        scale = scale[0]\n        # the tuple must be converted to a list for item assignment:\n        trans = list(cmds.getAttr(\'%s.translate\' % x )[0])  \n        trans[0] *= scale[0]\n        trans[1] *= scale[1]\n        trans[2] *= scale[2]\n        cmds.setAttr(\'%s.scale\' % x, trans[0], trans[1], trans[2])\n        # call a mel procedure\n        mm.eval(\'myMelScript("%s",{%s,%s,%s})\' % (cmds.nodeType(x), trans[0], trans[1], trans[2]))\n```\n\n**with Pymel**\n\n```python\n# safe to import into main namespace (but only recommended when scripting interactively)\nfrom pymel import *\nfor x in ls( type=\'transform\'):\n    # object oriented design\n    print x.longName()\n\n    # make and break some connections\n    x.sx.connect(x.sy)\n    x.sx.connect(x.sz)\n    # disconnect all connections to .sx\n    x.sx.disconnect()\n\n    # add and set a string array attribute with the history of this transform\'s shape\n    x.setAttr(\'newAt\', x.getShape().history(), force=1)\n\n    # get and set some attributes\n    x.rotate.set([1, 1, 1])\n    trans = x.translate.get()\n    # vector math:\n    trans *= x.scale.get()\n    # ability to pass list/vector args\n    x.translate.set(trans)\n    # call a mel procedure\n    mel.myMelScript(x.type(), trans)\n```\n\nthere\'s a reason why python is rapidly becoming the industry stanadard. with pymel, python and maya finally play well together.\n\nInstallation\n------------\n\nTo install, first install `pip` using the `mayapy` interpreter.\n\nOn MacOS:\n\n```\nexport PATH=$PATH:/Applications/Autodesk/maya2021/Maya.app/Contents/bin\ncurl https://bootstrap.pypa.io/get-pip.py | mayapy\nmayapy -m pip install --pre pymel\n```\n\nOn Linux:\n\n```\nexport PATH=$PATH:/usr/autodesk/maya2021/bin\ncurl https://bootstrap.pypa.io/get-pip.py | mayapy\nmayapy -m pip install --pre pymel\n```\n\nUnless your user account has write privileges to the Maya installation directory,\n`pip` should automatically install `pymel` into your user site-packages directory.\nTo see where it was installed you can run:\n\n```\nmayapy -c "import pymel;print(pymel.__file__)"\n``` \n\n---\n\nPymel is developed and maintained by [Luma Pictures](http://www.lumapictures.com).\n',
    'author': 'Chad Dombrova',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Lumapictures/pymel',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*, !=3.6.*',
}


setup(**setup_kwargs)
