from typing import Any, Optional

class NO_DATA(Exception): ...

class Condition:
    value: Any = ...
    def __init__(self, value: Optional[Any] = ...) -> None: ...
    def eval(self, data: Any = ...): ...
    def __or__(self, other: Any): ...
    def __ror__(self, other: Any): ...
    def __and__(self, other: Any): ...
    def __rand__(self, other: Any): ...
    def __invert__(self): ...
    def __bool__(self): ...

Always: Any
Never: Any

class Inverse(Condition):
    toInvert: Any = ...
    def __init__(self, toInvert: Any) -> None: ...
    def eval(self, data: Any = ...): ...

class AndOrAbstract(Condition):
    args: Any = ...
    def __init__(self, *args: Any) -> None: ...
    def eval(self, data: Any = ...): ...

class And(AndOrAbstract): ...
class Or(AndOrAbstract): ...
