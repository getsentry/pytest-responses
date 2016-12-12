from __future__ import (
    absolute_import, print_function, division, unicode_literals
)

import responses


# pytest plugin support
def pytest_runtest_setup(item):
    responses.start()


def pytest_runtest_teardown(item):
    responses.stop()
