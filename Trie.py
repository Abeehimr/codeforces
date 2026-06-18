class Trie:
    __slots__ = ('children', 'is_end', 'size')
    ALPHABET_SIZE = 10

    def __init__(self, *words):
        self.children = []
        self.is_end   = []
        self.size     = 0
        self._new_node()          # node 0 = root
        for word in words:
            self.add(word)

    def _new_node(self):
        node = self.size
        self.children.extend([-1] * self.ALPHABET_SIZE)  # 10 slots appended
        self.is_end.append(False)
        self.size += 1
        return node

    def add(self, word):
        node = 0
        for ch in word:
            idx = node * self.ALPHABET_SIZE + (ord(ch) - 48)
            if self.children[idx] == -1:
                self.children[idx] = self._new_node()
            node = self.children[idx]
        self.is_end[node] = True

    def __contains__(self, word):
        node = 0
        for ch in word:
            idx = node * self.ALPHABET_SIZE + (ord(ch) - 48)
            node = self.children[idx]
            if node == -1:
                return False
        return self.is_end[node]

    def __delitem__(self, word):
        node = 0
        path = []
        for ch in word:
            idx = node * self.ALPHABET_SIZE + (ord(ch) - 48)
            path.append((node, idx))
            node = self.children[idx]
        self.is_end[node] = False
        # prune dead branches bottom-up
        for parent_node, idx in reversed(path):
            child = self.children[idx]
            # only delete if leaf and not an end
            if not self.is_end[child] and not any(
                self.children[child * self.ALPHABET_SIZE + d] != -1
                for d in range(self.ALPHABET_SIZE)
            ):
                self.children[idx] = -1
            else:
                break

    def get_node(self, digit_ord, node):
        child = self.children[node * self.ALPHABET_SIZE + digit_ord - 48]
        return child

    def is_end_node(self, node):
        return self.is_end[node]