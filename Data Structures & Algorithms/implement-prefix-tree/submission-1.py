class Trie:
    def __init__(self):
        self._children = [None for _ in range(26)]
        self._is_terminal = False

class PrefixTree:

    def __init__(self):
        self._root = Trie()

    def insert(self, word: str) -> None:
        curr = self._root
        for ch in word:
            index = ord(ch) - ord('a')
            if not curr._children[index]:
                curr._children[index] = Trie()
            curr = curr._children[index]
        curr._is_terminal = True


    def search(self, word: str) -> bool:
        curr = self._root
        for ch in word:
            index = ord(ch) - ord('a')
            if not curr._children[index]:
                return False
            curr = curr._children[index]
        return curr._is_terminal

    def startsWith(self, prefix: str) -> bool:
        curr = self._root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if not curr._children[index]:
                return False
            curr = curr._children[index]
        return any(curr._children) or curr._is_terminal