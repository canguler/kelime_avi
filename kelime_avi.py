__author__ = 'can'


class Trie(dict):
    def add_word(self, word):
        trie = self
        for letter in word:
            trie = trie.setdefault(letter, Trie())

        trie['.'] = None

    def get_sub_trie(self, word):
        trie = self
        for letter in word:
            if letter in trie:
                trie = trie[letter]
            else:
                return None

        return trie


trie = Trie()
with open('kelimeler.txt') as f:
    for line in f:
        word = line.strip().lower()
        if ' ' not in word:
            trie.add_word(word)


def bfs(letter_matrix, n):
    import queue
    found_words = set()
    q = queue.Queue()

    for row in range(n):
        for col in range(n):
            q.put(((row, col), ))

    while not q.empty():
        path = q.get()
        row = path[-1][0]
        col = path[-1][1]

        # print(path)
        def get_word(path):
            if len(path) == 0:
                return ''
            return letter_matrix[path[0][0]][path[0][1]] + get_word(path[1:])

        word = get_word(path)
        sub_trie = trie.get_sub_trie(word)
        if sub_trie is not None:
            if '.' in sub_trie:
                found_words.add(word)
        else:
            continue

        def add_node(new_row, new_col):
            if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in path:
                q.put(path + ((new_row, new_col), ))

        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                add_node(row + i, col + j)

    return found_words

def new_game():
    import math
    letters = input('Letters: ')
    n = int(math.sqrt(len(letters)))
    letter_matrix = []
    for i in range(n):
        letter_matrix.append([])
        for j in range(n):
            letter_matrix[i].append(letters[i * n + j])

    found_words = bfs(letter_matrix, n)
    for word in sorted(found_words, key=len):
        print(word)

while True:
    new_game()
