from dataclasses import dataclass


@dataclass
class AutoCompleteData:
    completed_sentence: str
    source_text: str
    offset: int
    score: int

    # methods that you need to define by yourself

    # TODO: insert function that whoul limit items to 5 items
    def __init__(self, sentence: str, source: str, offs: int):
        self.completed_sentence = sentence
        self.offset = offs
        self.source_text = source
        self.score = 0

    def add_score(self, score_: int):
        self.score += score_ * 2

    def print_suggest(self):
        print(f"{self.completed_sentence[:-1]}  ({self.source_text} {self.offset} {self.score})")
