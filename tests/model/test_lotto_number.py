# pyright: reportUnusedVariable=false
# pyright: reportGeneralTypeIssues=false
# flake8: noqa

import pytest

import lotto.model


def test_range_success():
    proper_lotto_number = lotto.model.LottoNumber(45)
    assert proper_lotto_number.number in range(lotto.model.MIN_LOTTO_NUMBER, lotto.model.MAX_LOTTO_NUMBER + 1)


def test_range_fail():
    with pytest.raises(ValueError):
        invalid_lotto_number = lotto.model.LottoNumber(46)


def test_null_number():
    with pytest.raises(Exception):
        empty_lotto_number = lotto.model.LottoNumber()
