"""
Define class LottoNumber.
"""

MIN_LOTTO_NUMBER = 1
MAX_LOTTO_NUMBER = 45


class LottoNumber:
    """
    Class defining number on each lotto ball.
    Number should satisfy MIN_LOTTO_NUMBER <= number <= MAX_LOTTO_NUMBER.
    """

    def __init__(self, number: int):
        if number not in range(MIN_LOTTO_NUMBER, MAX_LOTTO_NUMBER + 1):
            raise ValueError("Out of range")
        self.number = number
