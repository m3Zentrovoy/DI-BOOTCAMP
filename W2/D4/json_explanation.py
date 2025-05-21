import json 
import os    
dir_path = os.path.dirname(os.path.realpath(__file__))


#converting to a dict to json

my_family = {
    'parents' : ['Beth', 'jejrry'],
    'chlidren' :  ['Summer', 'Morty']
}


with open(f'{dir_path}/family.json', 'w') as f:
    json.dump(my_family, f)



json_my_family = json.dumps(my_family)
print(my_family)

#CONVER JSON INTO A DICT

with open(f'{dir_path}/family.json', 'r') as f:
   my_family_2  = json.load(f)
print(my_family_2)

parsed_family = json.loads(json_my_family)
print("parsed from json string (using loads")