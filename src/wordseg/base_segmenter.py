import concurrent.futures as cf
from abc import ABCMeta, abstractmethod


class BaseSegmenter(metaclass=ABCMeta):
    """Base class of a word segmentation model."""

    @abstractmethod
    def fit(self, sents):
        """Train the model with the input segmented sentences.

        No cleaning or preprocessing (e.g, normalizing upper/lowercase,
        tokenization) is performed on for the training data.

        For consistency across all word segmentation model classes,
        the input to training must be an iterable of segmented sentences,
        even though some models could have used simpler data structure
        for training (e.g., just a wordlist for the longest string matching
        model).

        Parameters
        ----------
        sents : Iterable[Iterable[str]]
            An iterable of segmented sentences
        """
        pass

    def predict(self, sent_strs):
        """Segment the given unsegmented sentences.

        Parameters
        ----------
        sent_strs : Iterable[str]
            An iterable of unsegmented sentences

        Returns
        -------
        Iterable[Iterable[str]]
            A generator of segmented sentences
        """
        with cf.ThreadPoolExecutor() as executor:
            sents_predicted = executor.map(self._predict_sent, sent_strs, chunksize=16)
        return sents_predicted

    @abstractmethod
    def _predict_sent(self, sent_str):
        """Segment the given unsegmented sentence.

        Parameters
        ----------
        sent_str : str
            An unsegmented sentence

        Returns
        -------
        Iterable[str]
            A segmented sentence
        """
        pass
