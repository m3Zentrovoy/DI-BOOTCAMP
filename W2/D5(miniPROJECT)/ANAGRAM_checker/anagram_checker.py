import os

class AnagramChecker:
    def __init__(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path, "sowpods.txt")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                self.sowpods = set(word.strip().lower() for word in file.read().split())
                self.anagram_dict = {}
                for word in self.sowpods:
                    sorted_key = ''.join(sorted(word))
                    self.anagram_dict.setdefault(sorted_key, []).append(word)
        except FileNotFoundError:
            print(f"Error: {file_path} not found!")
            self.sowpods = set()
            self.anagram_dict = {}
        except Exception as e:
            print(f"An error occurred: {e}")
            self.sowpods = set()
            self.anagram_dict = {}

    def is_valid_word(self, word):
        if not isinstance(word, str) or not word:
            return False
        return word.lower() in self.sowpods

    def is_anagram(self, word1, word2):
        return (isinstance(word1, str) and isinstance(word2, str) and word1 and word2 and
                ''.join(sorted(word1.lower())) == ''.join(sorted(word2.lower())))

    def get_anagrams(self, word):
        if not isinstance(word, str) or not word:
            return []
        sorted_key = ''.join(sorted(word.lower()))
        anagrams = self.anagram_dict.get(sorted_key, [])
        return [w for w in anagrams if w.lower() != word.lower()]