import binascii
import re

ciphertext = '029abcdea0394819abcde123abcde d' #raw_input("Enter ciphertext: ")
key = 'boat' #raw_input("Enter key: ")

ciphertextArray = []
ciphertextValues = []
ciphertextwords = []

#array of indexs in string that have "abcde" one that changes is +5
firstarray = [m.start() for m in re.finditer('abcde', ciphertext)]
secondarray = []
for index in firstarray:
    secondarray.append(index + 5)

print secondarray

for i in ciphertext:
    ciphertextwords.append(i)

#print ciphertextwords.remove[secondarray[0] - 5]
badcounter = 0
badbad = 0
for i in secondarray:
    print ciphertextwords
    del ciphertextwords[secondarray[badcounter] - (badbad * 5) - 1]
    del ciphertextwords[secondarray[badcounter] - (badbad * 5) - 2]
    del ciphertextwords[secondarray[badcounter] - (badbad * 5) - 3]
    del ciphertextwords[secondarray[badcounter] - (badbad * 5) - 4]
    del ciphertextwords[secondarray[badcounter] - (badbad * 5) - 5]
    badcounter += 1
    badbad += 1

print ciphertextwords

for index in secondarray:
    letter = ciphertext[index]
    print int(bin(int(binascii.hexlify(letter), 16)),2) - 32



#convert ciphertext to binary
for letter in ciphertext:
    ciphertextArray.append(bin(int(binascii.hexlify(letter), 16)))

#converts ciphertext to ascii
for item in ciphertextArray:
    ciphertextValues.append(int(item,2))

print ciphertextValues


'''for char in ciphertext:
    if 'abcde' in ciphertext:
        print "it works"
        print ciphertext.index('e')
for char in ciphertext:
    if char == "a":
        print ciphertext.index(char)
        #if ciphertext[ciphertext.index(char + 1)] == "b":
        #    print "success"


#array of indexs in string that have "abcde" one that changes is +5
firstarray = [m.start() for m in re.finditer('abcde', ciphertext)]
secondarray=[]
for index in firstarray:
    secondarray.append(index + 5)

print secondarray'''


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
ciphertextlength = len(ciphertext)

plaintextArray = []
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
        plaintextArray.append(popo + j + 19)

for i in plaintextArray:
    i = int(i)
