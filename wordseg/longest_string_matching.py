from wordseg.base_segmenter import BaseSegmenter


class LongestStringMatching(BaseSegmenter):
    """Longest string matching segmenter.

    This model constructs predicted words by moving from left to right
    along an unsegmented sentence and finding the longest matching words,
    constrained by a maximum word length parameter.
    """

    def __init__(self, *, max_word_length):
        """Initialize a longest string matching segmenter.

        Parameters
        ----------
        max_word_length : int
            Maximum word length in the segmented sentences during prediction

        Raises
        ------
        ValueError
            If max_word_length is < 2.
        """
        self.max_word_length = max_word_length
        if self.max_word_length < 2:
            raise ValueError(
                f"max_word_length must be >= 2 to be meaningful: {max_word_length}"
            )

    def fit(self, sents):
        self._words = set()
        for sent in sents:
            self._words |= set(sent)

    def _predict_sent(self, sent_str):
        sent_predicted = []
        max_word_length = min(len(sent_str), self.max_word_length)

        i = 0
        j = i + max_word_length

        while i < len(sent_str):
            j = min(j, len(sent_str))
            test = sent_str[i:j]

            if len(test) == 1 or test in self._words:
                sent_predicted.append(test)
                i = j
                j = i + max_word_length
            else:
                j -= 1

        return sent_predicted
