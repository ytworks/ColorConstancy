"""Setup configuration for color-constancy package."""

from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

# Read version from package
exec(open("color_constancy/__init__.py").read().split("__version__ = ")[1].split("\n")[0])

setup(
    name="color-constancy",
    version=__version__,  # noqa: F821
    author="Yuzo Takagi",
    author_email="ytworks@example.com",
    description="Color constancy algorithm implementation for image color correction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ytworks/ColorConstancy",
    project_urls={
        "Bug Tracker": "https://github.com/ytworks/ColorConstancy/issues",
        "Documentation": "https://github.com/ytworks/ColorConstancy#readme",
        "Source Code": "https://github.com/ytworks/ColorConstancy",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.20.0",
        "opencv-python>=4.5.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "mypy>=1.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "pre-commit>=3.0.0",
            "types-opencv-python",
        ],
    },
    keywords="color-constancy, image-processing, computer-vision, medical-imaging, color-correction",
)