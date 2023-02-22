"""
Define class Lotto.
"""
from typing import List
from .lotto_number import LottoNumber

LOTTO_LENGTH = 6


class Lotto:
    def __init__(self, numbers: List[int]):
        if len(numbers) > LOTTO_LENGTH:
            raise ValueError("Exceeded length.")
        if len(numbers) < LOTTO_LENGTH:
            raise ValueError("Lack of numbers.")
        numbers.sort()
        if not all(numbers[i] < numbers[i + 1] for i in range(LOTTO_LENGTH - 1)):
            raise ValueError("Duplicated.")
        self.LottoNumbers = [LottoNumber(number) for number in numbers]

    def __len__(self):
        return len(self.LottoNumbers)
