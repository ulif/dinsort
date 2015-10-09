# -*- coding: utf-8 -*-
#
# tests for dinsort module.
from dinsort import normalize, VARIANT1, VARIANT2

class TestDinsort(object):

    def test_variants(self):
        # we can get variants
        assert VARIANT1 is not None
        assert VARIANT2 is not None


class TestNormalize(object):
    # tests for normalize()

    def test_normalize(self):
        # we can normalize strings
        assert normalize(u"string") is not None

    def test_sharp_s(self):
        # sharp s equals 'ss'
        assert normalize(u"ß") == u"ss"

