# tests for dinsort module.
from dinsort import normalize

def test_normalize():
    # we can normalize strings
    assert normalize("string") is not None
