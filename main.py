class Node:
    def __init__(self):
        self.children = dict()
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = Node()

            current_node = current_node.children[c]
        current_node.end_of_word = True

    def search(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return current_node.end_of_word

    def delete(self, word):
        self._delete(self.root, word, 0)


    def has_prefix(self, prefix):
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return True

    def start_with_prefix(self, prefix):
        words = []
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return words
            current_node = current_node.children[c]
        def _dfs(current_node, path):
            if current_node.end_of_word:
                words.append(''.join(path))
            for c, child_node in current_node.children.items():
                _dfs(child_node, path + [c])
        _dfs(current_node, list(prefix))
        return words


    def list_words(self):
        words = []
        current_node = self.root
        def _dfs(current_node, path):
            if current_node.end_of_word:
                words.append(''.join(path))
            for c, child_node in current_node.children.items():
                _dfs(child_node, path + [c])
        _dfs(current_node, [])
        return words


    def _delete(self, current_node, word, index):
        if index == len(word):
            if not current_node.end_of_word:
                return False
            current_node.end_of_word = False
            return len(current_node.children) == 0
        c = word[index]
        node = current_node.children.get(c)
        if node is None:
            return False
        delete_current_node = self._delete(node, word, index + 1)
        if delete_current_node:
            del current_node.children[c]
            return len(current_node.children) == 0 and not current_node.end_of_word
        return False



# if __name__ == "__main__":
#     trie = Trie()
#
#     trie.insert("hello")
#     trie.insert("henry")
#     trie.insert("mike")
#     trie.insert("minimal")
#     trie.insert("minimum")
#     trie.insert("mini")
#
#     print(trie.list_words())
#
#     print(trie.has_prefix("mi"))
#     print(trie.start_with_prefix("h"))
#
#     trie.delete("minimum")
#
#     print(trie.search("hello"))
#     print(trie.search("henry"))
#     print(trie.search("mi"))
#
#     print(trie.list_words())
#
#     print(trie.insert("minimum"))
#
#     print(trie.start_with_prefix("mini"))


