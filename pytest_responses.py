from __future__ import (
    absolute_import, print_function, division, unicode_literals
)

import responses


# pytest plugin support
def pytest_runtest_setup(item):
    if not item.get_marker('withoutresponses'):
        responses.start()


def pytest_runtest_teardown(item):
    if not item.get_marker('withoutresponses'):
        try:
            responses.stop()
        except RuntimeError:
            # patcher was already uninstalled and responses doesnet let us
            # force maintain it
            pass
