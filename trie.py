# Prefix Trie
class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes
        self.children = {}
        # Flag to indicate the end of a word
        self.is_word_end = False

class Trie:
    def __init__(self):
        # Initialize the Trie with an empty root node
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert a word into the Trie.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                # Create a new node if the character is not present
                current.children[char] = TrieNode()
            current = current.children[char]
        # Mark the end of the word
        current.is_word_end = True

    def search(self, word):
        """
        Search for a word in the Trie.
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        # Check if the last node marks the end of a word
        return current.is_word_end

    def starts_with(self, prefix):
        """
        Check if any words in the Trie start with the given prefix.
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        # Check if any child node marks the end of a word
        return any(child.is_word_end for child in current.children.values())

    def longest_prefix(self, word):
        """
        Find the longest prefix of the given word present in the Trie.
        """
        node = self.root
        prefix = ""
        for char in word:
            if char not in node.children:
                break
            prefix += char
            node = node.children[char]
            if node.is_word_end:
                return prefix
        return prefix

    def delete(self, word):
        """
        Delete a word from the Trie.
        """
        self._delete_recursive(self.root, word, 0)

    def _delete_recursive(self, node, word, index):
        """
        Helper function for recursive deletion.
        """
        if index == len(word):
            # If the end of the word is reached, mark the node as not the end of a word
            if not node.is_word_end:
                return False
            node.is_word_end = False
            # Return True if the node has no children (can be deleted)
            return len(node.children) == 0

        char = word[index]
        if char not in node.children:
            # If the character is not present, the word is not in the Trie
            return False

        child = node.children[char]
        # Recursively delete the child node
        should_delete_child = self._delete_recursive(child, word, index + 1)

        if should_delete_child:
            # If the child node can be deleted, remove it from the current node's children
            del node.children[char]
            # Return True if the current node has no other children (can be deleted)
            return len(node.children) == 0

        return False

    def print_trie(self, node=None, level=0):
        """
        Print the Trie structure for visualization.
        """
        if node is None:
            node = self.root

        print("Level:", level, "Children:", list(node.children.keys()), "End of Word:", node.is_word_end)

        for char, child in node.children.items():
            self.print_trie(child, level + 1)


# Creating a new Trie and inserting words
trie1 = Trie()
words1 = ["car", "card", "care", "cared", "cars"]
for word in words1:
    trie1.insert(word)

# Searching for words in Trie1
print(trie1.search("card"))  # True
print(trie1.search("cares"))  # False

# Checking if any words start with a certain prefix
print(trie1.starts_with("car"))  # True
print(trie1.starts_with("cab"))  # False

# Finding the longest prefix of a word in Trie1
print(trie1.longest_prefix("caring"))  # 'car'
print(trie1.longest_prefix("bark"))    # ''

# Printing the Trie1 structure
trie1.print_trie()

# Deleting a word from Trie1
trie1.delete("card")
print(trie1.search("card"))  # False
trie1.print_trie()




# suffix and prefix Trie code


# class TrieNode:
#     def __init__(self):
#         # Dictionary to store child nodes
#         self.children = {}
#         # Flag to indicate the end of a word
#         self.is_end_of_word = False


# class Trie:
#     def __init__(self):
#         # Initialize the Trie with an empty root node
#         self.root = TrieNode()

#     def insert(self, word):
#         """
#         Insert a word into the Trie.
#         """
#         current = self.root
#         for char in word:
#             if char not in current.children:
#                 # Create a new node if the character is not present
#                 current.children[char] = TrieNode()
#             current = current.children[char]
#         # Mark the end of the word
#         current.is_end_of_word = True

#     def search(self, word):
#         """
#         Search for a complete word in the Trie.
#         """
#         current = self.root
#         for char in word:
#             if char not in current.children:
#                 return False
#             current = current.children[char]
#         # Check if the last node marks the end of a word
#         return current.is_end_of_word

#     def starts_with(self, prefix):
#         """
#         Check if any words in the Trie start with the given prefix.
#         """
#         current = self.root
#         for char in prefix:
#             if char not in current.children:
#                 return False
#             current = current.children[char]
#         # At least one child node indicates words starting with the prefix
#         return True

#     def ends_with(self, suffix):
#         """
#         Check if any words in the Trie end with the given suffix.
#         """
#         reversed_suffix = suffix[::-1]
#         current = self.root
#         for char in reversed_suffix:
#             if char not in current.children:
#                 return False
#             current = current.children[char]
#         # At least one child node indicates words ending with the suffix
#         return True

