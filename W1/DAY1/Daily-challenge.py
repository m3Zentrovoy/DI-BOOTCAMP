import random
user_inp = (input('Input string (must be exactly 10 characters long) '))
if len(user_inp) > 10:
        print("String too long.")

elif len(user_inp) < 10:
    print('String not long enough.')

else:
    x = user_inp[0]
    y = user_inp[-1]
    print(f"Perfect string {x}{y}")

for i in range(len(user_inp)):
     print(user_inp[:i+1])

b = list(user_inp)
random.shuffle(b)
print(''.join(b))