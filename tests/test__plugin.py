import pytest
from simple_settings import LazySettings


instance = LazySettings('tests.settings')


@pytest.fixture()
def settings_instance():
    return instance


def test_settings(fake_settings):
    # act
    fake_settings.BAR = 2
    fake_settings.set(BAZ=3)

    # assert
    assert instance.FOO == 1
    assert instance.BAR == 2
    assert instance.BAZ == 3
