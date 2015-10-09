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

    def test_umlaut(self):
        # we get ä -> a by default (and variant1 explicitly requested)
        assert normalize(u"ä") == u"a"
        assert normalize(u"ä", variant=VARIANT1) == u"a"

    def test_umlaut_variant2(self):
        # we get ä -> ae with variant 2
        assert normalize(u"ä", variant=VARIANT2) == u"ae"
