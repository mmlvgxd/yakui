""""""
# fmt: off
from ..constants import CSI
from ..typehinting import (
    _Red, _Green, _Blue,
    _Color, _FORE, _BACK
)
# fmt: on


class ColorConverters:
    """"""

    def from_rgb(
        # fmt: off
        red: _Red | int | str,
        green: _Green | int | str,
        blue: _Blue | int | str,
        *,
        mode: _FORE | _BACK | int | str,
        # fmt: on
    ) -> _Color | str:
        """"""
        return f"{CSI}{mode};2;{red};{green};{blue}m"
