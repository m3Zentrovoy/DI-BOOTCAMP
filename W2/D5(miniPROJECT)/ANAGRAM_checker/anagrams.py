from anagram_checker import AnagramChecker

def show_menu():
    print("Enter a word or 'exit' to quit")

def is_single_word(word):
    return len(word.split()) == 1

def is_alpha_only(word):
    return word.isalpha()

def main():
    checker = AnagramChecker()
    while True:
        show_menu()
        user_input = input(": ").strip()
        if user_input.lower() == "exit":
            print("Exiting program.")
            break
        if not is_single_word(user_input):
            print("Error: Please enter a single word.")
            continue
        if not is_alpha_only(user_input):
            print("Error: Only alphabetic characters are allowed.")
            continue
        if not checker.is_valid_word(user_input):
            print("Invalid word or not found in the list.")
            continue
        anagrams = checker.get_anagrams(user_input)
        if anagrams:
            print(f"The word '{user_input}' is a valid word and its anagrams are: {anagrams}")
        else:
            print(f"The word '{user_input}' is a valid word but has no anagrams.")

if __name__ == "__main__":
    main()