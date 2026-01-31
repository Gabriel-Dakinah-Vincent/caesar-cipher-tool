# Contributing to Caesar Cipher Tool

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/caesar-cipher-tool.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Unix)
5. Install in development mode: `pip install -e .`
6. Install development dependencies: `pip install pytest build twine`

## Development Workflow

1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Run tests: `pytest tests/ -v`
4. Commit your changes: `git commit -m "feat: add your feature"`
5. Push to your fork: `git push origin feature/your-feature-name`
6. Create a Pull Request

## Code Standards

- Follow PEP 8 style guidelines
- Add tests for new functionality
- Update documentation as needed
- Keep functions small and focused
- Use descriptive variable names

## Testing

- All tests must pass: `pytest tests/ -v`
- Add tests for new features
- Maintain test coverage above 90%

## Commit Messages

Use conventional commits format:
- `feat:` for new features
- `fix:` for bug fixes
- `docs:` for documentation changes
- `test:` for test additions/changes
- `refactor:` for code refactoring

## Pull Request Process

1. Ensure all tests pass
2. Update README.md if needed
3. Add yourself to contributors if desired
4. Request review from maintainers

## Issues

- Use issue templates when available
- Provide clear reproduction steps for bugs
- Include Python version and OS information

## Questions?

Feel free to open an issue for questions or discussions.