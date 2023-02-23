# pyright: reportUnusedVariable=false
# pyright: reportGeneralTypeIssues=false
# flake8: noqa

import lotto.model
import pytest


## Lotto Length tests
def test_proper_lotto_length():
    proper_lotto = lotto.model.Lotto([1, 2, 3, 4, 5, 6])
    assert len(proper_lotto) == lotto.model.LOTTO_LENGTH


def test_longer_lotto_length():
    with pytest.raises(ValueError):
        longer_lotto = lotto.model.Lotto([1, 2, 3, 4, 5, 6, 7])


def test_shorter_lotto_length():
    with pytest.raises(ValueError):
        shorter_lotto = lotto.model.Lotto([1, 2, 3, 4, 5])


## Lotto with invalid LottoNumber test.
def test_invalid_lotto_number():
    with pytest.raises(ValueError):
        improper_lotto = lotto.model.Lotto([1, 2, 3, 4, 5, 46])


## Duplication test.
def test_not_duplicated_lotto():
    proper_lotto = lotto.model.Lotto([1, 2, 3, 4, 5, 6])
    assert all(
        proper_lotto.LottoNumbers[i] < proper_lotto.LottoNumbers[i + 1] for i in range(lotto.model.LOTTO_LENGTH - 1)
    )


def test_duplicated_lotto():
    with pytest.raises(ValueError):
        duplicated_lotto = lotto.model.Lotto([1, 1, 2, 3, 4, 5])
