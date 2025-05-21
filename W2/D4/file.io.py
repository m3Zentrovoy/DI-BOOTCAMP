


#file i/o - input / output

# #old school way if opening python file
# file_object = open(r'/Users/zentrovoy/Documents/BOOTCAMP/W2/file.io.py')
# print(file_object)


# mofern school to open pythob file

# with open(r'/Users/zentrovoy/Documents/BOOTCAMP/W2/secret.txt', encoding='utf-8') as file_object:
#     out_put = file_object.read() #reterns the whole content of the file
#     out_put = file_object.readline() #returns 1 line
#     out_put = file_object.readlines() #reterns a list where each element is an element


import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(r'/Users/zentrovoy/Documents/BOOTCAMP/W2/starwars.txt','a' , encoding='utf-8') as file_object:
    out_put = file_object.readlines()
  
    name = ['SkyWalker']
    file_object.writelines(name)
    print('names aded suscesfylli')


 
    # for i, word in enumerate(out_put):
    #     if i == 4:
    #         split_word = word.split()
    #         print(', '.join(split_word))
    #         break

    # for i, word in enumerate(out_put):
    #     if i == 4:
    #         break
    #     split_word = word.split()
    #     print(', '.join(split_word))



    # for  word in out_put:
    #     for letter in word:
    #         letter_word = word.split()
    #         print(', '.join(letter.split()))

    







# with open(f'{dir_path}/secret.txt', 'a', encoding='utf-8') as file_obj:
#     # file_object.writelines('Hello Pythob I/O \n Todayy')

#     names = ['Aragorn\n' , 'Gandalf\n', 'Legolas\n']
#     file_obj.writelines(names)
#     print('names aded suscesfylli')


# for 