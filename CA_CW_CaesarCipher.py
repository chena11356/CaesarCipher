#Made by William Chen and Alex Chen

from random import randint
from string import *

def reverseWord(s):
    """Reverses words s using while loop
returns reversed word"""
    i=len(s)-1 #while loop should run len(s)-1 times
    res="" #initialize the result
    while i>=0:
        temp=s[int(i)] #temporary value is the ith letter of s
        res=res+temp #add that value on to the result
        i-=1 #i decremented by 1
    return res

def randPhrases(lst): #lists of random phrases for creativity!
    if lst=="ed": #type of phrase chosen and then list chosen
        phrases=["Invalid input. ","Wrong. ","No. ","Why are you like this. ", "What you just typed is not E nor D. ","Incorrect input. "]
    elif lst=="compliment":
        phrases=["Good job! ","Nice job! ","Well done! ","Great! ","Fantastic! ","Smashing! ","Swell! ","Peachy! ","Not bad, you can follow basic directions! "]
    elif lst=="isdigit":
        phrases=["Invalid input. ","Completely wrong. ","Do you need to go back to preschool to learn what a number between 1 and 94 is? "]
    elif lst=="range":
        phrases=["Invalid input. ","Nope. ","Let me reiterate: your integer has to be between 1 and 94. ","That's not correct. "]
    elif lst=="direc":
        phrases=["Invalid input. ","Wrong. ","What you just typed is not + nor -. ","Please follow directions. ","Stop disobeying. We all want to go home. ","Mr Fomin, you're a smart man. You're better than this. "]
    elif lst=="redo":
        phrases=["Invalid input. ","Come on, we're almost done. ","Incorrect. ","Dude. Stop. ","Mr Fomin, please, I'm so tired. ","Do you want to do this again or not? "]
    return phrases[randint(0,len(phrases)-1)] #random index from 0 to the last index

def encrypt(message,eshift,oshift,direc): #encrypts message
    encrypted=""
    if direc=="+":
        mult=1
    elif direc=="-":
        mult=-1
    i=0
    while i <= len(message)-1: #converts message into ASCII
        if i%2==0:
            encrypted+=shift(message[i],eshift,mult)
        elif i%2==1:
            encrypted+=shift(message[i],oshift,mult)
        i+=1
    return encrypted
                         
def shift(character,shift,mult):
    char=ord(character)
    char+=(shift*mult)
    if char>126:
        char+=-95
    elif char<32:
        char+=95
    return chr(char)


def decrypt(message,eshift,oshift,direc):
    #Utilizes the encrypt function within to decrypt the message.
    #Effectively, if the encrypt function incremented the letter by a given number, to decrypt it, one would have to increment by the negation of that number.
    res=encrypt(message,(-1*int(eshift)),(-1*int(oshift)),direc)
    return res

def getIntInRange(a,b):
    ans=raw_input("Please input an integer between %d and %d. >>> " %(a,b))
    if ans.isdigit() == False:
        print randPhrases("isdigit")
        return getIntInRange(a,b)
    if a<=int(ans)<=b:
        return int(ans)
    else:
        print randPhrases("range")
        return getIntInRange(a,b)
    
def CaesarCipher(): #input validation gets ed, message, shift1, shift2, direct, and redo
    print "Would you like to encrypt or decrypt a message? Type E or D."
    ed=raw_input() #user inputs encryption/decryption
    ed=ed.lower() #turned to lowercase to ease software recognition of e or d
    while ed!="e" and ed!="d": #guardian
        print randPhrases("ed")+"Please type E or D."
        ed=raw_input()
        ed=ed.lower()
    print randPhrases("compliment")+"Now, please type in your message."
    message=raw_input() #user inputs message. This does not get checked for invalid inputs, as ANY printable character (character that can be inputted into the program) will work and can be shifted.
    #The following couple lines were used to test the code. It made message a string containing every single printable character.
    #message=""
    #print "The user input for the message and the reverseWord functions are disabled for testing."
    #for test in range(32,127):
    #    message+=chr(test)
    print "You will need an even shift."
    shift1=getIntInRange(1,94)
    print "You will need an odd shift too."
    shift2=getIntInRange(1,94)
    print randPhrases("compliment")+"Now, please type in the encryption direction. Type either + or -."
    direc=raw_input() #user inputs direction
    while direc!="+" and direc!="-": #guardian against non-directions
        print randPhrases("direc")+"Please type in the encryption direction. Type either + or -."
        direc=raw_input()
    if ed=='e':
        nmessage=reverseWord(encrypt(message,shift1,shift2,direc))
        #nmessage=reverseWord(nmessage) #used to test the code
        print 'Your encrypted message is: \n'+nmessage+'\n Your original message is: \n'+message
    elif ed=='d':
        nmessage=reverseWord(message)
        #nmessage=reverseWord(nmessage) #used to test the code
        nmessage=decrypt(nmessage,shift1,shift2,direc)
        print 'Your decrypted message is: \n'+nmessage+'\n Your original message is: \n'+message
    print "Do you want to encrypt or decrypt another message? Type in yes or no."
    redo=raw_input() #user inputs whether or not they want to do this again
    redo=redo.lower() #lowercase-ified to make easier for software to recognize
    while redo!="yes" and redo!="no": #guardian to make sure input is yes or no
        print randPhrases("redo")+"Please type in whether or not you want to encrypt or decrypt another message. Type yes or no."
        redo=raw_input()
        redo=redo.lower()
    if redo=="yes": #calls function again if user wants to redo
        CaesarCipher()
    if redo=="no": #says bye if user is done
        print "Goodbye!"

CaesarCipher() #calling main function
