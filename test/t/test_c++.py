import pytest


class Test(object):

    @pytest.mark.complete("c++ ")
    def test_(self, completion):
        assert completion.list
