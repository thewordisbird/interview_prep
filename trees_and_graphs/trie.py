class Node:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_node = self.root
        for i, char in enumerate(word):
            node = current_node.children.get(char)
            if not node:
                node = Node()
                current_node.children[char] = node
            current_node = node
        current_node.is_word = True

    def search(self, word):
        current_node = self.root
        for i, char in enumerate(word):
            node = current_node.children.get(char)
            if not node:
                return False
            current_node = node
        return current_node.is_word

    def delete(self, word):
        self._delete(self.root, word, 0)

    def _delete(self, current_node, word, index):
        # Returns True if the parent should delete the mapping
        if index == len(word):
            # when end if wird us reached only delete if current_node.is_word is True
            if not current_node.is_word:
                return False
            current_node.is_word = False
            # If current_node has no other mapping then return True
            return len(current_node.children) == 0
        
        char = word[index]
        node = current_node.children.get(char)
        if not node:
            return False
        delete_current_node = self._delete(node, word, index + 1)
        # If True is returned then delete thte mapping of char and the node refrerence from map
        if delete_current_node:
            del current_node.children[char]
            # Return True if no mappings are left
            return len(current_node.children) == 0
        
        return False
