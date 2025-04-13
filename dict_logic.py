import json
from difflib import get_close_matches

class Dictionary:
    def __init__(self, data_path='data/data.json'):
        with open(data_path, 'r') as file:
            self.data = json.load(file)

    def get_meaning(self, word):
        word = word.lower()
        if word in self.data:
            return self.data[word], word, None
        elif len(get_close_matches(word, self.data.keys())) > 0:
            close_match = get_close_matches(word, self.data.keys())[0]
            return None, word, close_match
        else:
            return None, word, None
