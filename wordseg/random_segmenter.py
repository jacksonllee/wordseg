import random

from wordseg.base_segmenter import BaseSegmenter


# TODO: RandomSegmenter takes a random seed.


class RandomSegmenter(BaseSegmenter):
    """A random segmenter.

    Segmentation is predicted at random at each potential word
    boundary independently for a given probability. No training is required.
    """

    def __init__(self, *, prob):
        """Initialize a random segmenter.

        Parameters
        ----------
        prob : float
            The probability from [0, 1) that segmentation occurs between
            two symbols.

        Raises
        ------
        ValueError
            If prob is outside [0, 1).
        """
        self.prob = prob
        if not 0 <= self.prob < 1:
            raise ValueError(f"prob must be from [0, 1): {prob}")

    def fit(self, sents):
        raise NotImplementedError("No training needed for RandomSegmenter")

    def _predict_sent(self, sent_str):
        segment_or_not = [self.prob > random.random() for _ in range(len(sent_str) - 1)]
        boundaries = [i + 1 for i, seg in enumerate(segment_or_not) if seg]
        sent = []
        for i, j in zip([0] + boundaries, boundaries + [len(sent_str)]):
            word = sent_str[i:j]
            sent.append(word)
        return sent
