
# Python3 program to implement XOR - Encryption
  
# The same function is used to encrypt and
# decrypt
def encryptDecrypt(inpString):
  
    # Define XOR key
    # Any character value will work
    with open('Key.txt','r') as file:
      xorKey = file.read()
    

    # calculate length of input string
    length = len(inpString);
  
    # perform XOR operation of key
    # with every caracter in string
    for i in range(length):
      
        inpString = (inpString[:i] + 
             chr(ord(inpString[i]) ^ ord(xorKey)) +
                     inpString[i + 1:]);
        print(inpString[i], end = "");
      
    return inpString;
  
# Driver Code
if __name__ == '__main__':
    
    with open('String.txt', 'r') as file:
      sampleString = file.read()
  
    # Encrypt the string
    sampleString = encryptDecrypt(sampleString);
    print(sampleString)

    with open('String.txt', 'w') as file:
      file.write(sampleString)