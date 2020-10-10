import os
from setuptools import setup, find_packages


_THIS_DIR = os.path.dirname(__file__)
with open(os.path.join(_THIS_DIR, "README.md"), encoding="utf-8") as f:
    _LONG_DESCRIPTION = f.read().strip()

_VERSION = "0.0.1"


def main():
    setup(
        name="wordseg",
        version=_VERSION,
        description="Word segmentation models",
        long_description=_LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        url="https://github.com/jacksonllee/wordseg",
        author="Jackson L. Lee",
        author_email="jacksonlunlee@gmail.com",
        license="MIT License",
        packages=find_packages(),
        keywords=[
            "computational linguistics",
            "natural language processing",
            "NLP",
            "word segmentation",
            "linguistics",
            "corpora",
            "speech",
            "language",
        ],
        python_requires=">=3.6",
        setup_requires="setuptools>=39",
        install_requires=[],
        package_data={},
        data_files=[(".", ["README.md", "LICENSE.txt", "CHANGELOG.md"])],
        zip_safe=False,
        classifiers=[
            "Development Status :: 2 - Pre-Alpha",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Information Technology",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Topic :: Scientific/Engineering",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Topic :: Scientific/Engineering :: Human Machine Interfaces",
            "Topic :: Scientific/Engineering :: Information Analysis",
            "Topic :: Text Processing",
            "Topic :: Text Processing :: Filters",
            "Topic :: Text Processing :: General",
            "Topic :: Text Processing :: Indexing",
            "Topic :: Text Processing :: Linguistic",
        ],
    )


if __name__ == "__main__":
    main()
