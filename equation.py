class TooManyCharactersException(Exception):
    pass

def patterns(words):
    words = [str(word) for word in words]
    chars = []
    patterns = []
    for word in words:
        pattern = []
        for character in word:
            if character in chars:
                pattern.append(chars.index(character))
            else:
                chars.append(character)
                pattern.append(chars.index(character))
        patterns.append(pattern)
    return patterns

def generate_numbers(num_array, patterns):
    return [int("".join([str(num_array[i]) for i in pattern])) for pattern in patterns]

class Words(object):
    def __init__(self, *words):
        self.words = [word.upper() for word in words]
        self.verify()
        self.patterns = patterns(self.words)

    def verify(self):
        if len(set([c for word in self.words for c in word])) > 10:
            raise TooManyCharactersException("Please submit valid words")

class Numbers(object):
    def __init__(self, *numbers):
        self.numbers = numbers
        self.patterns = patterns(self.numbers)
