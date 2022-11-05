# data = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
import re

regex = r"([a-z]?)"
    
match = re.search(regex, "i am") 

print(bool(match))