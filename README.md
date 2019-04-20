# pytest-simple-settings

[![PyPI version](https://badge.fury.io/py/pytest-simple-settings.svg)](https://pypi.org/project/pytest-simple-settings/) [![Build Status](https://travis-ci.org/tkukushkin/pytest-simple-settings.svg?branch=master)](https://travis-ci.org/tkukushkin/pytest-simple-settings)

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
