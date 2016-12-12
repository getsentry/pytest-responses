pytest-responses
================

Automatically activate responses across your py.test-powered test suite (thus preventing HTTP requests).

If particular tests need access to external domains, you can use the ``withoutresponses`` marker:

.. sourcecode:: python

    @pytest.mark.withoutresponses
    def test_disabled():
        with pytest.raises(ConnectionError):
            requests.get('http://responses.invalid')

        assert len(responses.calls) == 0
