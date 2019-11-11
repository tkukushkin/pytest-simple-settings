# pytest-simple-settings

[![PyPI version](https://badge.fury.io/py/pytest-simple-settings.svg)](https://pypi.org/project/pytest-simple-settings/) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pytest-simple-settings.svg?color=green) [![Build Status](https://github.com/tkukushkin/pytest-simple-settings/workflows/build/badge.svg?branch=master)](https://github.com/tkukushkin/pytest-simple-settings/actions?query=workflow%3Abuild+branch%3Amaster)

## Usage

With default `simple_settings.settings`:

```python
from simple_settings import settings


def test_foo(fake_settings):
    fake_settings.FOO = 1
    fake_settings.set(BAR=2)
    
    assert settings.FOO == 1
    assert settings.BAR == 2
```

With custom `LazySettings` instance
```python
import pytest
from simple_settings import LazySettings


instance = LazySettings('settings')


@pytest.fixture()
def settings_instance():
    return instance


def test_foo(fake_settings):
    fake_settings.FOO = 1
    fake_settings.set(BAR=2)
    
    assert instance.FOO == 1
    assert instance.BAR == 2
```
