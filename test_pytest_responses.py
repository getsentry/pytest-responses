from __future__ import (
    absolute_import, print_function, division, unicode_literals
)

import requests
import responses
import pytest

from requests.exceptions import ConnectionError

pytest_plugins = str('pytester')


@pytest.mark.withoutresponses
def test_disabled():
    with pytest.raises(ConnectionError):
        requests.get('http://responses.invalid')

    assert len(responses.calls) == 0


def test_enabled():
    with pytest.raises(ConnectionError):
        requests.get('http://responses.invalid')

    assert len(responses.calls) == 1


def test_marker(testdir):
    result = testdir.runpytest('--markers')
    assert '@pytest.mark.withoutresponses' in result.stdout.str()


class TestReset:
    """
    Ensure that the callback registered in `test_1` is cleaned up before
    `test_2`.
    """
    def test_1(self):
        responses.add(responses.GET, 'http://responses.invalid', json=1)
        assert requests.get('http://responses.invalid').json() == 1

    def test_2(self):
        responses.add(responses.GET, 'http://responses.invalid', json=2)
        assert requests.get('http://responses.invalid').json() == 2
