import os
import random
import json
dir_path = os.path.dirname(os.path.realpath(__file__))



def get_words_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file_object:
            lines = file_object.readlines()
            return [word for line in lines for word in line.split()]
    except FileNotFoundError:
        print(f"Error: file {file_path} not found!")
        return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

def get_random_sentence(length_sentence):
    file_path = os.path.join(dir_path, "secrett.txt")
    words_list = get_words_from_file(file_path)
    
    if not words_list:
        return "Error: the word list is empty!"
    
    selected_words = random.choices(words_list, k=length_sentence)
    return " ".join(selected_words).lower()

def main():
    print('The program generates a random lowercase sentence from a word list based on user-specified length.')
    
    user_len = input('What is the desired sentence length? ')
    
    try:
        length = int(user_len)
    except ValueError:
        print("Error: please enter an integer!")
        return
    
    if not 2 <= length <= 20:
        print("Error: the number must be between 2 and 20 inclusive!")
        return
    
    sentence = get_random_sentence(length)
    print("Generated sentence:", sentence)

if __name__ == "__main__":
    main()





#ex2

sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

dictonar = json.loads(sampleJson)
dictonar["company"]["employee"].update({"birth_date" : "1995-03-09"})

with open(os.path.join(dir_path, "employee_data.json"), 'w', encoding='utf-8') as f:
    json.dump(dictonar, f, indent=4)

print(dictonar["company"]["employee"]["payable"]["salary"])

