from __future__ import (
    absolute_import, print_function, division, unicode_literals
)

import requests
import responses
import pytest

from requests.exceptions import ConnectionError


@pytest.mark.withoutresponses
def test_disabled():
    with pytest.raises(ConnectionError):
        requests.get('http://responses.invalid')

    assert len(responses.calls) == 0


def test_enabled():
    with pytest.raises(ConnectionError):
        requests.get('http://responses.invalid')

    assert len(responses.calls) == 1


def test_fixture(responses):
    with pytest.raises(ConnectionError):
        requests.get('http://responses.invalid')

    assert len(responses.calls) == 1
