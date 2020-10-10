import pkg_resources

from wordseg.longest_string_matching import LongestStringMatching
from wordseg.random_segmenter import RandomSegmenter


__version__ = pkg_resources.get_distribution("wordseg").version

__all__ = ["__version__", "RandomSegmenter", "LongestStringMatching"]
