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
        pass


    def list_words(self):
        pass

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



