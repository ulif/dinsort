# tests for dinsort module.
from dinsort import normalize


class TestNormalize(object):
    # tests for normalize()

    def test_normalize(self):
        # we can normalize strings
        assert normalize("string") is not None
