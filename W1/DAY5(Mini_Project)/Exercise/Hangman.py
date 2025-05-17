
# Компьютер выбирает случайное слово и отмечает звездочками каждую букву каждого слова.
# Затем игроку предстоит угадать букву.
# Если эта буква есть в слове(ах), то компьютер вставляет ее во все правильные позиции слова.
# Если в слове(ах) нет буквы, то добавьте к виселице часть тела (голову, тело, левую руку, правую руку, левую ногу, правую ногу).
# Игрок будет продолжать угадывать буквы до тех пор, пока не разгадает слово (слова) (или фразу) или все шесть частей тела не окажутся на виселице.
# Игрок не может угадывать одну и ту же букву дважды.

import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
encrypt_word = '*' * len(word)
body_part = ['head', 'body', 'left arm', 'right arm', 'left leg', 'right leg']
gallows = []
guessed_letters = []

def show_word():
    print(encrypt_word)

def guess_letter(choose_letter):
    global encrypt_word, gallows
    valid_guess = True
    
    # Проверка на пустой ввод или пробел
    if not choose_letter or choose_letter.isspace():
        print("Please enter a letter, not a space!")
        return (False, False, False)
    
    # Проверка на длину ввода
    if len(choose_letter) != 1:
        print("Please enter exactly one letter!")
        return (False, False, False)
    
    # Проверка, что введённый символ — буква
    if not choose_letter.isalpha():
        print("Please enter a letter (a-z, A-Z)!")
        return (False, False, False)
    
    # Проверка на повторное угадывание
    if choose_letter in guessed_letters:
        print("You've already guessed that letter!")
        return (False, False, False)
    
    guessed_letters.append(choose_letter)
    encrypted_list = list(encrypt_word)
    letter_found = False
    
    # Проверяем, есть ли буква в слове
    for i, char in enumerate(word):
        if char == choose_letter:
            encrypted_list[i] = char
            letter_found = True
    
    # Обновляем зашифрованное слово
    encrypt_word = ''.join(encrypted_list)
    
    # Если буква не найдена, добавляем часть тела
    if not letter_found and len(gallows) < 6:
        gallows.append(body_part[len(gallows)])
    
    return (letter_found, encrypt_word == word, len(gallows) == 6)

# Игровой цикл
while True:
    show_word()
    print("Gallows:", gallows)
    guessed_letter = input("Try to guess a letter? ")
    result = guess_letter(guessed_letter)
    
    # Проверяем, валидный ли ход
    if result == (False, False, False):  # Невалидный ввод
        continue
    
    letter_found, word_guessed, game_over = result
    
    if word_guessed:
        print("Congratulations! You've guessed the word:", word)
        break
    if game_over:
        print("Game over! The word was:", word)
        print("Gallows:", gallows)
        break