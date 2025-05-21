from deep_translator import GoogleTranslator

def translate_words(source_words, target_lang):
    # Создаём переводчик
    translator = GoogleTranslator(source='auto', target=target_lang)
    
    # Переводим каждое слово и сохраняем в список
    translated_words = [translator.translate(word) for word in source_words]
    
    # Создаём словарь, где ключи — исходные слова, а значения — переведённые
    translation_dict = dict(zip(source_words, translated_words))
    
    return translation_dict

def main():
    print("Добро пожаловать в программу переводчика!")
    
    try:
        # Список слов для перевода
        source_words = ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
        print("Список слов для перевода:", source_words)

        # Запрашиваем целевой язык
        target_lang = input("Введите код языка, на который перевести текст (например, 'en' для английского, 'fr' для французского): ").strip().lower()

        # Переводим слова
        result = translate_words(source_words, target_lang)
        
        # Выводим результат
        print("Переведённый текст:", result)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Запускаем программу
if __name__ == "__main__":
    main()