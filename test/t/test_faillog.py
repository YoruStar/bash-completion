import pytest


class Test(object):

    @pytest.mark.complete("faillog -")
    def test_dash(self, completion):
        assert completion.list
