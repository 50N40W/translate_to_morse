import time
import numpy as np
import simpleaudio as sa

#for windows, can use the winsound implementation
#import winsound

#  2020 07 15   Howard Bishop
#  BSD clause 2 license
#  Plays a MSG in Morse, both audio and visual
#  Have not verified if simpleaudio works on windows
#     but winsound does NOT work on linux :-)
#  Dependencies: as indicated in the imports
#  To do:
#   1.  detect OS and switch which method is used to play beep.
#   2. Maybe add a gui for tone freq, wpm, msg, and num. or repetitions


#MSG is where you enter the string you want to see translated.
# could be more elaborate, but this is the uninteresting part :-)
MSG = 'using lower case, write some letters or 2 or 3 numbers. ok? hihi'
DIT_MILLISECONDS = 100
DIT_SECONDS = DIT_MILLISECONDS/1000
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


def linux_beep(dah_or_dit_time):
    """ making a linux compatible variable duration beep  Cribbed from: 
    https://simpleaudio.readthedocs.io/
    en/latest/tutorial.html#playing-audio-directly
    This is a pretty crude implementation """
    fs = 44100
    seconds = 1  # Note duration of 3 seconds

    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * fs, False)
    note = np.sin(FREQ * t * 2 * np.pi)
    
    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    # Convert to 16-bit data
    audio = audio.astype(np.int16)
    
    # Start playback
    play_obj = sa.play_buffer(audio, 1, 2, fs)
    time.sleep(dah_or_dit_time)
    play_obj.stop()

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
                    linux_beep(dah_dit*DIT_SECONDS)
                    #for windows, can use the winsound instead of linux_beep
                    #winsound.Beep(FREQ, dah_dit*DIT_MILLISECONDS)
                    time.sleep(DIT_SECONDS*3)
                print(" ", end="")
                time.sleep(0.4)
    print(" ")
    print("-Done-")
