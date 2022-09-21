#Generting a Key value
def generateKey(string, key):
	key = list(key)
	if len(string) == len(key):
		return(key)
	else:
		for i in range(len(string) -
					len(key)):
			key.append(key[i % len(key)])
	return("" . join(key))
	
#Starting_Encryption using Vigenere_Cipher concept
def cipherText(string, key):
	cipher_text = []
	for i in range(len(string)):
		x = (ord(string[i]) +
			ord(key[i])) % 26
		x += ord('A')
		cipher_text.append(chr(x))
	return("" . join(cipher_text))

#Final_Decryption using Vigenere_Cipher concept
def originalText(cipher_text, key):
    orig_text = []
    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) -
             ord(key[i]) + 26) % 26
        x += ord('A')
        orig_text.append(chr(x))
    return("" . join(orig_text))


#MAIN METHOD

string = "PROGRAMMING"
#string=input("Enter the message: ")
keyword = "CODE"
#keyword=input("Enter the string for key value: ")
#print("Original text:",string
print("Vigenere Cipher: ")
key = generateKey(string, keyword)
print(key)
cipher_text = cipherText(string,key)
print("Ciphertext: ", cipher_text)
original_text=originalText(cipher_text,key)
print("DecryptedText: ",original_text)

