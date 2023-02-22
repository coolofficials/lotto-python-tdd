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

    def _is_valid_operand(self, other: "LottoNumber"):
        return hasattr(other, "number")

    def __lt__(self, other: "LottoNumber"):
        if not self._is_valid_operand(other):
            return NotImplemented
        return self.number < other.number
