# Contributing to Color Constancy

Thank you for considering contributing to the Color Constancy project! This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [Coding Standards](#coding-standards)
- [Documentation](#documentation)

## 📜 Code of Conduct

Please note that this project adheres to a Code of Conduct. By participating, you are expected to:

- Use welcoming and inclusive language
- Be respectful of differing viewpoints and experiences
- Gracefully accept constructive criticism
- Focus on what is best for the community
- Show empathy towards other community members

## 🚀 Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ColorConstancy.git
   cd ColorConstancy
   ```
3. **Add the upstream repository**:
   ```bash
   git remote add upstream https://github.com/ytworks/ColorConstancy.git
   ```

## 💻 Development Setup

### Prerequisites

- Python 3.8 or higher
- pip
- git

### Installation

1. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install the package in development mode**:
   ```bash
   pip install -e ".[dev]"
   ```

3. **Install pre-commit hooks**:
   ```bash
   pre-commit install
   ```

### Development Tools

The development environment includes:

- **pytest**: Testing framework
- **mypy**: Static type checking
- **black**: Code formatting
- **flake8**: Linting
- **pre-commit**: Git hooks for code quality

## 🔧 Making Changes

### Workflow

1. **Create a new branch** for your feature or bugfix:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bugfix-name
   ```

2. **Make your changes** following the coding standards

3. **Add or update tests** as needed

4. **Update documentation** if you're changing functionality

5. **Run tests and checks**:
   ```bash
   # Run tests
   pytest
   
   # Type checking
   mypy color_constancy
   
   # Formatting
   black color_constancy tests
   
   # Linting
   flake8 color_constancy tests
   ```

### Types of Contributions

We welcome various types of contributions:

- **Bug fixes**: Fix issues reported in GitHub Issues
- **Features**: Add new functionality
- **Documentation**: Improve or add documentation
- **Tests**: Add missing tests or improve existing ones
- **Performance**: Optimize code performance
- **Examples**: Add usage examples

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=color_constancy --cov-report=html

# Run specific test file
pytest tests/test_core.py

# Run with verbose output
pytest -v
```

### Writing Tests

- Place tests in the `tests/` directory
- Name test files with `test_` prefix
- Use descriptive test function names
- Include docstrings explaining what each test does
- Test both success cases and error conditions

Example test:

```python
def test_color_constancy_with_valid_image():
    """Test that color_constancy processes valid images correctly."""
    image = np.zeros((100, 100, 3), dtype=np.uint8)
    result = color_constancy(image)
    assert result.shape == image.shape
    assert result.dtype == np.uint8
```

## 📤 Submitting Changes

### Pull Request Process

1. **Update your branch** with the latest upstream changes:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Push your changes** to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request** on GitHub:
   - Use a clear, descriptive title
   - Reference any related issues
   - Describe what changes you made and why
   - Include screenshots if applicable

### Pull Request Checklist

Before submitting, ensure:

- [ ] All tests pass
- [ ] Code follows the project's style guidelines
- [ ] Type hints are included for new code
- [ ] Documentation is updated if needed
- [ ] Commit messages are clear and descriptive
- [ ] PR description explains the changes

## 📏 Coding Standards

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use [black](https://github.com/psf/black) for formatting (line length: 100)
- Use meaningful variable and function names
- Keep functions focused and small

### Type Hints

- Add type hints to all function signatures
- Use `from typing import` for complex types
- Example:
  ```python
  from typing import Union, Optional
  import numpy as np
  import numpy.typing as npt
  
  def process_image(
      image: Union[str, npt.NDArray[np.uint8]],
      gamma: float = 2.2
  ) -> npt.NDArray[np.uint8]:
      ...
  ```

### Docstrings

- Use Google-style or NumPy-style docstrings
- Include descriptions for all parameters and returns
- Add usage examples for complex functions

### Git Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests

Example:
```
Add gamma parameter validation

- Validate gamma is positive
- Add appropriate error messages
- Include tests for edge cases

Fixes #123
```

## 📚 Documentation

### Code Documentation

- Add docstrings to all public functions and classes
- Include type information in docstrings
- Provide examples in docstrings when helpful

### README Updates

When adding features, update the README to include:
- Feature description in the Features section
- Usage examples
- API documentation if adding public functions

### Changelog

For significant changes, update the CHANGELOG.md following [Keep a Changelog](https://keepachangelog.com/) format.

## ❓ Questions?

If you have questions or need help:

1. Check existing [issues](https://github.com/ytworks/ColorConstancy/issues)
2. Create a new issue with the question label
3. Join discussions in pull requests

## 🙏 Thank You!

Thank you for contributing to Color Constancy! Your efforts help make this project better for everyone.