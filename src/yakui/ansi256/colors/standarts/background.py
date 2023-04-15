""""""

from ...constants import BACKGROUND
from ...colors.converters import ColorConverters
from ...typehinting import _Color


class ColorStandartBackground:
    """"""

    mode = BACKGROUND

    WHITE: _Color | str = ColorConverters.from_rgb(255, 255, 255, mode=mode)
    BLACK: _Color | str = ColorConverters.from_rgb(0, 0, 0, mode=mode)
    RED: _Color | str = ColorConverters.from_rgb(255, 0, 0, mode=mode)
    GREEN: _Color | str = ColorConverters.from_rgb(0, 255, 0, mode=mode)
    BLUE: _Color | str = ColorConverters.from_rgb(0, 0, 255, mode=mode)
