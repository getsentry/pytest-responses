import pytest

import responses as responses_


# pytest plugin support
def pytest_configure(config):
    config.addinivalue_line(
        'markers',
        'withoutresponses: Tests which need access to external domains.'
    )


def pytest_runtest_setup(item):
    if not item.get_closest_marker('withoutresponses'):
        responses_.start()


def pytest_runtest_teardown(item):
    if not item.get_closest_marker('withoutresponses'):
        try:
            responses_.stop()
            responses_.reset()
        except RuntimeError:
            # patcher was already uninstalled and responses doesnt let us
            # force maintain it
            pass


@pytest.yield_fixture
def responses():
    with responses_.RequestsMock() as rsps:
        yield rsps
