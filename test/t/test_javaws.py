import pytest


class Test(object):

    @pytest.mark.complete("javaws ")
    def test_(self, completion):
        assert completion.list
