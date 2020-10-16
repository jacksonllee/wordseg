from wordseg import LongestStringMatching


def test_basic():
    model = LongestStringMatching(max_word_length=4)
    model.fit(
        [
            ("this", "is", "a", "sentence"),
            ("that", "is", "not", "a", "sentence"),
        ]
    )
    assert list(model.predict(["thatisadog", "thisisnotacat"])) == [
        ["that", "is", "a", "d", "o", "g"],
        ["this", "is", "not", "a", "c", "a", "t"],
    ]
