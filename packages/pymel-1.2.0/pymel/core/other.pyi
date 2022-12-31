from builtins import str
from typing import Any

class NameParser(str):
    PARENT_SEP: str = ...
    def __new__(cls, strObj: Any): ...
    def __getattr__(self, attr: Any): ...
    def stripNamespace(self, levels: int = ...): ...
    def stripGivenNamespace(self, namespace: Any, partial: bool = ...): ...
    def swapNamespace(self, prefix: Any): ...
    def namespaceList(self): ...
    def namespace(self): ...
    def addPrefix(self, prefix: Any): ...
    def attr(self, attr: Any): ...

class AttributeName(NameParser):
    attrItemReg: Any = ...
    def __init__(self, attrName: Any) -> None: ...
    def __getitem__(self, item: Any): ...
    def __call__(self, *args: Any, **kwargs: Any) -> None: ...
    def array(self): ...
    def plugNode(self): ...
    node: Any = ...
    def plugAttr(self): ...
    def lastPlugAttr(self): ...
    def nodeName(self): ...
    def item(self, asSlice: bool = ..., asString: bool = ...): ...
    def getParent(self, generations: int = ...): ...
    def addAttr(self, **kwargs: Any): ...
    def setAttr(self, *args: Any, **kwargs: Any): ...
    set: Any = ...
    add: Any = ...
    def exists(self): ...

class DependNodeName(NameParser):
    def node(self): ...
    def nodeName(self): ...
    def exists(self, **kwargs: Any): ...
    def stripNum(self): ...
    def extractNum(self): ...
    def nextUniqueName(self): ...
    def nextName(self): ...
    def prevName(self): ...

class DagNodeName(DependNodeName):
    def root(self): ...
    def getRoot(self): ...
    def firstParent(self): ...
    def getParent(self, generations: int = ...): ...
    def nodeName(self): ...

TanimLayer: Any
TrenderSetupStates: Any
adpAnalyticsDialog: Any
adskAsset: Any
adskAssetLibrary: Any
adskAssetList: Any

def adskAssetListUI(*args: Any, **kwargs: Any): ...

agFormatIn: Any
agFormatOut: Any
artAttr: Any
artAttrSkinPaint: Any
artAttrSkinPaintCmd: Any
artFluidAttr: Any
artSelect: Any
artSetPaint: Any
blend: Any
caddyManip: Any
clearShear: Any
copyNode: Any
crashInfoCmd: Any
dagCommandWrapper: Any
dagObjectHit: Any
debug: Any
debugNamespace: Any
debugVar: Any
dgControl: Any
dgPerformance: Any
dgcontrol: Any
dgdebug: Any
dgstats: Any
directConnectPath: Any
dispatchGenericCommand: Any
dynTestData: Any
evalContinue: Any
evaluationManagerInternal: Any
evaluatorInternal: Any
extendFluid: Any

def flagTest(*args: Any, **kwargs: Any): ...

flushIdleQueue: Any
flushThumbnailCache: Any
fontAttributes: Any
greasePencil: Any
greasePencilHelper: Any
greaseRenderPlane: Any
groupParts: Any
hotkeyEditor: Any
hotkeyMapSet: Any

def imageWindowEditor(*args: Any, **kwargs: Any): ...

interactionStyle: Any
iterOnNurbs: Any
journal: Any
licenseCheck: Any
manipComponentPivot: Any
manipComponentUpdate: Any
matrix: Any
mayaDpiSettingAction: Any
meshIntersectTest: Any
mimicMnipulation: Any
mouldMesh: Any
mouldSrf: Any
mouldSubdiv: Any
movieCompressor: Any
myTestCmd: Any
nodeGrapher: Any
nop: Any
nurbsCurveRebuildPref: Any
ogsdebug: Any
paint3d: Any
polyColorSetCmdWrapper: Any
polyIterOnPoly: Any
polyPrimitiveMisc: Any
polySelectEditCtxDataCmd: Any
polySelectSp: Any
polySetVertices: Any
polySpinEdge: Any
polyTestPop: Any
polyToCurve: Any
polyUVStackSimilarShellsCmd: Any
polyWarpImage: Any
psdConvSolidTxOptions: Any
rampWidget: Any
rampWidgetAttrless: Any
readPDC: Any

def repeatLast(*args: Any, **kwargs: Any): ...

retimeHelper: Any
safemodecheckhash: Any

def selectKeyframe(*args: Any, **kwargs: Any): ...

subdDisplayMode: Any
subdToNurbs: Any
subgraph: Any
syncSculptCache: Any
testPa: Any
testPassContribution: Any
texSculptCacheSync: Any

def timeRangeInfo(*args: Any, **kwargs: Any): ...

timeSliderCustomDraw: Any
warnUserDialog: Any
