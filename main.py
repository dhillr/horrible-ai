import random

class WordPairs:
    def __init__(self, words, weights, single_weights):
        self.words = words
        self.weights = weights
        self.single_weights = single_weights

        self.word_weights = []

        self.words_s = []
        for item in self.single_weights:
            self.words_s.append(item[0][0])

        for item in self.weights:
            t = (item[0][0], int(item[1][0]))
            u = (item[0][1], int(item[1][1]))

            if not self.word_weights.__contains__(t): self.word_weights.append(t)
            if not self.word_weights.__contains__(u): self.word_weights.append(u)

        print(self.words[-1], self.word_weights[-1])

def parse_wpf():
    wpf = open("wpf.dat", "r").read()

    lines = wpf.split("\n")

    res = []
    res_s = []
    words = []

    for i in range(0, len(lines)-1, 2):
        pair = lines[i].split(" ")
        weights = lines[i+1]

        for word in pair:
            if not words.__contains__(word): words.append(word)

        if len(pair) == 1:
            res_s.append((pair, weights.split(" ")))
        else:
            res.append((pair, weights.split(" ")))

    return WordPairs(words, res, res_s)

parsed = parse_wpf()

def respond(prompt: str):
    word = random.choice(parsed.words_s)
    prev_word = word
    count = 0

    res = ""
    while count < 256:
        prev_word = word
        res += word + " "

        possible_matches = []
        for pair in parsed.weights:
            if pair[0][1] == word and (pair[0][0] == prev_word if prev_word != word else True):
                for i in range(parsed.word_weights[parsed.words.index(pair[0][2])][1]):
                    possible_matches.append(pair[0][2])

                    if prompt.lower().__contains__(pair[0][1].lower()):
                        for i in range(50):
                            possible_matches.append(pair[0][2])

        if len(possible_matches) > 0:
            word = random.choice(possible_matches)
        else:
            break

        count += 1

    return res

while True: print(respond(input(">>> ")))