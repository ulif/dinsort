# -*- coding: utf-8 -*-
#
# tests for dinsort module.
from __future__ import unicode_literals
from dinsort import normalize, VARIANT1, VARIANT2

class TestDinsort(object):

    def test_variants(self):
        # we can get variants
        assert VARIANT1 is not None
        assert VARIANT2 is not None

    def test_sort_key(self):
        # we can use normalize to sort by key
        assert sorted(["Musst", "Muß"]) == ["Musst", "Muß"]
        assert sorted(["Musst", "Muß"], key=normalize) == ["Muß", "Musst"]


class TestNormalize(object):
    # tests for normalize()

    def test_normalize(self):
        # we can normalize strings
        assert normalize("string") is not None

    def test_sharp_s(self):
        # sharp s equals 'ss'
        assert normalize("ß") == "ss"

    def test_umlaut(self):
        # we get ä -> a by default (and variant1 explicitly requested)
        assert normalize("ä") == "a"
        assert normalize("ä", variant=VARIANT1) == "a"

    def test_umlaut_variant2(self):
        # we get ä -> ae with variant 2
        assert normalize("ä", variant=VARIANT2) == "ae"

    def test_lower_case(self):
        # normalized terms are lowercase
        assert normalize("FÖÖbar") == "foobar"
        assert normalize("FÖÖbar", variant=VARIANT2) == "foeoebar"

    def test_diacritic_chars_are_removed_from_diacritic(self):
        # chars with diacritics (acutes, graves, tildas, etc.) are stripped.
        assert normalize("Čéñâça") == "cenaca"
        assert normalize("Čéñâça", variant=VARIANT1) == "cenaca"
        assert normalize("ČÉÑÂÇA", variant=VARIANT2) == "cenaca"
        assert normalize("ČÉÑÂÇA") == "cenaca"
