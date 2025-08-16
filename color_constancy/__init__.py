"""
Color Constancy Algorithm Implementation.

This package provides an implementation of the color constancy algorithm
for image color correction, particularly useful for medical imaging applications.
"""

from .core import color_constancy
from .types import ImageArray, FloatImageArray

__version__ = "0.1.0"
__author__ = "Yuzo Takagi"
__email__ = "ytworks@example.com"
__all__ = ["color_constancy", "ImageArray", "FloatImageArray"]