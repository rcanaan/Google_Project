from dataclasses import dataclass
from AutoComplete import AutoCompleteData


@dataclass
class TrieNode:
    def __init__(self):
        self.children = dict()
        self.end_sen = False
        self.best_5_sen = list()
        self.depth = 0

    def add_sentence(self, suggest: AutoCompleteData):
        if len(self.best_5_sen) == 5:
            self.best_5_sen.append(suggest)
            self.best_5_sen = sorted(self.best_5_sen, key=lambda sentence: sentence.completed_sentence.strip().lower())
            self.best_5_sen = self.best_5_sen[:-1]
        else:
            self.best_5_sen.append(suggest)
        self.best_5_sen = sorted(self.best_5_sen, key=lambda sentence: sentence.completed_sentence.lower())

    def set_depth(self, d: int):
        self.depth = d
