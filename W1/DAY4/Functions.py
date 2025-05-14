Function
syntax

def func_name():
    '''prints a phrase on the console''' #docstrings
    print('I am a function')

func_name()
print(func_name.__doc__)



# def greetings():
#     '''ПРИВЕТ'''
#     print('Здарова')

# greetings()



def greetings(language, username):
    if language == 'RU':
        print(f'Здарова ' + {username})
    elif language == 'ENG':
        print(f'Hello ' + {username})
    elif language == '中國':
        print(f'你好 ' + {username})
    else:
        print('language is not found')

#keywords arguments
greetings('RU','Rick')
greetings('ENG','Morty')
greetings('中國', '娜斯佳')




# create a function called contry_info than recieves a country name as arguiment 
# and prints the capital of the country. Make the country argument defoult



def contry_info(country_name = 'Naboo'):
    if country_name == 'France':
       print(f'The capital of {country_name} is Paris')
    elif country_name == 'Italy':
        print(f'The capital of {country_name} is Rome')
    elif country_name == 'Naboo':
        print(f'The capital of {country_name} is Theed')
    else:
        print('Counry name not found')

# contry_info()

# calculation(5,4)


#return keyword 
def calculation(num1, num2):
    result = num1 + num2
    return result

countries = ['Brazil', 'Israel', 'China']
def country_info(countries):
    for country in countries:
        if country == 'Israel':
            return country
        
print(country_info(countries))

#SCOPES
#global scopes: on the fail in general 
#local scopes: indeted block ( if statement , a for a loop, a functions ...)


global_var = 100

def calculation(a,b):
    addition = a+b
    substractions = a-b
    global_var = 50
    return addition,substractions
additional, substruct = calculation(5,7)
print(additional, substruct)
print(global_var)