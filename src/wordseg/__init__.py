try:
    from importlib.metadata import version
except ModuleNotFoundError:
    # For Python 3.7
    from importlib_metadata import version

from .longest_string_matching import LongestStringMatching
from .random_segmenter import RandomSegmenter


__version__ = version("wordseg")

__all__ = ["__version__", "RandomSegmenter", "LongestStringMatching"]
