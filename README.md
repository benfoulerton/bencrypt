# bencrypt.py

bencrypt is a python module for simple cipher-style encryption.
- 

Installation Guide
-
pip -m install bencrypt


Different functions:
-
* `moveCharacter(character, shift)` - This function takes a letter and moves it 'shift' places down the list of accepted characters (at the bottom) it returns the character at the index of 'character's index' + shift.

* `moveStringSame(string, shift)` - This function takes a string and moves all of its characters an equal amount down the list of accepted characters. It will return a string where each letter is shift places from each letter in the original string.

* `moveStringDiff(string, shiftList)` - This function takes a string and a list of numbers, each number corresponds to a character in the string. For example it gets string[0] and moves it shiftList[0] places.

* `encryptWithPass(toEncrypt, password)` - This function is just moveStringDiff but it accepts two strings and converts the second one (password) into the list of numbers in order to encrypt toEncrypt. The whole point of this "Encryption" is so you can only decrypt your password (or any string) using a master password.

* `decryptWithPass(toDecrypt, password)` - This function is encryptWithPass but the password's corresponding number list gets reversed (each number multiplied by -1) in order to decrypt toDecrypt.

Other Minor Functions
-
* `condenseList(list)` just gets every item in a list and condenses it into a string.

* `stringToNumberList(string)` takes the string, converts it into a list and finds the index of every character in that list on the accepted character list.

* `negateList(list)` takes each value in the list and multiplies them by -1


SPECIAL MENTIONS! 
-

* `for i in range(0, len(list))`
this has been my best friend so i can loop through a list and perform a function on each individual items in a list

* list(string)
this has been super useful for splitting a string into a list, to perform a function on each character, then use condenseList to put it back into a string

* modulo!! this lets me loop the indexes in the list. For example if I need to shift a character at the end of the list, it just loops back to the start when it gets to the end. This was the code I wrote to do that:
`return(CHARACTERS[(shift % len(CHARACTERS) + CHARACTERS.index(character)) % len(CHARACTERS)])`


Extra Notes
-

This is my first proper python project and I'd appreciate any feedback on this!
You can contact me at benfoulerton@gmail.com


!DISCLAIMER!
-
THIS IS JUST A FUN PROJECT I HAVE MADE, PLEASE DO NOT USE IT FOR ANYTHING THAT REQUIRES REAL ENCRYPTION