CHARACTERS = ["", "!", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


"""moveCharacter(character, shift)
    This function takes the parameter of character and 
    locates its position in the list of accepted characters.
    It then takes that index and adds shift to it, so the 
    character moves forward shift places"""
def moveCharacter(character, shift): 
    return(CHARACTERS[(shift % len(CHARACTERS) + 
    CHARACTERS.index(character)) % len(CHARACTERS)])

"""condenseList(list)
    this function takes a list and loops through
    its values, adding each part of the list onto
    a string. Essentially condensing a list with
    multiple values into a single string."""
def condenseList(list):
    condensedList = ""
    for i in range(0,len(list)):
        list[i] = str(list[i])
        condensedList = condensedList + list[i]
    return condensedList

"""moveStringSame(string, shift)
    This function just runs moveCharacter on
    every character in a string."""
def moveStringSame(string, shift):
    newList = []
    stringList = list(string)
    for i in range(0, len(stringList)):
        newList.append(moveCharacter(stringList[i], shift))
    return condenseList(newList)
    
"""stringToNumberList(string)
   This finds the index in the CHARACTERS list for each
   character in the string. Converting the string into a
   list of numbers."""
def stringToNumberList(string):
    stringList = list(string)
    newList = []
    for i in range(0, len(string)):
        newList.append(CHARACTERS.index(stringList[i]))
    return newList

"""negateList(list)
   This function takes each number in the list and multiplies
   it by -1, this allows for decryption by reversing the move."""
def negateList(list):
    newList = []
    for i in range(0, len(list)):
        newList.append(list[i] * -1)
    return newList

"""moveStringDiff(string, shiftList)
   This takes the string and changes each letter based off
   of each number in the shiftList. For example index 0 in string
   (which gets changed into list), moves shiftList[0] position."""
def moveStringDiff(string, shiftList):
    newList = []
    string = list(string)
    for i in range(0, len(string)):
        newList.append(moveCharacter(string[i], shiftList[i]))
    return(condenseList(newList))
    
"""encryptWithPass(toEncrypt, password)
   this just runs moveStringDiff with toEncrypt and a password
   which gets converted into a number."""
def encryptWithPass(toEncrypt, password):
    encryptedInput = moveStringDiff(toEncrypt, stringToNumberList(password))
    return encryptedInput

"""decryptWithPass(toDecrypt, password)
   runs encryptWithPass just with a negated password number
   string to reverse the encryption."""
def decryptWithPass(toDecrypt, password):
    decryptedInput = moveStringDiff(toDecrypt, negateList(stringToNumberList(password)))
    return decryptedInput

