from dataclasses import dataclass
from enum import Enum, auto
from typing import Sequence, Tuple


class Feedback(Enum):
    RIGHT_PLACE = auto()
    WRONG_PLACE = auto()
    WRONG = auto()

@dataclass
class Result:
    win: bool
    feedback: Sequence[Tuple[str, Feedback]]

class InvalidAttempt(Exception):
    pass

@dataclass
class Termo:
    word: str

    def feedback(self, guess: str):
        if len(guess) != len(self.word):
            raise InvalidAttempt()
        for index, c in enumerate(guess):
            if c == self.word[index]:
                yield c, Feedback.RIGHT_PLACE
            elif c in self.word:
                yield c, Feedback.WRONG_PLACE
            else:
                yield c, Feedback.WRONG

    def test(self, guess: str) -> Result:
        return Result(
            win=self.word==guess,
            feedback=list(self.feedback(guess))
        )
