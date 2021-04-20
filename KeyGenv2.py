import random
import string

def generate_key():

    key = []
    
    for x in range(255):
        string.ascii_lowercase
        key.insert(x, 
        random.choice(
            string.ascii_lowercase + 
            string.digits + 
            string.ascii_uppercase + 
            string.punctuation))
    return key
    
    
key = generate_key()
keystring = "" 
for x in key:
  keystring += x 
f = open("key.txt", "w")
f.write(keystring)
f.close()