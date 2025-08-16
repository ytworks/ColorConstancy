# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Complete project restructuring for OSS release
- Type hints throughout the codebase
- Comprehensive error handling
- Unit tests with pytest
- CI/CD pipeline with GitHub Actions
- Pre-commit hooks for code quality
- Detailed documentation and examples

### Changed
- Refactored code to follow PEP 8 conventions
- Renamed `ColorConstancy` to `color_constancy` (snake_case)
- Improved variable naming for clarity
- Enhanced docstrings with detailed descriptions

### Fixed
- Added input validation for all parameters
- Improved error messages for better debugging

## [0.1.0] - 2024-01-01

### Added
- Initial implementation of color constancy algorithm
- Basic gamma correction functionality
- Grey-Edge algorithm with Minkowski p-norm (p=3)
- Support for file path and numpy array inputs
- Sample images from ISIC dataset

### Features
- Color constancy correction for image processing
- Customizable gamma parameter
- OpenCV integration for image I/O

[Unreleased]: https://github.com/ytworks/ColorConstancy/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ytworks/ColorConstancy/releases/tag/v0.1.0