# wordseg

[![CircleCI](https://circleci.com/gh/jacksonllee/wordseg/tree/main.svg?style=svg)](https://circleci.com/gh/jacksonllee/wordseg/tree/main)

`wordseg` is a Python package of word segmentation models.

Table of contents:

* [Usage](https://github.com/jacksonllee/wordseg#usage)
* [Installation](https://github.com/jacksonllee/wordseg#installation)
* [License](https://github.com/jacksonllee/wordseg#license)
* [Changelog](https://github.com/jacksonllee/wordseg#changelog)

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

## Installation

Python 3.6 or above is required.

To install from the command line:

```bash
pip install git+https://github.com/jacksonllee/wordseg@v0.0.1#egg=wordseg
```

To include this package in `requirements.txt` ...

```
git+https://github.com/jacksonllee/wordseg@v0.0.1#egg=wordseg
```

... or in `setup.py`:

```python
setup(
    # ...
    install_requires=[
        # ...
        "wordseg @ git+https://github.com/jacksonllee/wordseg@v0.0.1#egg=wordseg",
        # ...
    ],
    # ...
)
```

If you would like to install by cloning (e.g., for development):

```bash
git clone https://github.com/jacksonllee/wordseg.git
cd wordseg
pip install -r dev-requirements.txt  # For running the linter and tests
pip install -e .
```

## License

MIT License. Please see [`LICENSE.txt`](LICENSE.txt).

## Changelog

Please see [`CHANGELOG.md`](CHANGELOG.md).
