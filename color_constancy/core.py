"""Core implementation of the color constancy algorithm."""

from typing import Union, Optional
from pathlib import Path
import numpy as np
import cv2

from .types import ImageArray, FloatImageArray, LookupTable, RGBVector


def color_constancy(
    image: Union[str, Path, ImageArray],
    gamma: float = 2.2
) -> ImageArray:
    """
    Apply color constancy algorithm to an image.
    
    This algorithm performs color correction through two steps:
    1. Gamma correction to linearize the image
    2. Color constancy using the Minkowski p-norm (p=3)
    
    Args:
        image: Input image as file path (str or Path) or numpy array.
               If a path is provided, the image will be loaded using OpenCV.
        gamma: Gamma correction value for linearization (default: 2.2).
               Standard sRGB displays use gamma=2.2.
    
    Returns:
        Color-corrected image as a numpy array with dtype uint8.
        
    Raises:
        ValueError: If the image cannot be loaded or processed.
        TypeError: If the input type is invalid.
        
    Example:
        >>> import cv2
        >>> from color_constancy import color_constancy
        >>> 
        >>> # From file path
        >>> corrected = color_constancy('image.jpg')
        >>> cv2.imwrite('corrected.jpg', corrected)
        >>> 
        >>> # From numpy array
        >>> img = cv2.imread('image.jpg')
        >>> corrected = color_constancy(img)
        
    References:
        - http://vislab.isr.ist.utl.pt/wp-content/uploads/2012/12/14-ICIPa.pdf
        - https://pdfs.semanticscholar.org/2f3f/8f151a52afa3c1e80505ddb09b8624162e35.pdf
    """
    # Load image if path is provided
    if isinstance(image, (str, Path)):
        img: Optional[ImageArray] = cv2.imread(str(image))
        if img is None:
            raise ValueError(f"Failed to load image from path: {image}")
    elif isinstance(image, np.ndarray):
        if image.dtype != np.uint8:
            raise ValueError(f"Image array must have dtype uint8, got {image.dtype}")
        if len(image.shape) != 3 or image.shape[2] != 3:
            raise ValueError(f"Image must be a 3-channel color image, got shape {image.shape}")
        img = image.copy()
    else:
        raise TypeError(f"Image must be a file path (str/Path) or numpy array, got {type(image)}")
    
    # Validate gamma parameter
    if gamma <= 0:
        raise ValueError(f"Gamma must be positive, got {gamma}")
    
    # Step 1: Gamma correction for linearization
    img = _apply_gamma_correction(img, gamma)
    
    # Step 2: Color constancy correction
    img = _apply_color_correction(img)
    
    return img


def _apply_gamma_correction(image: ImageArray, gamma: float) -> ImageArray:
    """
    Apply gamma correction to linearize the image.
    
    Args:
        image: Input image array.
        gamma: Gamma correction value.
        
    Returns:
        Gamma-corrected image.
    """
    # Create lookup table for efficient gamma correction
    lookup_table: LookupTable = np.zeros((256, 1), dtype=np.uint8)
    for i in range(256):
        lookup_table[i, 0] = int(255 * pow(float(i) / 255, 1.0 / gamma))
    
    # Apply lookup table to all channels
    return cv2.LUT(image, lookup_table)


def _apply_color_correction(image: ImageArray) -> ImageArray:
    """
    Apply color constancy correction using Minkowski p-norm.
    
    This implements the Grey-Edge algorithm with p=3.
    
    Args:
        image: Gamma-corrected input image.
        
    Returns:
        Color-corrected image.
    """
    # Convert to float32 for calculations
    img_float: FloatImageArray = image.astype(np.float32)
    
    # Calculate p-norm with p=3
    p: float = 3.0
    img_p3: FloatImageArray = np.power(img_float, p)
    
    # Calculate the illumination vector
    # Mean across spatial dimensions (height, width)
    mean_p3: RGBVector = np.mean(img_p3, axis=(0, 1))
    rgb_vec: RGBVector = np.power(mean_p3, 1.0 / p)
    
    # Normalize the RGB vector
    rgb_norm: float = np.sqrt(np.mean(np.power(rgb_vec, 2.0)))
    if rgb_norm > 0:
        rgb_vec = rgb_vec / rgb_norm
    
    # Calculate correction factors
    # Avoid division by zero
    rgb_vec = np.where(rgb_vec > 0, 1.0 / rgb_vec, 1.0)
    
    # Apply correction
    corrected: FloatImageArray = np.multiply(img_float, rgb_vec)
    
    # Clip values to valid range and convert back to uint8
    corrected = np.clip(corrected, 0, 255)
    return corrected.astype(np.uint8)