import pytest


class Test(object):

    @pytest.mark.complete("avctrl ")
    def test_(self, completion):
        assert completion.list
