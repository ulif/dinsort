# -*- coding: utf-8 -*-
#
# tests for dinsort module.
from dinsort import normalize


class TestNormalize(object):
    # tests for normalize()

    def test_normalize(self):
        # we can normalize strings
        assert normalize("string") is not None

    def test_sharp_s(self):
        # sharp s equals 'ss'
        assert normalize("ß") == "ss"

