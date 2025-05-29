def say_hello(name, city, state):
    
    name = input("write your name: ").split()
    city = input("write city: ").capitalize
    state = input("wtite state: ").capitalize
    
    
    print(f"Hello, {' '.join(name)}! Welcome to {city}, {state}!")
    
    
say_hello(['John', 'Smith'], 'Phoenix', 'Arizona')