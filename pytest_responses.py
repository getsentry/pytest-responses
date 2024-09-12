from packaging import version

import pytest

from responses import (
    Call,
    CallbackResponse,
    CallList,
    PassthroughResponse,
    RequestsMock,
    Response,
    matchers,
    registries,
)
from responses import mock as _mock


def get_withoutresponses_marker(item):
    if version.parse(pytest.__version__) >= version.parse('4.0.0'):
        return item.get_closest_marker('withoutresponses')
    else:
        return item.get_marker('withoutresponses')


# pytest plugin support
def pytest_configure(config):
    config.addinivalue_line(
        'markers',
        'withoutresponses: Tests which need access to external domains.'
    )


def pytest_runtest_setup(item):
    if not get_withoutresponses_marker(item):
        _mock.start()


def pytest_runtest_teardown(item):
    if not get_withoutresponses_marker(item):
        try:
            _mock.stop()
            _mock.reset()
        except (AttributeError, RuntimeError):
            # patcher was already uninstalled (or not installed at all) and
            # responses doesnt let us force maintain it
            pass


@pytest.fixture
def responses():
    with RequestsMock() as rsps:
        yield rsps


__all__ = [
    'responses',
    'Call',
    'CallbackResponse',
    'CallList',
    'PassthroughResponse',
    'RequestsMock',
    'Response',
    'matchers',
    'registries',
    # pytest plug-in setup
    'pytest_configure',
    'pytest_runtest_setup',
    'pytest_runtest_teardown',
]
