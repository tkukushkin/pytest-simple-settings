from typing import Any  # pylint: disable=unused-import

import pytest
from simple_settings import (  # pylint: disable=unused-import
    LazySettings,
    settings,
)


class _FakeSettings(object):

    def __init__(self, instance):
        # type: (LazySettings) -> None
        self._instance = instance
        self._original_settings = instance._dict.copy()

    def __setattr__(self, key, value):
        # type: (str, Any) -> None
        if key in {'_instance', '_original_settings'}:
            super(_FakeSettings, self).__setattr__(key, value)
            return
        self._instance._dict[key] = value

    def set(self, **new_settings):
        for key, value in new_settings.items():
            setattr(self, key, value)

    def teardown(self):
        # type: () -> None
        self._instance._dict = self._original_settings


@pytest.fixture(name='settings_instance')
def settings_instance_fixture():
    # type: () -> LazySettings
    return settings


@pytest.fixture(name='fake_settings')
def fake_settings_fixture(settings_instance):
    fake_settings = _FakeSettings(settings_instance)
    yield fake_settings
    fake_settings.teardown()
