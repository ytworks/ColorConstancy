#!/usr/bin/env python
"""Basic usage example of the color_constancy package."""

from pathlib import Path
import cv2
from color_constancy import color_constancy


def main() -> None:
    """Demonstrate basic usage of color_constancy function."""
    # Define paths
    examples_dir = Path(__file__).parent
    images_dir = examples_dir / "images"
    
    # Process sample images
    sample_images = ["ISIC_0012221.jpg", "ISIC_0012222.jpg"]
    
    for image_name in sample_images:
        # Input and output paths
        input_path = images_dir / image_name
        output_name = image_name.replace(".jpg", "_corrected.jpg")
        output_path = images_dir / output_name
        
        print(f"Processing {image_name}...")
        
        # Apply color constancy
        corrected_image = color_constancy(input_path)
        
        # Save the result
        cv2.imwrite(str(output_path), corrected_image)
        print(f"  Saved corrected image to {output_name}")
        
        # Alternatively, you can load the image first and then process it
        original_image = cv2.imread(str(input_path))
        if original_image is not None:
            # Apply with custom gamma value
            corrected_custom = color_constancy(original_image, gamma=2.4)
            custom_output = image_name.replace(".jpg", "_gamma2.4.jpg")
            cv2.imwrite(str(images_dir / custom_output), corrected_custom)
            print(f"  Saved with gamma=2.4 to {custom_output}")
    
    print("\nColor constancy correction completed!")
    print("Check the examples/images/ directory for the output files.")


def advanced_example() -> None:
    """Demonstrate advanced usage with error handling."""
    import numpy as np
    
    try:
        # Create a synthetic image for demonstration
        synthetic_image = np.zeros((200, 200, 3), dtype=np.uint8)
        
        # Add color gradients
        for i in range(200):
            synthetic_image[i, :, 0] = int(255 * (i / 200))  # Red gradient
            synthetic_image[:, i, 1] = int(255 * (i / 200))  # Green gradient
            synthetic_image[i, i, 2] = 255  # Blue diagonal
        
        # Apply color constancy
        corrected = color_constancy(synthetic_image)
        
        # Save the synthetic example
        examples_dir = Path(__file__).parent / "images"
        cv2.imwrite(str(examples_dir / "synthetic_original.jpg"), synthetic_image)
        cv2.imwrite(str(examples_dir / "synthetic_corrected.jpg"), corrected)
        
        print("Created synthetic example images.")
        
    except ValueError as e:
        print(f"Error processing image: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    print("Color Constancy Algorithm - Basic Usage Example")
    print("=" * 50)
    
    # Run basic example
    main()
    
    print("\n" + "=" * 50)
    print("Running advanced example...")
    advanced_example()