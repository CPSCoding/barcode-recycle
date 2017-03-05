import binascii

plaintext = "jackson" #raw_input("Enter message: ")
key = "boat"

plaintextArray = []
plaintextvalues = []

#convert plaintext into binary
for letter in plaintext:
    plaintextArray.append(bin(int(binascii.hexlify(letter), 16)))

#gives plaintext ascii value
for item in plaintextArray:
    plaintextvalues.append(int(item,2))

print plaintextvalues

keyArray = []
threekeyArray = []

keyValues=[]

#turns binary into an array
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


print(keyValues)

keylength = len(key)
plaintextlength = len(plaintext)
