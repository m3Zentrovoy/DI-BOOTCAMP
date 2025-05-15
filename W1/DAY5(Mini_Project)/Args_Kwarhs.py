# Args_Kwarhs



# def say_hello(language, user_name):
#     if language == 'EN':
#         print(f'Hello, {user_name}')

# say_hello()


# def print_names(*args):
#     for name in args:
#         print(f'Hello {name}')
#     if not args:
#         print('please add names yo say hello')

# print_names()



# def user_name(**kvargs):
#     for info in kvargs.items():
#         print(info)

# user_name(name = 'Max', age  = 30, adress = 'Holon')



#create a functuon called - task_manager that accept tasks 
# and prints "today I need to dp : {task}"

# def task_manager(*args):
#     if args:
#         for task in args:
#             print(f"today I need to do {task}")
#     elif not args:
#        task = print(input('Please pass a taks as argument'))
       
# task_manager()




def party_planner(*args, **kwargs):
    if args:
        print('You need to bue')

        for arg in args:
            print(arg)
    else:
        print('There is no food to bue')
    if kwargs:
        print('Party details: ')

        for key, value in kwargs.items():
            print(f' {key} : {value}')


# party_planner('pizza','chips','cola', open = 9.00, pool_time = 12.00, close = 18.00)
# party_planner('pizza','chips','cola')
party_planner(open =  9.00, pool_time = 12.00, close = 18.00)


# 'pizza','chips','cola'


#exercise : 1 - 
#1 - Call this function and pass the party details. 
#2 - Call it only with food info
#2 - Call it with only the details


