# Complete Guide: PyPI Publishing, CI/CD & Community Setup

## 1. PyPI Publishing Steps

### Prerequisites
1. Create accounts:
   - PyPI: https://pypi.org/account/register/
   - TestPyPI: https://test.pypi.org/account/register/

2. Generate API tokens:
   - PyPI: Account Settings → API tokens → Add API token
   - TestPyPI: Same process
   - Save tokens securely (format: `pypi-...`)

### Publishing Commands

```bash
# 1. Install publishing tools
pip install build twine

# 2. Build package
python -m build

# 3. Test upload to TestPyPI first
twine upload --repository testpypi dist/*
# Enter username: __token__
# Enter password: [your-testpypi-token]

# 4. Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ caesar-cipher-tool

# 5. Upload to real PyPI
twine upload dist/*
# Enter username: __token__
# Enter password: [your-pypi-token]
```

### Version Management
- Update version in `cipher_tool/__init__.py`
- Create git tag: `git tag v1.0.1`
- Push tag: `git push origin v1.0.1`

## 2. CI/CD Integration Steps

### GitHub Secrets Setup
1. Go to GitHub repo → Settings → Secrets and variables → Actions
2. Add secrets:
   - `PYPI_API_TOKEN`: Your PyPI API token
   - `TEST_PYPI_API_TOKEN`: Your TestPyPI API token (optional)

### Workflow Triggers
- **Push to main/develop**: Runs tests only
- **Pull Request**: Runs tests only  
- **Release created**: Runs tests + publishes to PyPI

### Creating Releases
1. Go to GitHub repo → Releases → Create new release
2. Tag: `v1.0.1` (increment version)
3. Title: `Release v1.0.1`
4. Description: List changes
5. Publish → Triggers automatic PyPI upload

## 3. Community Contributions Setup

### Repository Settings
1. Go to Settings → General
2. Enable:
   - Issues
   - Wiki (optional)
   - Discussions (optional)
3. Branch protection rules:
   - Require PR reviews
   - Require status checks
   - Require up-to-date branches

### Labels Setup
Create these labels in Issues → Labels:
- `bug` (red)
- `enhancement` (blue)
- `documentation` (green)
- `good first issue` (purple)
- `help wanted` (yellow)

### Contributor Recognition
Add to README.md:
```markdown
## Contributors
- [Your Name](https://github.com/yourusername) - Creator
```

## 4. Maintenance Workflow

### Regular Tasks
1. **Weekly**: Review issues and PRs
2. **Monthly**: Update dependencies
3. **Quarterly**: Review and update documentation

### Release Process
1. Update version number
2. Update CHANGELOG.md
3. Create GitHub release
4. Monitor CI/CD pipeline
5. Verify PyPI upload

### Community Engagement
1. Respond to issues within 48 hours
2. Review PRs within 1 week
3. Welcome new contributors
4. Maintain code of conduct

## 5. Next Steps Checklist

### Immediate (Today)
- [ ] Create PyPI accounts
- [ ] Generate API tokens
- [ ] Add tokens to GitHub secrets
- [ ] Test publish to TestPyPI

### This Week
- [ ] Create first GitHub release
- [ ] Set up branch protection
- [ ] Add contributor guidelines
- [ ] Enable GitHub discussions

### This Month
- [ ] Add more cipher algorithms
- [ ] Improve documentation
- [ ] Add CLI interface
- [ ] Create tutorial videos

## 6. Commands Reference

```bash
# Development
pip install -e .
pytest tests/ -v
python -m build

# Publishing
twine upload --repository testpypi dist/*
twine upload dist/*

# Git workflow
git checkout -b feature/new-feature
git add .
git commit -m "feat: add new feature"
git push origin feature/new-feature

# Release workflow
git tag v1.0.1
git push origin v1.0.1
# Create GitHub release → Auto-publishes to PyPI
```

Your project is now ready for professional open-source development! 🚀