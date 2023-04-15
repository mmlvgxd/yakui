from .effects.effect import Effect
from .typehinting import _Color, _Effect


def beautify(
    # fmt: off
    text: str,
    color: _Color | str,
    effect: _Effect | str,
    # fmt: on
) -> str:
    return effect + color + text + Effect.Standart.RESET
