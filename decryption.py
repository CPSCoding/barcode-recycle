import binascii
import re

ciphertext = '029abcde10394819abcde123' #raw_input("Enter ciphertext: ")
key = 'j' #raw_input("Enter key: ")

ciphertextArray = []
ciphertextValues = []

#convert ciphertext to binary
for letter in ciphertext:
    ciphertextArray.append(bin(int(binascii.hexlify(letter), 16)))

#converts ciphertext to ascii
for item in ciphertextArray:
    ciphertextValues.append(int(item,2))



'''for char in ciphertext:
    if 'abcde' in ciphertext:
        print "it works"
        print ciphertext.index('e')



for char in ciphertext:
    if char == "a":
        print ciphertext.index(char)
        #if ciphertext[ciphertext.index(char + 1)] == "b":
        #    print "success" '''

#array of indexs in string that have "abcde" one that changes is +5
firstarray = [m.start() for m in re.finditer('abcde', ciphertext)]
secondarray=[]
for index in firstarray:
    secondarray.append(index + 5)

print secondarray