#     def search_prefix(self, prefix):
#         """
#         Retrieve all words in the Trie with a given prefix.
#         """
#         current = self.root
#         for char in prefix:
#             if char not in current.children:
#                 return []
#             current = current.children[char]
#         # Get all words starting with the prefix
#         return self._get_all_words(current, prefix)

#     def search_suffix(self, suffix):
#         """
#         Retrieve all words in the Trie with a given suffix.
#         """
#         reversed_suffix = suffix[::-1]
#         current = self.root
#         for char in reversed_suffix:
#             if char not in current.children:
#                 return []
#             current = current.children[char]
#         # Get all words ending with the suffix
#         return self._get_all_words(current, "")[::-1]

#     def _get_all_words(self, node, prefix):
#         """
#         Helper function to retrieve all words from a given Trie node.
#         """
#         words = []
#         if node.is_end_of_word:
#             words.append(prefix)
#         for char, child in node.children.items():
#             words.extend(self._get_all_words(child, prefix + char))
#         return words

#     def delete(self, word):
#         """
#         Delete a word from the Trie.
#         """
#         self._delete_recursive(self.root, word, 0)

#     def _delete_recursive(self, node, word, index):
#         """
#         Helper function for recursive deletion.
#         """
#         if index == len(word):
#             # If the end of the word is reached, mark the node as not the end of a word
#             if not node.is_end_of_word:
#                 return False
#             node.is_end_of_word = False
#             # Return True if the node has no children (can be deleted)
#             return len(node.children) == 0

#         char = word[index]
#         if char not in node.children:
#             # If the character is not present, the word is not in the Trie
#             return False

#         child = node.children[char]
#         # Recursively delete the child node
#         should_delete_child = self._delete_recursive(child, word, index + 1)

#         if should_delete_child:
#             # If the child node can be deleted, remove it from the current node's children
#             del node.children[char]
#             # Return True if the current node has no other children (can be deleted)
#             return len(node.children) == 0

#         return False


# # Example usage:
# trie = Trie()

# # Insert words into the Trie
# trie.insert("apple")
# trie.insert("application")
# trie.insert("apply")
# trie.insert("banana")
# trie.insert("orange")

# # Search for words
# print(trie.search("apple"))  # True
# print(trie.search("app"))    # False

# # Check if any words start with a certain prefix
# print(trie.starts_with("app"))  # True
# print(trie.starts_with("ban"))  # True

# # Check if any words end with a certain suffix
# print(trie.ends_with("le"))  # True
# print(trie.ends_with("na"))  # True
# print(trie.ends_with("xyz"))  # False

# # Retrieve all words with a given prefix
# print(trie.search_prefix("app"))  # ['apple', 'application', 'apply']

# # Retrieve all words with a given suffix
# print(trie.search_suffix("e"))  # ['apple', 'orange']

# # Delete a word from the Trie
# trie.delete("apple")
# print(trie.search("apple"))  # False
# print(trie.search_prefix("app"))  # ['application', 'apply']




# Suffix trie

# class SuffixTrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False


# class SuffixTrie:
#     def __init__(self):
#         self.root = SuffixTrieNode()

#     def insert_suffix(self, suffix):
#         current = self.root
#         for char in suffix:
#             if char not in current.children:
#                 current.children[char] = SuffixTrieNode()
#             current = current.children[char]
#         current.is_end_of_word = True

#     def build_suffix_trie(self, text):
#         for i in range(len(text)):
#             suffix = text[i:]
#             self.insert_suffix(suffix)

#     def search_suffix(self, suffix):
#         current = self.root
#         for char in suffix:
#             if char not in current.children:
#                 return False
#             current = current.children[char]
#         return current.is_end_of_word

#     def search_suffixes(self, suffix):
#         current = self.root
#         for char in suffix:
#             if char not in current.children:
#                 return []
#             current = current.children[char]
#         return self._get_all_suffixes(current, "")

#     def _get_all_suffixes(self, node, suffix):
#         suffixes = []
#         if node.is_end_of_word:
#             suffixes.append(suffix)
#         for char, child in node.children.items():
#             suffixes.extend(self._get_all_suffixes(child, suffix + char))
#         return suffixes


# # Example usage:
# suffix_trie = SuffixTrie()

# # Build suffix trie with a text
# text = "banana"
# suffix_trie.build_suffix_trie(text)

# # Search for specific suffixes
# print(suffix_trie.search_suffix("ana"))  # True
# print(suffix_trie.search_suffix("abc"))  # False

# # Search for all suffixes starting with a certain suffix
# print(suffix_trie.search_suffixes("an"))  # ['ana', 'anana']

# Insert more suffixes if needed
# suffix_trie.insert_suffix("example")

# Note: This example focuses on suffix operations, and you can customize it further based on your specific requirements.
