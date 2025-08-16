"""Unit tests for the core color constancy functionality."""

import pytest
import numpy as np
import cv2
from pathlib import Path
from typing import Tuple

from color_constancy import color_constancy


class TestColorConstancy:
    """Test suite for the color_constancy function."""
    
    @pytest.fixture
    def sample_image(self) -> np.ndarray:
        """Create a sample test image."""
        # Create a 100x100 RGB image with known values
        image = np.zeros((100, 100, 3), dtype=np.uint8)
        image[:50, :50] = [255, 0, 0]  # Red quadrant
        image[:50, 50:] = [0, 255, 0]  # Green quadrant
        image[50:, :50] = [0, 0, 255]  # Blue quadrant
        image[50:, 50:] = [128, 128, 128]  # Gray quadrant
        return image
    
    @pytest.fixture
    def temp_image_path(self, tmp_path: Path, sample_image: np.ndarray) -> Path:
        """Create a temporary image file for testing."""
        image_path = tmp_path / "test_image.jpg"
        cv2.imwrite(str(image_path), sample_image)
        return image_path
    
    def test_numpy_array_input(self, sample_image: np.ndarray) -> None:
        """Test color_constancy with numpy array input."""
        result = color_constancy(sample_image)
        
        assert isinstance(result, np.ndarray)
        assert result.dtype == np.uint8
        assert result.shape == sample_image.shape
    
    def test_file_path_input_str(self, temp_image_path: Path) -> None:
        """Test color_constancy with string file path input."""
        result = color_constancy(str(temp_image_path))
        
        assert isinstance(result, np.ndarray)
        assert result.dtype == np.uint8
        assert len(result.shape) == 3
        assert result.shape[2] == 3
    
    def test_file_path_input_path(self, temp_image_path: Path) -> None:
        """Test color_constancy with Path object input."""
        result = color_constancy(temp_image_path)
        
        assert isinstance(result, np.ndarray)
        assert result.dtype == np.uint8
        assert len(result.shape) == 3
        assert result.shape[2] == 3
    
    def test_gamma_parameter(self, sample_image: np.ndarray) -> None:
        """Test different gamma values."""
        # Test with different gamma values
        result1 = color_constancy(sample_image, gamma=1.8)
        result2 = color_constancy(sample_image, gamma=2.2)
        result3 = color_constancy(sample_image, gamma=2.6)
        
        # Results should be different for different gamma values
        assert not np.array_equal(result1, result2)
        assert not np.array_equal(result2, result3)
        assert not np.array_equal(result1, result3)
    
    def test_invalid_gamma_raises_error(self, sample_image: np.ndarray) -> None:
        """Test that invalid gamma values raise appropriate errors."""
        with pytest.raises(ValueError, match="Gamma must be positive"):
            color_constancy(sample_image, gamma=0)
        
        with pytest.raises(ValueError, match="Gamma must be positive"):
            color_constancy(sample_image, gamma=-1.5)
    
    def test_invalid_file_path_raises_error(self) -> None:
        """Test that non-existent file paths raise appropriate errors."""
        with pytest.raises(ValueError, match="Failed to load image"):
            color_constancy("non_existent_file.jpg")
    
    def test_invalid_input_type_raises_error(self) -> None:
        """Test that invalid input types raise appropriate errors."""
        with pytest.raises(TypeError, match="Image must be a file path"):
            color_constancy(123)  # type: ignore
        
        with pytest.raises(TypeError, match="Image must be a file path"):
            color_constancy([1, 2, 3])  # type: ignore
    
    def test_invalid_array_dtype_raises_error(self) -> None:
        """Test that arrays with invalid dtype raise appropriate errors."""
        wrong_dtype_image = np.zeros((100, 100, 3), dtype=np.float32)
        with pytest.raises(ValueError, match="dtype uint8"):
            color_constancy(wrong_dtype_image)
    
    def test_invalid_array_shape_raises_error(self) -> None:
        """Test that arrays with invalid shape raise appropriate errors."""
        # Test with grayscale image
        grayscale_image = np.zeros((100, 100), dtype=np.uint8)
        with pytest.raises(ValueError, match="3-channel color image"):
            color_constancy(grayscale_image)
        
        # Test with wrong number of channels
        wrong_channels = np.zeros((100, 100, 4), dtype=np.uint8)
        with pytest.raises(ValueError, match="3-channel color image"):
            color_constancy(wrong_channels)
    
    def test_output_range(self, sample_image: np.ndarray) -> None:
        """Test that output values are in valid range."""
        result = color_constancy(sample_image)
        
        assert result.min() >= 0
        assert result.max() <= 255
    
    def test_consistency(self, sample_image: np.ndarray) -> None:
        """Test that the function produces consistent results."""
        result1 = color_constancy(sample_image)
        result2 = color_constancy(sample_image)
        
        assert np.array_equal(result1, result2)
    
    def test_preserves_image_dimensions(self, sample_image: np.ndarray) -> None:
        """Test that the function preserves image dimensions."""
        # Test with various image sizes
        sizes: list[Tuple[int, int]] = [(50, 50), (100, 200), (480, 640)]
        
        for height, width in sizes:
            test_image = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
            result = color_constancy(test_image)
            assert result.shape == (height, width, 3)
    
    def test_handles_edge_cases(self) -> None:
        """Test edge cases like uniform color images."""
        # Test with uniform gray image
        gray_image = np.full((100, 100, 3), 128, dtype=np.uint8)
        result = color_constancy(gray_image)
        assert isinstance(result, np.ndarray)
        
        # Test with black image
        black_image = np.zeros((100, 100, 3), dtype=np.uint8)
        result = color_constancy(black_image)
        assert isinstance(result, np.ndarray)
        
        # Test with white image
        white_image = np.full((100, 100, 3), 255, dtype=np.uint8)
        result = color_constancy(white_image)
        assert isinstance(result, np.ndarray)