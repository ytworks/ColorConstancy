# Color Constancy Algorithm

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5+-green.svg)](https://opencv.org/)

A Python implementation of the color constancy algorithm for image color correction, particularly useful for medical imaging and computer vision applications.

## 🎯 Overview

Color constancy is the ability to perceive colors of objects invariant to the color of the light source. This package implements a color constancy algorithm that transforms image colors acquired under an unknown light source to appear as if they were taken under a canonical (reference) light source.

The algorithm performs two main steps:
1. **Gamma correction**: Linearizes the image to remove display gamma
2. **Color correction**: Applies the Grey-Edge algorithm with Minkowski p-norm (p=3) to estimate and correct for the illuminant

## ✨ Features

- Simple and efficient color constancy correction
- Support for various input formats (file paths, numpy arrays)
- Customizable gamma correction
- Type hints for better IDE support
- Comprehensive error handling
- Well-tested with pytest

## 📦 Installation

### From Source

```bash
git clone https://github.com/ytworks/ColorConstancy.git
cd ColorConstancy
pip install -e .
```

### For Development

```bash
git clone https://github.com/ytworks/ColorConstancy.git
cd ColorConstancy
pip install -e ".[dev]"
```

## 🚀 Quick Start

```python
from color_constancy import color_constancy
import cv2

# Process an image file
corrected = color_constancy('path/to/image.jpg')
cv2.imwrite('corrected_image.jpg', corrected)

# Process a numpy array
image = cv2.imread('path/to/image.jpg')
corrected = color_constancy(image, gamma=2.2)
```

## 📖 Detailed Usage

### Basic Usage

```python
from pathlib import Path
from color_constancy import color_constancy
import cv2

# Using file path (str or Path object)
corrected = color_constancy('image.jpg')
corrected = color_constancy(Path('image.jpg'))

# Using numpy array
image = cv2.imread('image.jpg')
corrected = color_constancy(image)

# Custom gamma value
corrected = color_constancy('image.jpg', gamma=2.4)
```

### Error Handling

```python
from color_constancy import color_constancy

try:
    corrected = color_constancy('image.jpg')
except ValueError as e:
    print(f"Error processing image: {e}")
except TypeError as e:
    print(f"Invalid input type: {e}")
```

### Running Examples

```bash
cd examples
python basic_usage.py
```

This will process the sample images in `examples/images/` and create corrected versions.

## 🔬 Algorithm Details

The implementation uses the Grey-Edge algorithm with the following mathematical foundation:

1. **Gamma Correction**: 
   - Linearizes the image using inverse gamma transformation
   - Default gamma value: 2.2 (standard for sRGB displays)

2. **Illuminant Estimation**:
   - Computes the Minkowski p-norm (p=3) of the image
   - Estimates the RGB illuminant vector
   - Normalizes the vector using L2 norm

3. **Color Correction**:
   - Applies the inverse of the estimated illuminant
   - Clips values to valid range [0, 255]

## 📚 API Reference

### `color_constancy(image, gamma=2.2)`

Apply color constancy algorithm to an image.

**Parameters:**
- `image` (Union[str, Path, np.ndarray]): Input image as file path or numpy array
- `gamma` (float): Gamma correction value (default: 2.2)

**Returns:**
- `np.ndarray`: Corrected image as uint8 numpy array

**Raises:**
- `ValueError`: If image cannot be loaded or processed
- `TypeError`: If input type is invalid

## 🧪 Testing

Run the test suite:

```bash
# Basic test run
pytest

# With coverage report
pytest --cov=color_constancy --cov-report=html

# Verbose output
pytest -v
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

1. Fork the repository
2. Clone your fork
3. Install in development mode:
   ```bash
   pip install -e ".[dev]"
   pre-commit install
   ```
4. Make your changes
5. Run tests: `pytest`
6. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📝 References

- [Color constancy algorithm paper (ICIP)](http://vislab.isr.ist.utl.pt/wp-content/uploads/2012/12/14-ICIPa.pdf)
- [Grey-Edge algorithm details](https://pdfs.semanticscholar.org/2f3f/8f151a52afa3c1e80505ddb09b8624162e35.pdf)

## 🙏 Acknowledgments

- Sample images from the International Skin Imaging Collaboration (ISIC) dataset
- Algorithm based on research in computational color constancy

## 📊 Project Status

- ✅ Core algorithm implementation
- ✅ Type hints and documentation
- ✅ Unit tests
- ✅ Example code
- ✅ CI/CD setup
- 🔄 PyPI package (planned)

## 📧 Contact

- Author: Yuzo Takagi
- GitHub: [@ytworks](https://github.com/ytworks)
- Issues: [GitHub Issues](https://github.com/ytworks/ColorConstancy/issues)