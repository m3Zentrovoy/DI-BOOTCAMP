import os
import random
import json
import string
import re

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = "/Users/zentrovoy/Documents/BOOTCAMP/W2/D4/Exercise/secrett.txt"

STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "he",
    "in", "is", "it", "its", "of", "on", "that", "the", "to", "was", "were", "will", "with"
}

class Text:
    def __init__(self, text):
        self.text = text

    def word_frequency(self, target_word):
        if not isinstance(target_word, str):
            return None
        words = self.text.split()
        count = sum(1 for word in words if isinstance(word, str) and word.lower() == target_word.lower())
        return None if count == 0 else count

    def most_common_word(self):
        dict_word = {}
        words = self.text.split()
        for word in words:
            dict_word[word] = dict_word.get(word, 0) + 1
        if dict_word:
            return max(dict_word, key=dict_word.get)
        return None

    def unique_words(self):
        words = self.text.split()
        unique = set(words)
        return list(unique)

    @classmethod
    def from_file(cls, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file_object:
                content = file_object.read()
            return cls(content)
        except FileNotFoundError:
            print(f"Error: File {file_path} not found!")
            return None
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            return None

class TextModification(Text):
    def remove_punctuation(self):
        translator = str.maketrans("", "", string.punctuation)
        return self.text.translate(translator)

    def remove_stop_words(self):
        words = self.text.split()
        filtered_words = [word for word in words if word.lower() not in STOP_WORDS]
        return " ".join(filtered_words)

    def remove_special_characters(self):
        return re.sub(r'[^a-zA-Z0-9\s]', '', self.text)

text_instance = Text.from_file(file_path)

if text_instance:
    print("Text content:", text_instance.text)
    print("Frequency of 'hello':", text_instance.word_frequency("hello"))
    print("Most common word:", text_instance.most_common_word())
    print("Unique words:", text_instance.unique_words())

    text_mod = TextModification(text_instance.text)
    print("Text without punctuation:", text_mod.remove_punctuation())
    print("Text without stop words:", text_mod.remove_stop_words())
    print("Text without special characters:", text_mod.remove_special_characters())