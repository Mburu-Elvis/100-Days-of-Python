'''
Dictionaries are a list of key value pairs enclosed in a {}
Each key value pair is separated by a comma
'''

programming_dict = {
    "Bug": "An error occured",
    "Function": "my_dict"
    }

programming_dict["Loop"] = "We go back and start again"

print(programming_dict)

# looping through a dictionary

for key, value in programming_dict.items():
    print(key, value)

for key in programming_dict:
    print(programming_dict[key])