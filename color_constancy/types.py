"""Type definitions for the color_constancy package."""

from typing import TypeAlias
import numpy as np
import numpy.typing as npt

# Type aliases for clarity
ImageArray: TypeAlias = npt.NDArray[np.uint8]
FloatImageArray: TypeAlias = npt.NDArray[np.float32]
Float64ImageArray: TypeAlias = npt.NDArray[np.float64]
LookupTable: TypeAlias = npt.NDArray[np.uint8]
RGBVector: TypeAlias = npt.NDArray[np.float64]