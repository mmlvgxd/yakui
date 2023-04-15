""""""

from ..constants import CSI
from ..typehinting import _Effect


class EffectConverters:
    """"""

    def from_int(int__: int) -> _Effect | str:
        return f"{CSI}{int__}m"
