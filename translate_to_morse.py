import time
#import sys

#import ossaudiodev

#if you don't want to install pygame, and are running windows ...
#import winsound

#MSG is where you enter the string you want to see translated.
# could be more elaborate, but this is the uninteresting part :-)
MSG = 'using lower case, write some letters or 2 or 3 numbers. ok? hihi'
DIT_MILLISECONDS = 100
FREQ = 700
HOW_MANY_TIMES = 3


# I am way too lazy to do the "a = .-" thing, so ...
#  making a dah 3x the length of a dit, we can use the ASCII order 
#  (or ordinality) to equate an "a" to a tone one unit long followed by a
#  tone 3 units long. Each unit is DIT_MILLISECONDS. The numbers are done 
#  similarly, and the special characters are added to the end
#
# thus "LETTERS" contains our Morse alphabet, numbers, and some special
#  characters, all represented as 1's and 3's
LETTERS = [13, 3111, 3131, 311, 1, 1131, 331, 1111, 11, 11333, 313, # a-k
        1131, 33, 31, 333, 1331, 3313, 131, 111, 3, 113, 1113,      # L-V
        133, 3113, 3133, 3311, 6,                                   # W-Z, gap
        33333, 13333, 11333, 11133, 11113, 11111,                   # 0-5
        31111, 33111, 33311, 33331, 33333,                          # 6-9
        131313, 331133, 113311, 31131, 133131]     # contents of SPECIAL_CHARS

# these are the non a-z and 0-9 characters we want to translate. 
# They correspond to the end (last line) of LETTERS
SPECIAL_CHARS = ['.', ',', '?', '/', '@']

#ON_SCREEN is how a "1" shows up as a "." and a 3 as a "-" in the printout
#  these are arbitrary. could just as easily be pigs and buffalo.  Try it.
#ON_SCREEN = [' ', 'pig.', ' ', 'BUFFALO.', ' ', '  ', 'X']
ON_SCREEN = [' ', '.', ' ', '-', ' ', '  ', 'X']

def get_ordinal(inChar):
    """ return an index value from the letter ordinality """
    if inChar in SPECIAL_CHARS:
        index = SPECIAL_CHARS.index(inChar) + 38
    elif ord(inChar) in range (ord('a'), ord('z')):
        index = ord(inChar) - ord('a')
    elif inChar == ' ':
        index = 26
    elif (int(inChar) >= 0 & int(inChar) <= 9):
        index = int(inChar)+27
    else:
        print(inChar + "** Unsupported **")
        index = 27
    return index

if __name__ == '__main__':
    PARSED = MSG.split()
    for repeats in range(0,HOW_MANY_TIMES):
        for i in range(0, len(PARSED)):
            a_word = PARSED[i]
            time.sleep(1.1)
            print(" ")
            for dits in range(0, len(a_word)):
                morseChar = get_ordinal(a_word[dits])
                this_char = LETTERS[morseChar]
                str_char = str(this_char)
                sonic = []
                for x in str_char:
                    sonic.append(str(x))
                for s in range(0, len(sonic)):
                    dah_dit = int(sonic[s])
                    print(ON_SCREEN[dah_dit], end="")
                    #winsound.Beep(FREQ, dah_dit*DIT_MILLISECONDS)
                print(" ", end="")
                time.sleep(0.4)
                #x = ord
    print(" ")
    print("-Done-")
