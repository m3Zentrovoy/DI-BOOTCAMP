# What is a class?
# It’s like a plan for stuff in Python,
# like I can make a "Dog" class to give dogs names and barks.

# What is an instance?
# It’s when I make a real thing from a class, 
# like my_dog = Dog("Buddy") is my dog.

# What is encapsulation?
# It’s hiding stuff in a class so no one can mess with it, 
# like keeping a dog’s age secret.

# What is abstraction?
# It’s hiding hard stuff and showing only what I need,
#  like driving a car without knowing the engine.

# What is inheritance?
# It’s when a class gets things from another, 
# like my "Dog" class getting eating from "Animal".

# What is multiple inheritance?
# It’s when a class gets stuff from two parents,
#  like "FlyingFish" getting flying and swimming.

# What is polymorphism?
# It’s when classes use the same method but do different things,
#  like "Dog" barks and "Cat" meows.

# What is method resolution order or MRO?
# It’s the order Python looks at parents, 
# like checking "FlyingFish", then "Bird", then "Fish".


#ex2

import random

class Card:

    def __init__(self,suit, value):
        self.suit = suit
        self.value  = value


    def __str__(self):
        return f"{self.value} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.value = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = []
        for s in self.suit:
            for v in self.value:
                self.cards.append(Card(s, v))


    def shuffle(self):
          
        if len(self.cards) != 52:
            self.cards = []
            for s in self.suit:
                for v in self.value:
                    self.cards.append(Card(s, v))   
        else:
            print(f"Created {len(self.cards)} cards")   
         
        random.shuffle(self.cards)      
        for card in self.cards:
            
            print(card)


    def deal(self):
        one_card = random.choice(self.cards)
        self.cards.remove(one_card)
        print(f'One card from deck - {one_card}')
        print(f"Created {len(self.cards)} cards")  

 

deck = Deck()
deck.shuffle()
deck.deal()




