import binascii
import re

ciphertext = raw_input("Enter ciphertext: ")
key = raw_input("Enter key: ")

ciphertextArray = []
ciphertextValues = []
ciphertextwords = []

#array of indexs in string that have "abcde" one that changes is +5
firstarray = [m.start() for m in re.finditer('abcde', ciphertext)]
secondarray = []
for index in firstarray:
    secondarray.append(index + 5)


for i in ciphertext:
    ciphertextwords.append(i)

badcounter = 0
badbad = 0
for i in secondarray:
    del ciphertextwords[secondarray[badcounter] - (badbad * 5) - 1]
    del ciphertextwords[secondarray[badcounter] - (badbad * 5) - 2]
    del ciphertextwords[secondarray[badcounter] - (badbad * 5) - 3]
    del ciphertextwords[secondarray[badcounter] - (badbad * 5) - 4]
    del ciphertextwords[secondarray[badcounter] - (badbad * 5) - 5]
    badcounter += 1
    badbad += 1


#convert ciphertext to binary
for letter in ciphertextwords:
    ciphertextArray.append(bin(int(binascii.hexlify(letter), 16)))

#converts ciphertext to ascii
for item in ciphertextArray:
    ciphertextValues.append(int(item,2) + 19)


c = 1
for num in secondarray:
    ciphertextValues[num - 5 * c] -= 32
    c += 1


#Beginning of key
keyArray = []
threekeyArray = []
keyValues=[]

#turns key binary into an array
number = 0
for letter in key:
    keyArray.append(bin(int(binascii.hexlify(letter), 16)))
    twokeyArray = []
    for x in keyArray[number]:
        if x != "b":
            twokeyArray.append(x)
    number += 1
    threekeyArray.append(twokeyArray)

#adds the value of bits depending on location
for array in threekeyArray:
    total = 0
    num = 8
    for place in array:
        place = int(place)
        if place == 1:
            total += num
        num -= 1
    keyValues.append(total)

#print "key values: %s" % keyValues
keylength = len(key)
ciphertextlength = len(ciphertextArray)

plainArray = []
keycounter = 0
ciphertextCounter = 0

#changes ciphertext values based on the key
for i in ciphertextValues:
    while ciphertextCounter < ciphertextlength:
        popo = ciphertextValues[ciphertextCounter]
        if keycounter >= keylength:
            keycounter = 0
        j = keyValues[keycounter]
        j = int(j)
        keycounter += 1
        ciphertextCounter += 1
        plainArray.append(popo - j)

for i in plainArray:
    i = int(i)

#prints the ciphertext
plainString = ""
for char in plainArray:
        plainString += chr(char)

print ("Plaintext: %s" %plainString)
