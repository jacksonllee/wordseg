import os
import re

import wordseg


def test_version_number_match_with_changelog():
    """__version__ and CHANGELOG.md match for the latest version number."""
    repo_dir = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    )
    changelog = open(os.path.join(repo_dir, "CHANGELOG.md")).read()
    # latest version number in changelog = the 1st occurrence of '[x.y.z]'
    version_in_changelog = (
        re.search(r"\[\d+\.\d+\.\d+\]", changelog).group().strip("[]")
    )
    assert wordseg.__version__ == version_in_changelog, (
        f"Make sure both __version__ ({wordseg.__version__}) and "
        f"CHANGELOG ({version_in_changelog}) "
        "are updated to match the latest version number"
    )
