# translate_to_morse
Converts a string to both audio and text Morse code representation.

From the file
 I am way too lazy to do the "a = '.-',  b = '-...' thing, so ...
  making a dah 3x the length of a dit, we can use the ASCII order (or ordinality) 
  to equate an "a" to a tone one unit long followed by a  tone 3 time units long. 
  Each time unit is DIT_MILLISECONDS. The numbers are done 
 similarly, and the special characters are added to the end

 thus "LETTERS" contains our Morse alphabet, numbers, and some special 
 characters, all represented as 1's and 3's
LETTERS = [13, 3111, 3131, 311, 1, 1131, 331, 1111, 11, 11333, 313, # a-k
        1131, 33, 31, 333, 1331, 3313, 131, 111, 3, 113, 1113,      # L-V
        133, 3113, 3133, 3311, 6,                                   # W-Z, gap
        33333, 13333, 11333, 11133, 11113, 11111,                   # 0-5
        31111, 33111, 33311, 33331, 33333,                          # 6-9
        131313, 331133, 113311, 31131, 133131]     # contents of SPECIAL_CHARS
        
these are the non a-z and 0-9 characters we want to translate. 
They correspond to the end (last line) of LETTERS

SPECIAL_CHARS = ['.', ',', '?', '/', '@']

ON_SCREEN is how a "1" shows up as a "." and a 3 as a "-" in the printout
  these are arbitrary. could just as easily be pigs and buffalo.  Try it.
#ON_SCREEN = [' ', 'pig.', ' ', 'BUFFALO.', ' ', '  ', 'X']
ON_SCREEN = [' ', '.', ' ', '-', ' ', '  ', 'X']
