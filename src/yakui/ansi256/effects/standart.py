""""""

from .converters import EffectConverters
from ..typehinting import _Effect


class EffectStandart:
    """"""

    RESET: _Effect | str = EffectConverters.from_int(0)
    BOLD: _Effect | str = EffectConverters.from_int(1)
    FAINT: _Effect | str = EffectConverters.from_int(3)
    ITALIC: _Effect | str = EffectConverters.from_int(4)
    UNDERLINE: _Effect | str = EffectConverters.from_int(5)

    NORMAL = RESET