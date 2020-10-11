# wordseg

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4077433.svg)](https://doi.org/10.5281/zenodo.4077433)
[![CircleCI](https://circleci.com/gh/jacksonllee/wordseg/tree/main.svg?style=svg)](https://circleci.com/gh/jacksonllee/wordseg/tree/main)

`wordseg` is a Python package of word segmentation models.

Table of contents:

* [Installation](https://github.com/jacksonllee/wordseg#installation)
* [Usage](https://github.com/jacksonllee/wordseg#usage)
* [License](https://github.com/jacksonllee/wordseg#license)
* [Changelog](https://github.com/jacksonllee/wordseg#changelog)
* [Citation](https://github.com/jacksonllee/wordseg#citation)

## Installation

`wordseg` is available through pip:

```bash
pip install wordseg
```

To install `wordseg` from the GitHub source:

```bash
git clone https://github.com/jacksonllee/wordseg.git
cd wordseg
pip install -r dev-requirements.txt  # For running the linter and tests
pip install -e .
```

## Usage

`wordseg` implements a word segmentation model as a Python class.
An instantiated model class object has the following methods
(emulating the scikit-learn-styled API for machine learning):

* `fit`: Train the model with segmented sentences.
* `predict`: Predict the segmented sentences from unsegmented sentences.

The implemented model classes are as follows:

* `RandomSegmenter`:
  Segmentation is predicted at random at each potential word
  boundary independently for some given probability. No training is required.
* `LongestStringMatching`: 
  This model constructs predicted words by moving
  from left to right along an unsegmented sentence and
  finding the longest matching words, constrained by a maximum word length parameter.

Sample code snippet:

```python
from wordseg import LongestStringMatching

# Initialize a model.
model = LongestStringMatching(max_word_length=4)

# Train the model.
# `fit` takes an iterable of segmented sentences (a tuple or list of strings).
model.fit(
    [
        ("this", "is", "a", "sentence"),
        ("that", "is", "not", "a", "sentence"),
    ]
)

# Make some predictions; `predict` gives a generator, which is materialized by list() here.
list(model.predict(["thatisadog", "thisisnotacat"]))
# [['that', 'is', 'a', 'd', 'o', 'g'], ['this', 'is', 'not', 'a', 'c', 'a', 't']]
# We can't get 'dog' and 'cat' because they aren't in the training data.
```

## Citation

Lee, Jackson L. 2020. wordseg: Word segmentation models in Python. https://doi.org/10.5281/zenodo.4077433

```bibtex
@software{leengrams,
  author       = {Jackson L. Lee},
  title        = {wordseg: Word segmentation models in Python},
  year         = 2020,
  doi          = {10.5281/zenodo.4077433},
  url          = {https://doi.org/10.5281/zenodo.4077433}
}
```

## License

MIT License. Please see [`LICENSE.txt`](https://github.com/jacksonllee/wordseg/blob/main/LICENSE.txt).

## Changelog

Please see [`CHANGELOG.md`](https://github.com/jacksonllee/wordseg/blob/main/CHANGELOG.md).
